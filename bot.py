import discord
from discord.ext import commands
import os

from myserver import server_on

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True

# สร้างบอท
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await load_cogs()

@bot.event
async def on_message(message):
    await bot.process_commands(message)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded extension {filename}')
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

server_on()

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
