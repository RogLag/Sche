from code import interact
from distutils.log import error
from tkinter import HIDDEN
from types import coroutine
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import datetime
import asyncio
import ics_reader
from discord.message import Message
from unidecode import unidecode

from os import getenv
from dotenv import load_dotenv
from random import choice

from readWords import readWordsJSON
from Enums import RedLetters, YellowLetters, BlueLetters
from Classes.game import Game, games
from utils import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

version = "2.0"

words, dict_words_accents = readWordsJSON("public/words.json")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Etre esclave :'("))
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
    await interaction.channel.send(f"Emploi du temps du {dateofday.day}/{dateofday.month}/{dateofday.year} pour le groupe {group} :")
    await interaction.channel.send(file=discord.File('./calendar.png'))
    print(f"Aujourd'hui on est un {dateofday.weekday()}")
    while True:
        dateofday = datetime.datetime.now()
        if dateofday.hour == 00 and dateofday.minute >= 5 and dateofday.minute <= 10:
            if dateofday.weekday() != 5 and dateofday.weekday() != 6:
                if dateofday.weekday() == 0:
                    ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, "0", "1", "1")
                else:
                    ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, f"{group}", "1", "1")
                await interaction.channel.purge(limit=2)
                await interaction.channel.send(f"Emploi du temps du {dateofday.day}/{dateofday.month}/{dateofday.year} pour le groupe {group} :")
                await interaction.channel.send(file=discord.File('./calendar.png'))
                print(f"Message bien envoyé à {interaction.channel.name} le {dateofday.day}/{dateofday.month}/{dateofday.year} à {dateofday.hour}:{dateofday.minute}:{dateofday.second}")
            await asyncio.sleep(60*60*24)
        else:
            time_sleep = 60*60*(24-dateofday.hour)+60*(5-dateofday.minute)+00-dateofday.second
            print(f"Le premier message sera envoyé dans {time_sleep} secondes.")
            await asyncio.sleep(time_sleep)

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
@app_commands.choices(year=[
    Choice(name="2022", value="2022"),
    Choice(name="2023", value="2023")
])
async def timetable(interaction: discord.Interaction, day: str, month: str, year: str):
    await interaction.response.defer(ephemeral=True)
    get_role = interaction.user.roles
    get_name_roles = []
    for i in get_role:
        get_name_roles.append(i.name)
    if "Groupe: A" not in get_name_roles and "Groupe: B" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de classe, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Groupe: A":
                group = "A"
            elif i == "Groupe: B":
                group = "B"
    if "Anglais: 1" not in get_name_roles and "Anglais: 2" not in get_name_roles and "Anglais: 3" not in get_name_roles and "Anglais: 4" not in get_name_roles and "Anglais: 5" not in get_name_roles and "Anglais: 6" not in get_name_roles and "Anglais: 7" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe d'anglais, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Anglais: 1":
                english = "1"
            elif i == "Anglais: 2":
                english = "2"
            elif i == "Anglais: 3":
                english = "3"
            elif i == "Anglais: 4":
                english = "4"
            elif i == "Anglais: 5":
                english = "5"
            elif i == "Anglais: 6":
                english = "6"
            elif i == "Anglais: 7":
                english = "7"
    if "S.I.: 1" not in get_name_roles and "S.I.: 2" not in get_name_roles and "S.I.: 3" not in get_name_roles and "S.I.: 4" not in get_name_roles and "S.I.: 5" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de S.I., merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "S.I.: 1":
                si = "1"
            elif i == "S.I.: 2":
                si = "2"
            elif i == "S.I.: 3":
                si = "3"
            elif i == "S.I.: 4":
                si = "4"
            elif i == "S.I.: 5":
                si = "5"
    if int(month) == 2:
        if int(day) > 28:
            await interaction.followup.send("La date entrée n'est pas valide.", ephemeral=True)
            return
    if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30:
            await interaction.followup.send("La date entrée n'est pas valide.", ephemeral=True)
            return
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 31:
            await interaction.followup.send("La date entrée n'est pas valide.", ephemeral=True)
            return
    try:
        ics_reader.getTimetable(int(year), int(month), int(day), group, english, si)
        await interaction.followup.send(f"Emploi du temps du {day}/{month}/{year}, groupe {group}, anglais {english}, SI {si} :",file=discord.File('./calendar.png'), ephemeral=True)
    except ValueError:
        await interaction.followup.send("Wrong date", ephemeral=True)
    print(f"Message envoyée dans le channel {interaction.channel.name} à l'utilisateur {interaction.user.name} sur le serveur {interaction.guild.name} le {datetime.datetime.now()}")

