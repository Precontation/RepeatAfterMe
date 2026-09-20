import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()

# Discord stuff
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Bot is logged in and ready!')

@bot.tree.command(name='repeat', description='Repeat exactly what you just typed')
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@discord.app_commands.allowed_installs(guilds=True, users=True)
async def on_message(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text);


bot.run(str(os.environ['DISCORD_BOT_TOKEN']))


