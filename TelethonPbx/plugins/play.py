from telethon import TelegramClient, events
from TelethonPbx.plugins import *
from telethon.tl.functions.phone import JoinGroupCall, LeaveGroupCall
from telethon.tl.functions.messages import GetHistory
import asyncio


api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'
async def play_song(audio_file):
    await client(JoinGroupCall(chat_id, -1002056907061))
    await client.send_file(chat_id, audio_file, voice_note=True)
   await asyncio.sleep(10)
   await client(LeaveGroupCall(chat_id))
async def skip_song():
      pass
async def stop_music():
       pass
@Pbx_cmd(pattern="play(?:\s|$)([\s\S]*)")
async def on_play(event):
    audio_file = 'song.ogg'  
    await play_song(audio_file)

@Pbx_cmd(pattern="skip(?:\s|$)([\s\S]*)")
async def on_skip(event):
    await skip_song()

@Pbx_cmd(pattern="stop(?:\s|$)([\s\S]*)")
async def on_stop(event):
    await stop_music()
    
