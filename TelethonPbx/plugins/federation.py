import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from TelethonPbx.plugins import *


@Pbx_cmd(pattern="newfed(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    Pbx = await eor(event, "`Making new fed...`")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/newfed {Pbx_input}")
            response = await conv.get_response()
        except YouBlockedUserError:
            await parse_error(Pbx, "__Unblock @MissRose_Bot and try again__", False)
            return
        if response.startswith("You already have a federation"):
            await eod(Pbx, f"You already have a federation. Do `{hl}renamefed` to rename your current fed.")
        else:
            texts = response
            lists = texts.split("/joinfed")
            fedid = lists[1].strip()
            await Pbx.edit(f"**Newfed Created Successsfully!!** \n\n**Name:** `{Pbx_input}` \n**FedID:** `{fedid}`")
        await event.client.delete_messages(conv.chat_id, [first.id, response.id])


@Pbx_cmd(pattern="renamefed(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    Pbx = await eor(event, "`Trying to rename your fed...`")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/renamefed {Pbx_input}")
            await asyncio.sleep(2)
            response = await conv.get_response()
            await Pbx.edit(f"{response}")
            await event.client.delete_messages(conv.chat_id, [first.id, response.id])
        except YouBlockedUserError:
            await parse_error(Pbx, "__Unblock @MissRose_Bot and try again.__", False)
            return


@Pbx_cmd(pattern="fstat(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx = await eor(event, "`Collecting fstat....`")
    chat = "@MissRose_bot"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        lavde = str(previous_message.sender_id)
        user = f"[user](tg://user?id={lavde})"
    else:
        lavde = event.pattern_match.group(1)
    if not lavde:
        return await eod(Pbx, "`Need username/id to check fstat`")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                first = await conv.send_message("/fedstat " + lavde)
                await asyncio.sleep(4)
                response = await conv.get_response()
                await asyncio.sleep(2)
                await Pbx.edit(response)
                await event.client.delete_messages(conv.chat_id, [first.id, response.id])
            except YouBlockedUserError:
                await parse_error(Pbx, "__Unblock @MissRose_Bot and try again.__", False)


@Pbx_cmd(pattern="fedinfo(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx = await eor(event, "`Fetching fed info.... please wait`")
    chat = "@MissRose_bot"
    lavde = event.pattern_match.group(1)
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message("/fedinfo " + lavde)
            response = await conv.get_response()
            await Pbx.edit(response.text + "\n\n**ʟᴇɢᴇɴᴅᴀʀʏ_ᴀғ_🕊️⃝‌ᴘʙx ❤️ᥫ᭡፝֟፝֟**")
            await event.client.delete_messages(conv.chat_id, [first.id, response.id])
        except YouBlockedUserError:
            await parse_error(Pbx, "__Unblock @MissRose_Bot and try again.__", False)


CmdHelp("federation").add_command(
    "newfed", "<newfed name>", "Makes a federation of Rose bot"
).add_command(
    "renamefed", "<new name>", "Renames the fed of Rose Bot"
).add_command(
    "fstat", "<username/id>", "Gets the fban stats of the user from rose bot federation"
).add_command(
    "fedinfo", "<fed id>", "Gives details of the given fed id"
).add_info(
    "Rose Bot Federation."
).add_warning(
    "✅ Harmless Module."
).add()
