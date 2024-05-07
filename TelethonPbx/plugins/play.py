import yt_dlp
from TelethonPbx.clients.logger import logging
from TelethonPbx.plugins import *

async def play_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['formats'][0]['url']
        await group_call.input_stream(audio_url)

@Pbx_cmd(pattern="play(?:\s|$)([\s\S]*)")
async def play(event):
    url = event.pattern_match.group(1)
    await play_youtube_audio(url)
    await event.respond('Playing YouTube audio...')
