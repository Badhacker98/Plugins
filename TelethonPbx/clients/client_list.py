from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_peer_id
from TelethonPbx.clients.session import H2, H3, H4, H5, Pbx
from TelethonPbx.DB.gvar_sql import gvarstat


async def clients_list():
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await Pbx.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await H2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await H3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await H4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await H5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None, is_html=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        II_BAD_BBY_II = uid.users[0].id
        PBX_USER = uid.users[0].first_name
        _mention = f"[{PBX_USER}](tg://user?id={II_BAD_BBY_II})"
        _html = f"<a href='tg://user?id={II_BAD_BBY_II}'>{PBX_USER}</a>"
        Pbx_mention = _html if is_html else _mention
    else:
        client = await event.client.get_me()
        uid = get_peer_id(client)
        II_BAD_BBY_II = uid
        PBX_USER = client.first_name
        _mention = f"[{PBX_USER}](tg://user?id={II_BAD_BBY_II})"
        _html = f"<a href='tg://user?id={II_BAD_BBY_II}'>{PBX_USER}</a>"
        Pbx_mention = _html if is_html else _mention
    return II_BAD_BBY_II, PBX_USER, Pbx_mention


async def get_user_id(event, ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await event.client.get_entity(ids)).id
    return userid