class RoleButton(discord.ui.Button):
    def __init__(self, role: discord.Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        if self.role in interaction.user.roles:
            if self.role != discord.utils.get(interaction.guild.roles, name="Groupe: A") or self.role != discord.utils.get(interaction.guild.roles, name="Groupe: B"):
                await interaction.user.remove_roles(self.role)
                return
            else:
                await interaction.response.send_message("Vous avez déjà ce rôle.", ephemeral=True)
                return
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: A"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: B"))
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: B"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: A"))
        await interaction.user.add_roles(self.role)
        await interaction.followup.send(f"Le rôle {self.role.name} vous a bien été attribué.", ephemeral=True)
        return

class RoleButtonSI(discord.ui.Button):
    def __init__(self, role: discord.Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        for i in range(1, 6):
            if self.role != discord.utils.get(interaction.guild.roles, name=f"SI: {i}"):
                await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name=f"S.I.: {i}"))
        await interaction.user.add_roles(self.role)
        await interaction.followup.send(f"Vous avez été ajouté au groupe de S.I. n°{self.role.name[5:]} !", ephemeral=True)
        return

class RoleButtonEnglish(discord.ui.Button):
    def __init__(self, role: discord.Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        for i in range(1, 8):
            if self.role != discord.utils.get(interaction.guild.roles, name=f"Anglais: {i}"):
                await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name=f"Anglais: {i}"))
        await interaction.user.add_roles(self.role)
        await interaction.followup.send(f"Vous avez été ajouté au groupe d'anglais n°{self.role.name[9:]} !", ephemeral=True)
        return
        
@bot.tree.command(name="reactionrole", description="Create a message with a reaction role")
@app_commands.checks.has_permissions(manage_roles=True)
async def reactionrole(interaction: discord.Interaction, title: str, message: str, roles: str, channel_name: str):
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)
    if channel is None:
        await interaction.response.send_message("Le channel n'existe pas", ephemeral=True)
        return
    if len(roles.split(",")) > 5:
        await interaction.response.send_message("Il y a trop de rôles", ephemeral=True)
        return
    role_list = []
    for role in roles.split(","):
        role_list.append(discord.utils.get(interaction.guild.roles, name=role))
    view = discord.ui.View(timeout=None)
    for i in range(len(role_list)):
        if role_list[i].name == "Gaming" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label=role_list[i].name, style=discord.ButtonStyle.secondary, emoji="🎮", custom_id=role_list[i].name))
        elif role_list[i].name == "Groupe: A" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe A", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
        elif role_list[i].name == "Groupe: B" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe B", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
        else:
            view.add_item(RoleButton(role_list[i], label=role_list[i].name, style=discord.ButtonStyle.success, custom_id=role_list[i].name))
    for i in range(0,len(message.split("\\n"))):
        if i == 0:
            embed = discord.Embed(title=title, description=message.split("\\n")[i], color=0x351DE7)
        else:
            if message.split("\\n")[i] == message.split("\\n")[0]:
                embed.add_field(name=message.split("\\n")[0],value=message.split("\\n")[1], inline=False)
            elif message.split("\\n")[i] == message.split("\\n")[1]:
                pass
            elif message.split("\\n")[i] != "":
                embed.add_field(name="\u200b",value=message.split("\\n")[i], inline=False)
            else:
                embed.add_field(name="\u200b",value="\u200b", inline=False)
    await channel.send(embed=embed, view=view)
    await interaction.response.send_message("Le message a bien été envoyé", ephemeral=True)

