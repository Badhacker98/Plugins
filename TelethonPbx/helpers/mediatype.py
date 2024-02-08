from TelethonPbx.clients.logger import LOGGER as LOGS
from TelethonPbx.helpers.formats import yaml_format
from TelethonPbx.helpers.progress import humanbytes


async def mediadata(e_media):
    Pbx = ""
    if e_media.file.name:
        Pbx += f"📍 NAME :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        Pbx += f"📍 MIME TYPE :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        Pbx += f"📍 SIZE :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        Pbx += f"📍 DATE :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        Pbx += f"📍 ID :  {e_media.file.id}<br>"
    if e_media.file.ext:
        Pbx += f"📍 EXTENSION :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        Pbx += f"📍 EMOJI :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        Pbx += f"📍 TITLE :  {e_media.file.title}<br>"
    if e_media.file.performer:
        Pbx += f"📍 PERFORMER :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        Pbx += f"📍 DURATION :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        Pbx += f"📍 HEIGHT :  {e_media.file.height}<br>"
    if e_media.file.width:
        Pbx += f"📍 WIDTH :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        Pbx += f"📍 STICKER SET :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            Pbx += f"📍 Thumb  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return Pbx


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None
