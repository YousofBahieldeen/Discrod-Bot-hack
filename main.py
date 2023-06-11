import discord
import random
import math

TOKEN = 'MTExNzEyNDA4NTU1MDQyODIyMA.GHEW9p.UwZzQ1prtRckPtbLaqPx59-sEwsaQKs1kCYX6w'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        if user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        if user_message.lower() == 'roll a number':
            random_number = f'Here is your random number: {random.randrange(100000000000)}'
            await message.channel.send(random_number)
            return
    if user_message.lower() == '/say hello':
        await message.channel.send(f'Hello!')
        return
    if user_message.lower() == '/get ip':
        await message.channel.send(f'Sorry! I am not programed to do that yet')
        return


client.run(TOKEN)
