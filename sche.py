import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import datetime
import time
import ics_reader

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

version = "0.0.1"

@bot.event
async def on_ready():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    channel_connected = bot.get_channel(972811106580058132)
    embed=discord.Embed(title=f"{bot.user.name} is ready !", description=f"Up date: {dt_string},\n\nVersion: {version},\n{bot.user.name} by Rog#8698.", color=0x33DAFF)
    await channel_connected.send(embed=embed)
    print(f"{bot.user.name} is ready.")  
    synced = await bot.tree.sync()
    print(f"Synced {synced} commands.")

@bot.tree.command(name="setup", description="Setup the bot for timetable of the day, every day.")
@app_commands.checks.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    dateofday = datetime.datetime.now()
    await interaction.response.send_message("Setup the bot for timetable of the day, every day.", ephemeral=True)
    await interaction.channel.send(file=discord.File('./calendar.png'))
    while True:
        dateofday = datetime.datetime.now()
        if dateofday.hour == 19 and dateofday.minute >= 0 and dateofday.minute <= 5:
            await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
            time.sleep(60*60*24)
        else:
            time.sleep(60*60*(19-dateofday.hour)+60*(60-dateofday.minute)+60-dateofday.second)

@bot.tree.command(name="timetable", description="Send the timetable of the day.")
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
            ics_reader.getTimetable(year, month, day, englishgroup, sigroup)
            await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
        except ValueError:
            await interaction.response.send_message("Wrong date", ephemeral=True)

bot.run('MTAyMDA0NzI1OTE1NDUzNDU2Mg.Gbbw4f.mYi-YmX0BsRxKyUJ6mfgO2YjZToduToXn0zkk8')