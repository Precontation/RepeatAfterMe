import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()

# Discord stuff
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# Pirate stuff 🔥
try:
    from arrr import translate # pyright: ignore[reportMissingImports]
    PIRATE_AVAILABLE = True
    print("Pirate available!")
except ImportError:
    PIRATE_AVAILABLE = False
    print("Pirate unavailable... :(")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in and ready!')

@bot.tree.command(name='repeat', description='Repeat exactly what you typed')
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # Allow use in guilds
@discord.app_commands.allowed_installs(guilds=False, users=True) # But you can't install it TO a guild
async def on_message(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)

if PIRATE_AVAILABLE:
    @bot.tree.command(name='repeat-as-a-pirate', description='idk why i made this')
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # Allow use in guilds
    @discord.app_commands.allowed_installs(guilds=False, users=True) # But you can't install it TO a guild
    async def on_message(interaction: discord.Interaction, text: str):
        pirate = translate(text)
        await interaction.response.send_message(pirate)

bot.run(os.environ['DISCORD_BOT_TOKEN'])


