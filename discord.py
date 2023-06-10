import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTExNzEyNDA4NTU1MDQyODIyMA.GAQjmL.8pXZcqzFrY5Q8xL-iQ0-SteMmHTKh7ERXgp3uY')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
