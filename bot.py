import discord
import responses
from discord.ext import commands

TOKEN = ""

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = ""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        file = discord.File("D:\DE-Discord\grappa.png", filename="grappa.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://grappa.png")
        if message.content.startswith('grappa'):
            channel = message.channel
            await channel.send(f'for you {username}',file=file, embed=embed)
        if message.author == client.user:
            return

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
