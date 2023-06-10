import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTExNzEyNDA4NTU1MDQyODIyMA.Gvg3JH.6SP_nwCVx1wPT8SNZV-LUPxmdv5LNhYgDjZ-gs')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
