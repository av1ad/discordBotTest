# Ideas for this bot
# Blackjack and economy for blackjack, gifs, crypto tracker, server info
# Force move all to one channel
# Gifs: slap, kiss, smack, cat, etc.


import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents explicitly
intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True
intents.guild_messages = True

# Create bot instance
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')
    await bot.change_presence(activity=discord.Streaming(name="Meow ^-^", url='https://www.twitch.tv/iraqs'))

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello ^-^ {ctx.author.name}! 😺')

if __name__ == "__main__":
    bot.run(TOKEN)