@bot.tree.command(name="reactionenglishgroup", description="Create a message with a reaction role")
@app_commands.checks.has_permissions(manage_roles=True)
async def reactionenglishgroup(interaction: discord.Interaction, title: str, message: str, channel_name: str):
    groupes = [1, 2, 3, 4, 5, 6, 7]
    liste_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)
    if channel is None:
        await interaction.response.send_message("Le channel n'existe pas", ephemeral=True)
        return
    view = discord.ui.View(timeout=None)
    roles_groupes = []
    for i in range(len(groupes)):
        roles_groupes.append(discord.utils.get(interaction.guild.roles, name=f"Anglais: {groupes[i]}"))
    for i in range(len(roles_groupes)):
            view.add_item(RoleButtonEnglish(roles_groupes[i], emoji=liste_emoji[i], style=discord.ButtonStyle.secondary, custom_id=roles_groupes[i].name))
    for i in range(0,len(message.split("\\n"))):
        if i == 0:
            embed = discord.Embed(title=title, description=message.split("\\n")[i], color=0x351DE7)
        else:
            if message.split("\\n")[i] == message.split("\\n")[0]:
                embed.add_field(name=message.split("\\n")[0],value=message.split("\\n")[1], inline=False)
            elif message.split("\\n")[i] == message.split("\\n")[1]:
                pass
            elif message.split("\\n")[i] != "":
                embed.add_field(name="\u200b",value=message.split("\\n")[i], inline=False)
            else:
                embed.add_field(name="\u200b",value="\u200b", inline=False)
    await channel.send(embed=embed, view=view)
    await interaction.response.send_message("Le message a bien été envoyé", ephemeral=True)

@bot.tree.command(name="reactionsigroup", description="Create a message with a reaction role")
@app_commands.checks.has_permissions(manage_roles=True)
async def reactionenglishgroup(interaction: discord.Interaction, title: str, message: str, channel_name: str):
    groupes = [1, 2, 3, 4, 5]
    liste_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)
    if channel is None:
        await interaction.response.send_message("Le channel n'existe pas", ephemeral=True)
        return
    view = discord.ui.View(timeout=None)
    roles_groupes = []
    for i in range(len(groupes)):
        roles_groupes.append(discord.utils.get(interaction.guild.roles, name=f"S.I.: {groupes[i]}"))
    for i in range(len(roles_groupes)):
            view.add_item(RoleButtonSI(roles_groupes[i], emoji=liste_emoji[i], style=discord.ButtonStyle.secondary, custom_id=roles_groupes[i].name))
    for i in range(0,len(message.split("\\n"))):
        if i == 0:
            embed = discord.Embed(title=title, description=message.split("\\n")[i], color=0x351DE7)
        else:
            if message.split("\\n")[i] == message.split("\\n")[0]:
                embed.add_field(name=message.split("\\n")[0],value=message.split("\\n")[1], inline=False)
            elif message.split("\\n")[i] == message.split("\\n")[1]:
                pass
            elif message.split("\\n")[i] != "":
                embed.add_field(name="\u200b",value=message.split("\\n")[i], inline=False)
            else:
                embed.add_field(name="\u200b",value="\u200b", inline=False)
    await channel.send(embed=embed, view=view)
    await interaction.response.send_message("Le message a bien été envoyé", ephemeral=True)

