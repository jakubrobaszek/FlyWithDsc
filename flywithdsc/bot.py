import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

prefix = '$'

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}hello'):
        await message.channel.send('hello!')