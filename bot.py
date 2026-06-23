import os
import discord

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

VOICE_CHANNEL_ID = 1513342594929786923

@client.event
async def on_ready():
    print(f"Conectado como {client.user}")

    canal = client.get_channel(VOICE_CHANNEL_ID)

    if canal:
        await canal.connect()
        print("Conectado al canal de voz")
    else:
        print("No encontré el canal")

client.run(TOKEN)