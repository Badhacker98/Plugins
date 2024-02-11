import glob
import os
import sys
from pathlib import Path

from PbxConfig import Config

from TelethonPbx.clients.logger import LOGGER as LOGS
from TelethonPbx.clients.session import H2, H3, H4, H5, Pbx, PbxBot
from TelethonPbx.utils.plug import load_module, plug_channel
from TelethonPbx.utils.startup import (join_it, logger_check, start_msg,
                                        update_sudo)
from TelethonPbx.version import __Pbxver__

# Global Variables #
PBX_PIC = "https://telegra.ph/file/c601d1866ea08f4532064.jpg"


# Client Starter
async def Pbxs(session=None, client=None, session_name="Main"):
    num = 0
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            num = 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
    return num


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as Pbx:
            path1 = Path(Pbx.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"TelethonPbx/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))


# Final checks after startup
async def Pbx_is_on(total):
    await update_sudo()
    await logger_check(Pbx)
    await start_msg(PbxBot, PBX_PIC, __Pbxver__, total)
    await join_it(Pbx)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# Pbxbot starter...
async def start_Pbxbot():
    try:
        tbot_id = await PbxBot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        Pbx.tgbot = PbxBot 
        LOGS.info("••• Starting PBxBot (TELETHON) •••")
        C1 = await Pbxs(Config.PBXBOT_SESSION, Pbx, "PBXBOT_SESSION")
        C2 = await Pbxs(Config.SESSION_2, H2, "SESSION_2")
        C3 = await Pbxs(Config.SESSION_3, H3, "SESSION_3")
        C4 = await Pbxs(Config.SESSION_4, H4, "SESSION_4")
        C5 = await Pbxs(Config.SESSION_5, H5, "SESSION_5")
        await PbxBot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• PBxBot Startup Completed •••")
        LOGS.info("••• Starting to load Plugins •••")
        await plug_load("TelethonPbx/plugins/*.py")
        await plug_channel(Pbx, Config.PLUGIN_CHANNEL)
        LOGS.info("👻 Your PBxBot Is Now Working 🤡")
        LOGS.info("Join @ll_THE_BAD_BOT_ll to get help regarding PBxBot.")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await Pbx_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


Pbx.loop.run_until_complete(start_Pbxbot())

if len(sys.argv) not in (1, 3, 4):
    Pbx.disconnect()
else:
    try:
        Pbx.run_until_disconnected()
    except ConnectionError:
        pass


# Pbxbot
