from TelethonPbx.clients.logger import logging
from TelethonPbx.plugins import *
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.phone import (CreateGroupCallRequest,
                                         DiscardGroupCallRequest,
                                         GetGroupCallRequest,
                                         InviteToGroupCallRequest)

import asyncio

# Replace these with your own API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'

# Replace this with the target chat ID and voice chat ID
chat_id = 100123456789  # Replace with the actual chat ID
voice_chat_id = 'your_voice_chat_id'  # Replace with the actual voice chat ID

async def play_song(audio_file):
    
    # Wait for a few seconds before leaving the voice chat
    await asyncio.sleep(10)

    # Leave the voice chat
    await asyncio(LeaveGroupCall(chat_id))

async def skip_song():
    # Implement your logic to skip the current song
    pass

async def stop_music():
    # Implement your logic to stop the music playback
    pass

@Pbx_cmd(pattern="play(?:\s|$)([\s\S]*)")

async def on_play(event):
    audio_file = 'song.ogg'  # Replace with the actual audio file you want to play
    await play_song(audio_file)

@Pbx_cmd(pattern="skip(?:\s|$)([\s\S]*)")

async def on_skip(event):
    await skip_song()

@Pbx_cmd(pattern="stop(?:\s|$)([\s\S]*)")

async def on_stop(event):
    await stop_music()
