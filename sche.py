import discord
from discord import app_commands
from discord.app_commands import Choice
import datetime
import ics_reader

##Options

version = "0.0.1"
token = "Token"

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
tree

##Commands

@tree.command(name='timetable', description="Show the timetable of the day.", guilds=[discord.Object(id=972500345815195700)])
@app_commands.checks.has_permissions(send_messages=True)
@app_commands.choices(month = [
    Choice(name='Janvier', value='1'),
    Choice(name='Fevrier', value='2'),
    Choice(name='Mars', value='3'),
    Choice(name='Avril', value='4'),
    Choice(name='Mai', value='5'),
    Choice(name='Juin', value='6'),
    Choice(name='Juillet', value='7'),
    Choice(name='Août', value='8'),
    Choice(name='Septembre', value='9'),
    Choice(name='Octobre', value='10'),
    Choice(name='Novembre', value='11'),
    Choice(name='Décembre', value='12'),
])
    
async def timetable(interaction: discord.Interaction, day: str, month: str, year: str, englishgroup: str, sigroup: str):
    if int(day) < 1 or int(day) > 31:
        await interaction.response.send_message("The day is not valid.", ephemeral=True)
    else:
        try:
            await ics_reader.getTimetable(year, month, day, englishgroup, sigroup)
            await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
        except ValueError:
            await interaction.response.send_message("Wrong date", ephemeral=True)

@tree.command(name="setup", description="Setup the bot for timetable of the day, every day.", guilds=[discord.Object(id=972500345815195700)])
@app_commands.checks.has_permissions(manage_guild=True)

async def setup(interaction: discord.Interaction):
    await interaction.response.send_message("Setup the bot for timetable of the day, every day.", ephemeral=True)
    dateofday = datetime.datetime.now()
    print(dateofday)


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

bot.run(f"{token}")
