import discord
import responses
from discord.ext import commands
import json


async def send_message(message, user_message, user_id, client,  is_private):
    try:
        response = responses.handle_response(user_message, user_id, client)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    with open("settings.json", 'r') as file:
        data = json.load(file)
    TOKEN = data["token"]
    if TOKEN == "token":
        exit("u need to add a token")

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('being a bot'))
        print(f'{client.user} ready')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author.id)
        user_message = str(message.content)

        if user_message[0] == "!":
            await send_message(message, user_message, username, client, is_private=False)

    client.run(TOKEN)
