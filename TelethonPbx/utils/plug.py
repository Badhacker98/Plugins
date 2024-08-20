import importlib
import logging
import os
import sys
from pathlib import Path

from PbxConfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from TelethonPbx.clients.client_list import client_id
from TelethonPbx.clients.decs import Pbx_cmd
from TelethonPbx.clients.logger import LOGGER as LOGS
from TelethonPbx.clients.session import H2, H3, H4, H5, Pbx, PbxBot
from TelethonPbx.utils.cmds import CmdHelp
from TelethonPbx.utils.decorators import admin_cmd, command, sudo_cmd
from TelethonPbx.utils.extras import delete_Pbx, edit_or_reply
from TelethonPbx.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import TelethonPbx.utils

        path = Path(f"TelethonPbx/plugins/{shortname}.py")
        name = "TelethonPbx.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("PbxBot - Successfully imported " + shortname)
    else:
        import TelethonPbx.utils

        path = Path(f"TelethonPbx/plugins/{shortname}.py")
        name = "TelethonPbx.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Pbx
        mod.H1 = Pbx
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Pbx = Pbx
        mod.PbxBot = PbxBot
        mod.tbot = PbxBot
        mod.tgbot = Pbx.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Pbx
        mod.Pbxbot = Pbx
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_Pbx = delete_Pbx
        mod.eod = delete_Pbx
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.Pbx_cmd = Pbx_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = TelethonPbx
        sys.modules["userbot"] = TelethonPbx
        sys.modules["userbot.events"] = TelethonPbx
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["TelethonPbx.plugins." + shortname] = mod
        LOGS.info("🤡 ᴘʙxʙᴏᴛ ❤️ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Pbx.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"TelethonPbx.plugins.{shortname}"

            for i in reversed(range(len(Pbx._event_builders))):
                ev, cb = Pbx._event_builders[i]
                if cb.__module__ == name:
                    del Pbx._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("👻 ᴘʙxʙᴏᴛ 👻 - PLUGIN CHANNEL DETECTED.")
        LOGS.info("😈 ᴘʙxʙᴏᴛ 😈 - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"TelethonPbx/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "TelethonPbx/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# Pbxbot
