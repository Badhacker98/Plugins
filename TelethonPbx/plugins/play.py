from telethon import TelegramClient, events
from TelethonPbx.plugins import *
from telethon.tl.functions.phone import JoinGroupCall, LeaveGroupCall
from telethon.tl.functions.messages import GetHistory
import asyncio

# Replace these with your own API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'

# Replace this with the target chat ID and voice chat ID

async def play_song(audio_file):
    await client(JoinGroupCall(chat_id, -1002056907061))
    await client.send_file(chat_id, audio_file, voice_note=True)
    await asyncio.sleep(10)

    # Leave the voice chat
    await client(LeaveGroupCall(chat_id))

async def skip_song():
    # Implement your logic to skip the current song
    pass

async def stop_music():
    # Implement your logic to stop the music playback
    pass

@Pbx_cmd(pattern="play(?:\s|$)([\s\S]*)")
async def on_play(event):
    audio_file = 'song.ogg'  # Replace with the actual audio file you want to play
    await play_song(audio_file)

@Pbx_cmd(pattern="skip(?:\s|$)([\s\S]*)")
async def on_skip(event):
    await skip_song()

@Pbx_cmd(pattern="stop(?:\s|$)([\s\S]*)")
async def on_stop(event):
    await stop_music()
