# Ideas for this bot
# Blackjack and economy for blackjack, gifs, crypto tracker, server info
# Force move all to one channel
# Gifs: slap, kiss, smack, cat, etc.


import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import shuffle

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True
intents.guild_messages = True

GUILD_ID = discord.Object(651263305796681748)

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())
        
    async def setup_hook(self):
        await self.tree.sync(guild=GUILD_ID)
        
    async def on_ready(self):
        print(f'{self.user} is now online!')
        await self.change_presence(activity=discord.Streaming(name="Meow ^-^", url='https://www.twitch.tv/iraqs'))


bot = Client()

@bot.tree.command(name='hello',description="hai", guild=GUILD_ID)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hallooooo :3 {interaction.user.name}! 😺')
    
@bot.tree.command(name="meow", description="meow",guild=GUILD_ID)
async def meow(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"<@{interaction.user.id}> meowed at <@{user.id}> ^-^")
    
@bot.tree.command(name="avatar", description="gets a user's avatar", guild=GUILD_ID)
async def avatar(interaction: discord.Interaction, user: discord.User):
    embed = discord.Embed(description=f"{user.mention}'s avatar", color=0xBA55D3)
    embed.set_thumbnail(url=user.display_avatar)
    await interaction.response.send_message(embed=embed)
    
if __name__ == "__main__":
    bot.run(TOKEN)