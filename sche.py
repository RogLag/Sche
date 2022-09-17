import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

##Connection Bot

class abot(discord.Client):
    
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1018837382633627658))
        self.synced = True
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        channel_connected = bot.get_channel(972811106580058132)
        embed=discord.Embed(title=f"{bot.user.name} is ready !", description=f"Up date: {dt_string},\n\nVersion: 0.1.1,\n{bot.user.name} by Rog#8698.", color=0x33DAFF)
        await channel_connected.send(embed=embed)
        print(f"{bot.user.name} is ready.")  
    
bot = abot()
tree = app_commands.CommandTree(bot)

##Commands

@tree.command(name='timetable.set', guild=discord.Object(id=1018837382633627658))
@app_commands.user_has_permissions(administrator=True)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('test')
    
##Error

@tree.error
async def error_handler(interaction: discord.Interaction, error: Exception):
    if isinstance(error, app_commands.CommandNotFound):
        await interaction.response.send_message(f"Command not found: {error.command_name}")
    elif isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(f"Missing permissions: {error.missing_permissions}")
    elif isinstance(error, app_commands.MissingRequiredArgument):
        await interaction.response.send_message(f"Missing required argument: {error.argument_name}")
    elif isinstance(error, app_commands.TooManyArguments):
        await interaction.response.send_message(f"Too many arguments: {error.argument_name}")
    elif isinstance(error, app_commands.ArgumentConversionFailure):
        await interaction.response.send_message(f"Argument conversion failure: {error.argument_name}")
    elif isinstance(error, app_commands.ArgumentParsingFailure):
        await interaction.response.send_message(f"Argument parsing failure: {error.argument_name}")
    elif isinstance(error, app_commands.CommandInvokeError):
        await interaction.response.send_message(f"Command invoke error: {error.original}")
    elif isinstance(error, app_commands.CommandError):
        await interaction.response.send_message(f"Command error: {error.original}")
    elif isinstance(error, app_commands.CommandRegistrationError):
        await interaction.response.send_message(f"Command registration error: {error.original}")
    elif isinstance(error, app_commands.CommandTreeError):
        await interaction.response.send_message(f"Command tree error: {error.original}")
    elif isinstance(error, app_commands.CommandTreeRegistrationError):
        await interaction.response.send_message(f"Command tree registration error: {error.original}")
    elif isinstance(error, app_commands.CommandTreeUnregistrationError):
        await interaction.response.send_message(f"Command tree unregistration error: {error.original}")
    elif isinstance(error, app_commands.CommandUnregistrationError):
        await interaction.response.send_message(f"Command unregistration error: {error.original}")
    elif isinstance(error, app_commands.BotMissingPermissions):
        await interaction.response.send_message(f"Bot missing permissions: {error.missing_permissions}")
    else:
        await interaction.response.send_message(f"Error: {error}")

##Run Bot

bot.run("MTAyMDA0NzI1OTE1NDUzNDU2Mg.GbPWMW.JEq7sHkId4KolE7kZnFNU59dOTsWAJyQvDUC1U")