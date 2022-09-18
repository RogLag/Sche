from optparse import Option
import discord
from discord import app_commands
import datetime

version = "0.0.1"

##Connection Bot

class abot(discord.Client):
    
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=972500345815195700))
        self.synced = True
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        channel_connected = bot.get_channel(972811106580058132)
        embed=discord.Embed(title=f"{bot.user.name} is ready !", description=f"Up date: {dt_string},\n\nVersion: {version},\n{bot.user.name} by Rog#8698.", color=0x33DAFF)
        await channel_connected.send(embed=embed)
        print(f"{bot.user.name} is ready.")  
    
bot = abot()
tree = app_commands.CommandTree(bot)

##Commands

@tree.command(name='timetable', description="Show the timetable of the day.", guilds=[discord.Object(id=972500345815195700),discord.Object(id=1018837382633627658)])
@app_commands.checks.has_permissions(manage_guild=True)
async def self(interaction: discord.Interaction, date: str):
    try:
        date = datetime.datetime.strptime(date, format)
        await interaction.response.send_message(file=discord.File('image.jpg'), ephemeral=True)
    except ValueError:
        await interaction.response.send_message("Wrong date", ephemeral=True)
   
    
##Error

@tree.error
async def error_handler(interaction: discord.Interaction, error: Exception):
    if isinstance(error, app_commands.CommandNotFound):
        await interaction.response.send_message(f"Command not found.", ephemeral=True)
    elif isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(f"Missing permissions: {error.missing_permissions}", ephemeral=True)
    elif isinstance(error, app_commands.CommandInvokeError):
        channel_connected = bot.get_channel(1020707241243967538)
        embed=discord.Embed(title=f"{bot.user.name} get an error !", description=f"Command invoke error for __/{interaction.command.name}__:,\n{error.original},\n\nin {interaction.guild.name}", color=0xED4245)
        await channel_connected.send(embed=embed)
        await interaction.response.send_message(f"Command invoke error: {error.original}", ephemeral=True)
    elif isinstance(error, app_commands.BotMissingPermissions):
        await interaction.response.send_message(f"Bot missing permissions: {error.missing_permissions}", ephemeral=True)
    elif isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(f"Command on cooldown: {error.retry_after}", ephemeral=True)
    else:
        await interaction.response.send_message(f"Error: {error}")

##Run Bot

bot.run("MTAyMDA0NzI1OTE1NDUzNDU2Mg.G_N71s.NOw6N5SjU7KrDzKpWqSfv8Hgoie4Acxsj8g1Gg")