@bot.tree.command(name="start_motus", description="Jouer au Motus")
@app_commands.choices(difficulty = [
    Choice(name="Facile", value="easy"),
    Choice(name="Moyen", value="medium"),
    Choice(name="Difficile", value="hard")
])
async def start_motus(interaction: discord.Interaction, difficulty: str = "medium"):
    await interaction.response.defer(ephemeral=True)
    if doesGameExist(games, interaction.channel.id):
        await interaction.followup.send("Il y a déjà un jeu en cours dans ce channel", ephemeral=True)
        return
    random_word = getRandomWordByDifficulty(words, difficulty)
    
    game = Game(interaction.channel.id, random_word)
    
    game.setRandomCorrectLetters(2)
    
    await interaction.channel.send("Démarrage de la partie. Mo Mo Motus !")
    await interaction.channel.send(f"Entrez un mot de {len(random_word)} lettres")
    await interaction.channel.send(game.correctLettersToString())

@bot.tree.command(name="stop_motus", description="Arrêter le jeu du Motus")
async def stop_motus(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    if not doesGameExist(games, interaction.channel.id):
        await interaction.followup.send("Il n'y a pas de jeu en cours dans ce channel", ephemeral=True)
        return
    game = games.get(interaction.channel.id)
    game.delete()
    await interaction.channel.send("Partie arrêtée")
    await interaction.followup.send("Le jeu a été arrêté")

@bot.event
async def on_message(message: Message):
    msg = unidecode(message.content).lower()

    # Pass message by bot
    if message.author == bot.user:
        return

    # Pass message if no active games in channel
    if not games.get(message.channel.id):
        return
    
    # If command slash
    if message.content.startswith("/"):
        return

    random_word = games.get(message.channel.id).word

    # Pass if the length of the word is not the same as the random_word
    if len(msg) != len(random_word):
        return

    if not msg in words:
        return await message.channel.send("Le mot que vous avez écrit n'est pas français.")


    game = games.get(message.channel.id)

    # Create a list with every valid letters
    list_letters = list(random_word)

    # [-, -, -, -, -, -]
    result = [BlueLetters.EMPTY for i in range(len(random_word))]

    # Set all correctly placed letters
    for i, letter in enumerate(msg):
        # If letter is correctly placed
        if letter == random_word[i]:
            # Remove letter from list
            index = list_letters.index(letter)
            list_letters.pop(index)

            # Replace - with valid letter

            letter_append = RedLetters[letter]

            game.correct[i] = letter_append
            result[i] = letter_append

        else:
            result[i] = BlueLetters[letter]

    # Set all letters not correctly placed
    for i, letter in enumerate(msg):
        # If letter is in the list of correct letters
        if letter in list_letters:
            # If letter is already placed continue
            if type(result[i]) != BlueLetters:
                continue

            # Remove letter from list
            index = list_letters.index(letter)
            list_letters.pop(index)

            # Replace - with incorrectly placed letter
            result[i] = YellowLetters[letter]
            
    historique = game.history
    historique.append(result)

    game.current += 1

    if len(historique) > 2:
        historique.pop(0)

    await message.channel.send(game.historyToString())

    if msg == game.word:
        game.delete()
        await message.channel.send(getRandomPhrase(message.author))
        await message.channel.send(findDefinitions(dict_words_accents.get(game.word)))
        return

    if game.current >= game.limit:
        await message.channel.send(f"Partie terminée ! Le mot était: {game.word}")
        game.delete()
    

@bot.tree.command(name="help", description="Affiche la liste des commandes")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Liste des commandes", description="Voici la liste des commandes", color=0x351DE7)
    embed.add_field(name="/help", value="Affiche la liste des commandes", inline=False)
    embed.add_field(name="/reactionrole", value="Crée un message avec un reaction role", inline=False)
    embed.add_field(name="/timetable", value="Affiche l'emploi du temps", inline=False)
    embed.add_field(name="/setup", value="Met l'emploi du temps d'un groupe tous les jours dans un channel (réservé aux administrateurs)", inline=False)
    
    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run('MTAyMzI2OTMzMzY2Njg4OTc5OA.GtSRmo.NECRXbsAVY7xsfcmmNU8DkARHI83Ah8QJ_wLyw')