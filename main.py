import discord
import dotenv
import os

dotenv.load_dotenv()

# Discord stuff
intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(discord_client)

# Pirate stuff 🔥
try:
    import arrr # pyright: ignore[reportMissingImports]
    PIRATE_AVAILABLE = True
    print("Pirate available!")
except ImportError:
    PIRATE_AVAILABLE = False
    print("Pirate unavailable... :(")

@discord_client.event
async def on_ready():
    await tree.sync()
    print(f'Logged in and ready!')

@tree.command(name='repeat', description='Repeat exactly what you typed')
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # Allow use in guilds
@discord.app_commands.allowed_installs(guilds=False, users=True) # But you can't install it TO a guild
async def repeat(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)

if PIRATE_AVAILABLE:
    @tree.command(name='piratize', description='Repeat arrrfter me')
    @discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # Allow use in guilds
    @discord.app_commands.allowed_installs(guilds=False, users=True) # But you can't install it TO a guild
    async def piratize(interaction: discord.Interaction, text: str):
        pirate = arrr.translate(text)
        await interaction.response.send_message(pirate)

discord_client.run(os.environ['DISCORD_BOT_TOKEN'])