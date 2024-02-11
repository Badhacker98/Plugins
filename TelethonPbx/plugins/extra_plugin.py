import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument
from TelethonPbx.plugins import *


@Pbx_cmd(pattern="extdl$")
async def install(event):
    chat = Config.PLUGIN_CHANNEL
    if chat == 0:
        return await parse_error(event, f"PLUGIN_CHANNEL not configured.")
    documentss = await event.client.get_messages(
        chat, None, filter=InputMessagesFilterDocument
    )
    total = int(documentss.total)
    total_doxx = range(0, total)
    Pbx_ = await eor(event, "__Installing plugins from Plugin Channel...__")
    Pbx = "**⦁ Installed Plugins:**\n\n"
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await event.client.get_messages(chat, ids=mxo), "TelethonPbx/plugins/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            Pbx += "__» Installed Plugin__ `{}`\n".format(
                os.path.basename(downloaded_file_name)
            )
        else:
            Pbx += "__» Failed to Install__ `{}`\n".format(
                os.path.basename(downloaded_file_name)
            )
    await Pbx_.edit(Pbx)


@Pbx_cmd(pattern="installall ([\s\S]*)")
async def install(event):
    chat = event.pattern_match.group(1)
    Pbx_ = await eor(event, f"**Starting To Install Plugins From {chat} !!**")
    Pbx = f"**⦁ Installed Plugins From {chat} :**\n\n"
    documentss = await event.client.get_messages(
        chat, None, filter=InputMessagesFilterDocument
    )
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await event.client.get_messages(chat, ids=mxo), "TelethonPbx/plugins/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            Pbx += "__» Installed Plugin__ `{}`\n".format(
                os.path.basename(downloaded_file_name)
            )
        else:
            Pbx += "__» Failed to Install__ `{}`\n".format(
                os.path.basename(downloaded_file_name)
            )
    await Pbx_.edit(Pbx)


CmdHelp("extra_plugin").add_command(
    "extdl", None, "Installs all plugins from the channal which id is in PLUGIN_CHANNEL Config"
).add_command(
    "installall", "Installs all the plugins in provided channel / group. (May get floodwait error)"
).add_info(
    "Extra Plugins."
).add_warning(
    "Don't Install plugins from Unknown channel."
).add()
