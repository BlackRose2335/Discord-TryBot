import os
import random
import discord
import asyncio
from dotenv import load_dotenv
from aiohttp import web

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/try'):
        response = random.choice(['Ano', 'Ne'])
        await message.channel.send(response)
    elif message.content.startswith('/roll'):
        roll = random.randint(1, 100)
        await message.channel.send(f'🎲 You rolled: {roll}')
    elif message.content.startswith('/coin'):
        coin = random.choice(['Heads', 'Tails'])
        await message.channel.send(f'🪙 Coin flip result: {coin}')

# Minimal web server so Render sees an open port
async def handle(request):
    return web.Response(text="TryBot is running!")

app = web.Application()
app.router.add_get('/', handle)

async def start_web_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    await site.start()
    print("Web server running on port 8000")

async def main():
    await start_web_server()
    await client.start(TOKEN)

asyncio.run(main())

# import discord
# from discord import app_commands
# import random
# import asyncio
# import os
# from dotenv import load_dotenv

# # Load token from .env
# load_dotenv()
# TOKEN = os.getenv("DISCORD_TOKEN")

# class MyClient(discord.Client):
#     def __init__(self):
#         super().__init__(intents=discord.Intents.default())
#         self.tree = app_commands.CommandTree(self)

#     async def setup_hook(self):
#         await self.tree.sync()

# client = MyClient()

# # /try command
# @client.tree.command(name="try", description="Randomly choose Ano or Ne")
# async def try_command(interaction: discord.Interaction):
#     weight_ano = random.uniform(0.3, 0.7)
#     weight_ne = 1 - weight_ano
#     choice = random.choices(["ANO", "NE"], weights=[weight_ano, weight_ne])[0]
#     await asyncio.sleep(random.uniform(0.3, 1.5))
#     await interaction.response.send_message(f"**{choice}**")

# # /roll command
# @client.tree.command(name="roll", description="Roll a number between 1 and 20")
# async def roll_command(interaction: discord.Interaction):
#     number = random.randint(1, 20)
#     await interaction.response.send_message(f"*{number}*")

# # /coin command
# @client.tree.command(name="coin", description="Flip a coin (Heads or Tails)")
# async def coin_command(interaction: discord.Interaction):
#     flip = random.choice(["Heads", "Tails"])
#     emoji = "🪙"
#     await interaction.response.send_message(f"{emoji}**{flip}**")

# # Run the bot
# client.run(TOKEN)

