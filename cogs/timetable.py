import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import ics_reader

class TimeTable(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("TimeTable cog is ready.")
    
    @commands.commands()
    async def sync(self, ctx) -> None:
        fat = await ctx.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f"Synced {len(fat)} commands.")

    @app_commands.command(name='timetable', description="Show the timetable of the day.", guilds=[discord.Object(id=972500345815195700)])
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
    async def timetable(self, interaction: discord.Interaction, day: str, month: str, year: str, englishgroup: str, sigroup: str):
        if int(day) < 1 or int(day) > 31:
            await interaction.response.send_message("The day is not valid.", ephemeral=True)
        else:
            try:
                await ics_reader.getTimetable(year, month, day, englishgroup, sigroup)
                await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
            except ValueError:
                await interaction.response.send_message("Wrong date", ephemeral=True)
    
    async def setup(bot):
        await bot.add_cog(TimeTable(bot), guilds=[discord.Object(id=972500345815195700)])