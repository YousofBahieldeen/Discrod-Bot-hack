import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTExNzEyNDA4NTU1MDQyODIyMA.GkVzMc.a3VrS3hc99fGiO8I8OOUwGXBlKiawXUs8BK-gA')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
