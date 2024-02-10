from PbxConfig import Config, db_config, os_config
from TelethonPbx import HEROKU_APP, StartTime
from TelethonPbx.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from TelethonPbx.clients.decs import Pbx_cmd, Pbx_handler
from TelethonPbx.clients.instaAPI import InstaGram
from TelethonPbx.clients.logger import LOGGER
from TelethonPbx.clients.session import (H2, H3, H4, H5, Pbx, PbxBot,
                                          validate_session)
from TelethonPbx.DB import gvar_sql
from TelethonPbx.helpers.anime import *
from TelethonPbx.helpers.classes import *
from TelethonPbx.helpers.convert import *
from TelethonPbx.helpers.exceptions import *
from TelethonPbx.helpers.formats import *
from TelethonPbx.helpers.gdriver import *
from TelethonPbx.helpers.google import *
from TelethonPbx.helpers.ig_helper import *
from TelethonPbx.helpers.image import *
from TelethonPbx.helpers.int_str import *
from TelethonPbx.helpers.mediatype import *
from TelethonPbx.helpers.mmf import *
from TelethonPbx.helpers.movies import *
from TelethonPbx.helpers.pasters import *
from TelethonPbx.helpers.pranks import *
from TelethonPbx.helpers.progress import *
from TelethonPbx.helpers.runner import *
from TelethonPbx.helpers.tools import *
from TelethonPbx.helpers.tweets import *
from TelethonPbx.helpers.users import *
from TelethonPbx.helpers.vids import *
from TelethonPbx.helpers.yt_helper import *
from TelethonPbx.strings import *
from TelethonPbx.utils.cmds import *
from TelethonPbx.utils.decorators import *
from TelethonPbx.utils.errors import *
from TelethonPbx.utils.extras import *
from TelethonPbx.utils.funcs import *
from TelethonPbx.utils.globals import *
from TelethonPbx.utils.plug import *
from TelethonPbx.utils.startup import *
from TelethonPbx.version import __Pbxver__, __telever__

cjb = "./PbxConfig/resources/pics/cjb.jpg"
Pbx_logo = "./PbxConfig/resources/pics/Pbxbot_logo.jpg"
restlo = "./PbxConfig/resources/pics/rest.jpeg"
shhh = "./PbxConfig/resources/pics/chup_madarchod.jpeg"
shuru = "./PbxConfig/resources/pics/shuru.jpg"
spotify_logo = "./PbxConfig/resources/pics/spotify.jpg"


Pbx_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
Pbxbot_version = __Pbxver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "ll_THE_BAD_BOT_ll"
my_group = Config.MY_GROUP or "ll_THE_BAD_BOT_ll"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/ll_THE_BAD_BOT_ll"
grp_link = "https://t.me/THE_DRAMA_CLUB_01"
Pbx_channel = f"[ᴛʜᴇ ᴘʙx ʙᴏᴛ]({chnl_link})"
Pbx_grp = f"[ᴘʙx ʙᴏᴛ ɢʀᴏᴜᴘ]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""

# TelethonPbx
