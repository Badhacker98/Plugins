import datetime
import random
import time
from unicodedata import name

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from TelethonPbx.DB.gvar_sql import gvarstat, addgvar
from TelethonPbx.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>╰•★★ 💫 🅟🅑🅧 🅑🅞🅣 🅐🅛🅘🅥🅔 💫 ★★•╯</b></i>

       ◆━━━━━━━━◉●•●◉━━━━━━━◆    
  <b><i>  🅾🆆🅽🅴🆁⇀</i></b> : 『 {Pbx_mention} 』
       ◆━━━━━━━━◉●•●◉━━━━━━━◆
    ┏━━━━━━━━━🧸━━━━━━━━┓
    ║➤ <b>» 𝐓ᴇʟᴇᴛʜᴏɴ•</b> <i>{telethon_version}</i>
    ║➤ <b>» 𝐏ʙxʙᴏᴛ•</b> <i>{Pbxbot_version}</i>
    ║➤ <b>» 𝐒ᴜᴅᴏ•</b> <i>{is_sudo}</i>
    ║➤ <b>» 𝐔ᴘᴛɪᴍᴇ•</b> <i>{uptime}</i>
    ║➤ <b>» 𝐏ɪɴɢ•</b> <i>{ping}</i>
    ║
    ║      ╔══════════════╗
    ║➤          <b><i>✬ <a href='https://t.me/ll_THE_BAD_BOT_ll'> 🇨🇦  𝗣𝗕𝗫  🌸 </a> ✬</i></b>
    ║      ╚══════════════╝
    ┗━━━━━━━━━🧸━━━━━━━━┛
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>𝐏ʙ𝐗ʙᴏᴛ ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@Pbx_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    Pbx = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await Pbx.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await Pbx.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@Pbx_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    userid, Pbx_user, Pbx_mention = await client_id(event, is_html=True)
    Pbx = await eor(event, "`Ruk Jra Sabar Karo 🫴🥺❤️‍🩹`")
    reply = await event.get_reply_message()
    uptime = await get_time((time.time() - StartTime))
    name = gvarstat("ALIVE_NAME") or Pbx_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/3daea7b5cc7501adcb001.jpg"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        Pbx_mention=Pbx_mention,
        telethon_version=telethon_version,
        Pbxbot_version=Pbxbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await Pbx.delete()


@Pbx_cmd(pattern="pbx$")
async def Pbx_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» 𝐏ʙ 𝐗 ʙᴏᴛ 𝐈s 𝐀ʟɪᴠᴇ ««</b>"
    try:
        Pbx = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await Pbx[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, telethon_version, Pbxbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the default Alive message."
).add_command(
    "pbx", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
  
