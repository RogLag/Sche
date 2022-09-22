from types import coroutine
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import datetime
import asyncio
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
@app_commands.choices(group=[
    Choice(name="A", value="A"),
    Choice(name="B", value="B")
])
async def setup(interaction: discord.Interaction, group: str):
    dateofday = datetime.datetime.now()
    await interaction.response.send_message("Setup the bot for timetable of the day, every day.", ephemeral=True)
    if dateofday.weekday() == 0:
        ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, "0", "1", "1")
    else:
        ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, f"{group}", "1", "1")
    await interaction.channel.send(file=discord.File('./calendar.png'))
    print("ok1")
    while True:
        dateofday = datetime.datetime.now()
        """
        verification que le jour est un lundi
        """
        if dateofday.hour == 00 and dateofday.minute >= 5 and dateofday.minute <= 00:
            if dateofday.weekday() == 0:
                ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, "0", "1", "1")
            else:
                ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, f"{group}", "1", "1")
            await interaction.channel.send(file=discord.File('./calendar.png'))
            print(f"Message bien envoyé à {interaction.channel.name} le {dateofday.day}/{dateofday.month}/{dateofday.year} à {dateofday.hour}:{dateofday.minute}:{dateofday.second}")
            await asyncio.sleep(60*60*24)
        else:
            print(f"Le premier message sera envoyé dans {60*60*(24-dateofday.hour)+60*(5-dateofday.minute)+00-dateofday.second} secondes.")
            await asyncio.sleep(60*60*(24-dateofday.hour)+60*(5-dateofday.minute)+00-dateofday.second)

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
@app_commands.choices(group=[
    Choice(name="A", value="A"),
    Choice(name="B", value="B")
])
async def timetable(interaction: discord.Interaction, day: str, month: str, year: str, group: str, englishgroup: str, sigroup: str):
    if int(month) == 2:
        if int(day) > 28:
            await interaction.response.send_message("La date entrée n'est pas valide.", ephemeral=True)
            return
    if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30:
            await interaction.response.send_message("La date entrée n'est pas valide.", ephemeral=True)
            return
    print("ok3")
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 31:
            await interaction.response.send_message("La date entrée n'est pas valide.", ephemeral=True)
            return
    try:
        ics_reader.getTimetable(int(year), int(month), int(day), group, englishgroup, sigroup)
        await interaction.response.send_message(file=discord.File('./calendar.png'), ephemeral=True)
    except ValueError:
        await interaction.response.send_message("Wrong date", ephemeral=True)
    print(f"Message envoyée dans le channel {interaction.channel.name} à l'utilisateur {interaction.user.name} sur le serveur {interaction.guild.name} le {datetime.datetime.now()}")
    
    
    
bot.run('MTAyMDA0NzI1OTE1NDUzNDU2Mg.GT06sA.sKPN-GX59xa5c4AX3ocKtPSJsSDTB18LgHHbDg')