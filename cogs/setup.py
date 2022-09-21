import discord
from discord.ext import commands
from discord import app_commands
import datetime
import time

class setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setup", description="Setup the bot for timetable of the day, every day.", guilds=[discord.Object(id=972500345815195700)])
    @app_commands.checks.has_permissions(manage_guild=True)
    async def setup(self, interaction: discord.Interaction):
        dateofday = datetime.datetime.now()
        await interaction.response.send_message("Setup the bot for timetable of the day, every day.", ephemeral=True)
        await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
        while True:
            dateofday = datetime.datetime.now()
            if dateofday.hour == 19 and dateofday.minute >= 0 and dateofday.minute <= 5:
                await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
                time.sleep(60*60*24)
            else:
                time.sleep(60*60*(19-dateofday.hour)+60*(60-dateofday.minute)+60-dateofday.second)

def setup(bot):
    bot.add_cog(setup(bot), guilds=[discord.Object(id=972500345815195700)])