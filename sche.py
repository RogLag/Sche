from optparse import Option
import discord
from discord import app_commands
from discord.app_commands import Choice
import datetime
import configparser

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

@tree.command(name='timetable', description="Show the timetable of the day.", guilds=[discord.Object(id=972500345815195700)])
@app_commands.checks.has_permissions(manage_guild=True)
@app_commands.choices(month = [
    Choice(name='1', value='1'),
    Choice(name='2', value='2'),
    Choice(name='3', value='3'),
    Choice(name='4', value='4'),
    Choice(name='5', value='5'),
    Choice(name='6', value='6'),
    Choice(name='7', value='7'),
    Choice(name='8', value='8'),
    Choice(name='9', value='9'),
    Choice(name='10', value='10'),
    Choice(name='11', value='11'),
    Choice(name='12', value='12'),
])
    
async def self(interaction: discord.Interaction, day: str, month: str):
    if int(day) < 1 or int(day) > 31:
        await interaction.response.send_message("The day is not valid.", ephemeral=True)
    else:
        try:
            date = ""
            date += f"2022-{month}-{day}"
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
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

bot.run("MTAyMDA0NzI1OTE1NDUzNDU2Mg.GfyNkM.pAc7Pn63lSeQA4ts0f6VnNEyFbyD1RGElJPuuc")
