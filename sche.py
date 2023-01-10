from distutils.log import error
from types import coroutine
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import datetime
import asyncio
import ics_reader
import delestage

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

version = "2.0"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Ce bot est vraiment mauvais sur les bords"))
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    channel_connected = bot.get_channel(972811106580058132)
    embed=discord.Embed(title=f"{bot.user.name} is ready !", description=f"Up date: {dt_string},\n\nVersion: {version},\n{bot.user.name} by Rog#8698.", color=0xdf0000)
    await channel_connected.send(embed=embed)
    print(f"{bot.user.name} is ready.")  
    synced = await bot.tree.sync()
    print(f"Synced {synced} commands.")

@bot.tree.command(name="setup", description="Setup the bot for timetable of the day, every day.")
@app_commands.checks.has_permissions(manage_guild=True)
@app_commands.choices(group=[
    Choice(name="5A", value="5A"),
    Choice(name="5B", value="5B"),
    Choice(name="6A", value="6A"),
    Choice(name="6B", value="6B")
])
async def setup(interaction: discord.Interaction, group: str):
    dateofday = datetime.datetime.now()
    await interaction.response.send_message("Setup the bot for timetable of the day, every day.", ephemeral=True)
    if dateofday.weekday() == 0:
        ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, "0", "1", "1")
    else:
        ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, str(group), "1", "1")
    await interaction.channel.send(f"Emploi du temps du {dateofday.day}/{dateofday.month}/{dateofday.year} pour le groupe {group} :")
    await interaction.channel.send(file=discord.File(f'./calendar{group}.png'))
    print(f"Aujourd'hui on est un {dateofday.weekday()}")

    while True:
        dateofday = datetime.datetime.now()
        if dateofday.hour == 00 and dateofday.minute >= 5 and dateofday.minute <= 10:
            if dateofday.weekday() != 5 and dateofday.weekday() != 6:
                if dateofday.weekday() == 0:
                    ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, "0")
                else:
                    ics_reader.getTimetable(dateofday.year, dateofday.month, dateofday.day, str(group))
                await interaction.channel.purge(limit=2)
                await interaction.channel.send(f"Emploi du temps du {dateofday.day}/{dateofday.month}/{dateofday.year} pour le groupe {group} :")
                await interaction.channel.send(file=discord.File(f'./calendar{group}.png'))
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
        Choice(name='Décembre', value='12')
    ])
@app_commands.choices(year=[
    Choice(name="2023", value="2023")
])
async def timetable(interaction: discord.Interaction, day: str, month: str, year: str):
    await interaction.response.defer(ephemeral=True)
    get_role = interaction.user.roles
    get_name_roles = []
    for i in get_role:
        get_name_roles.append(i.name)
    if "Groupe: 5A" not in get_name_roles and "Groupe: 5B" not in get_name_roles  and "Groupe: 6A" not in get_name_roles  and "Groupe: 6B" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de classe, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Groupe: 5A":
                group = "5A"
            elif i == "Groupe: 5B":
                group = "5B"
            elif i == "Groupe: 6A":
                group = "6A"
            elif i == "Groupe: 6B":
                group = "6B"
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
    if "Projet: DAE" not in get_name_roles and "Projet: DEE" not in get_name_roles and "Projet: DI" not in get_name_roles and "Projet: DMS" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de Projet, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Projet: DAE":
                si = "DAE"
            elif i == "Projet: DEE":
                si = "DEE"
            elif i == "Projet: DI":
                si = "DI"
            elif i == "Projet: DMS":
                si = "DMS"
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
        await interaction.followup.send(f"Emploi du temps du {day}/{month}/{year}, groupe {group}, anglais {english}, SI {si} :",file=discord.File(f'./calendar{group}.png'), ephemeral=True)
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
            if self.role != discord.utils.get(interaction.guild.roles, name="Groupe: 5A") or self.role != discord.utils.get(interaction.guild.roles, name="Groupe: 5B") or self.role != discord.utils.get(interaction.guild.roles, name="Groupe: 6A") or self.role != discord.utils.get(interaction.guild.roles, name="Groupe: 6B"):
                await interaction.user.remove_roles(self.role)
                return
            else:
                await interaction.response.send_message("Vous avez déjà ce rôle.", ephemeral=True)
                return
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: 5A"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5B"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6A"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6B"))
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: 5B"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5A"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6A"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6B"))
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: 6A"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5A"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5B"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6B"))
        if self.role == discord.utils.get(interaction.guild.roles, name="Groupe: 6B"):
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5A"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 5B"))
            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name="Groupe: 6A"))
        await interaction.user.add_roles(self.role)
        await interaction.followup.send(f"Le rôle {self.role.name} vous a bien été attribué.", ephemeral=True)
        return

class RoleButtonProjet(discord.ui.Button):
    def __init__(self, role: discord.Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role

    async def callback(self, interaction: discord.Interaction):
        nom_role = ["DAE","DEE","DI","DMS"]
        await interaction.response.defer(ephemeral=True)
        for i in range(0, 4):
            if self.role != discord.utils.get(interaction.guild.roles, name=f"Projet: {nom_role[i]}"):
                await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, name=f"Projet: {nom_role[i]}"))
        await interaction.user.add_roles(self.role)
        await interaction.followup.send(f"Vous avez été ajouté au groupe de Projet du batiment {self.role.name[8:]} !", ephemeral=True)
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
    
@bot.tree.command(name="setup_reaction", description="Setup des réactions pour les rôles")
@app_commands.checks.has_permissions(manage_roles=True)
async def setup_reaction(interaction: discord.Interaction, channel_name: str):
    await interaction.response.defer()
    if discord.utils.get(interaction.guild.channels, name=channel_name) is None:
        await interaction.followup.send("Le channel roles n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Groupe: 5A") is None:
        await interaction.followup.send("Le rôle Groupe: 5A n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Groupe: 5B") is None:
        await interaction.followup.send("Le rôle Groupe: 5B n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Groupe: 6A") is None:
        await interaction.followup.send("Le rôle Groupe: 6A n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Groupe: 6B") is None:
        await interaction.followup.send("Le rôle Groupe: 6B n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 1") is None:
        await interaction.followup.send("Le rôle Anglais: 1 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 2") is None:
        await interaction.followup.send("Le rôle Anglais: 2 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 3") is None:
        await interaction.followup.send("Le rôle Anglais: 3 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 4") is None:
        await interaction.followup.send("Le rôle Anglais: 4 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 5") is None:
        await interaction.followup.send("Le rôle Anglais: 5 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 6") is None:
        await interaction.followup.send("Le rôle Anglais: 6 n'existe pas.", ephemeral=True)
        return
    if discord.utils.get(interaction.guild.roles, name="Anglais: 7") is None:
        await interaction.followup.send("Le rôle Anglais: 7 n'existe pas.", ephemeral=True)
        return
    """Creation du premier reaction role:"""
    roles="Groupe: 5A,Groupe: 5B,Groupe: 6A,Groupe: 6B,Gaming"
    title="**__Reaction Role :__**"
    message="Veuillez sélectionner tout d'abord votre groupe de classe (<@&1022559746722631722>, <@&1022559875483570387>, <@&1060863856131440692> ou <@&1060864001396973568>) !\\nline\\nDe plus, le rôle <@&1020026863399223347> est disponible et permet d'accéder à différents salons dédiés aux jeux vidéos !\\n<@&1019163845413052488>"
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
        elif role_list[i].name == "Groupe: 5A" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe 5A", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
        elif role_list[i].name == "Groupe: 5B" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe 5B", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
        elif role_list[i].name == "Groupe: 6A" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe 6A", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
        elif role_list[i].name == "Groupe: 6B" and interaction.guild.name == "PEIP 9":
            view.add_item(RoleButton(role_list[i], label="Groupe 6B", style=discord.ButtonStyle.success, custom_id=role_list[i].name))
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
    """Creation du deuxieme reaction role:"""
    title="**__Reaction Role :__**"
    message="Veuillez, ensuite, selectionner votre groupe de S.I. !"
    groupes = ["DAE", "DEE", "DI", "DMS"]
    liste_emoji = ["DAE", "DEE", "DI", "DMS"]
    channel = discord.utils.get(interaction.guild.channels, name=channel_name)
    if channel is None:
        await interaction.response.send_message("Le channel n'existe pas", ephemeral=True)
        return
    view = discord.ui.View(timeout=None)
    roles_groupes = []
    for i in range(len(groupes)):
        roles_groupes.append(discord.utils.get(interaction.guild.roles, name=f"Projet: {groupes[i]}"))
    for i in range(len(roles_groupes)):
            view.add_item(RoleButtonProjet(roles_groupes[i], label=liste_emoji[i], style=discord.ButtonStyle.secondary, custom_id=roles_groupes[i].name))
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
    """Creation du troisieme reaction role:"""
    title="**__Reaction Role :__**"
    message="Enfin, selectionner votre groupe d'anglais !"
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
    await interaction.followup.send("Les réactions-roles ont été setup !")

@bot.tree.command(name="help", description="Affiche la liste des commandes")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Liste des commandes", description="Voici la liste des commandes", color=0x351DE7)
    embed.add_field(name="/help", value="Affiche la liste des commandes", inline=False)
    embed.add_field(name="/reactionrole", value="Crée un message avec un reaction role", inline=False)
    embed.add_field(name="/timetable", value="Affiche l'emploi du temps", inline=False)
    embed.add_field(name="/setup", value="Met l'emploi du temps d'un groupe tous les jours dans un channel (réservé aux administrateurs)", inline=False)
    
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name="today", description="Affiche l'emploi du temps du jour")
async def today(interaction: discord.Interaction):
    date = datetime.datetime.now()
    await interaction.response.defer(ephemeral=True)
    get_role = interaction.user.roles
    get_name_roles = []
    for i in get_role:
        get_name_roles.append(i.name)
    if "Groupe: 5A" not in get_name_roles and "Groupe: 5B" not in get_name_roles and "Groupe: 6A" not in get_name_roles and "Groupe: 6B" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de classe, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Groupe: 5A":
                group = "5A"
            elif i == "Groupe: 5B":
                group = "5B"
            elif i == "Groupe: 6A":
                group = "6A"
            elif i == "Groupe: 6B":
                group = "6B"
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
    if "Projet: DAE" not in get_name_roles and "Projet: DEE" not in get_name_roles and "Projet: DI" not in get_name_roles and "Projet: DMS" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de Projet, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Projet: DAE":
                si = "DAE"
            elif i == "Projet: DEE":
                si = "DEE"
            elif i == "Projet: DI":
                si = "DI"
            elif i == "Projet: DMS":
                si = "DMS"
    try:
        ics_reader.getTimetable(int(date.year), int(date.month), int(date.day), group, english, si)
        await interaction.followup.send(f"Emploi du temps du {str(date.day)}/{str(date.month)}/{str(date.year)}, groupe {group}, anglais {english}, projet {si} :",file=discord.File(f'./calendar{group}.png'), ephemeral=True)
    except Exception as e:
        await interaction.followup.send("Erreur: " + str(e))

@bot.tree.command(name="tomorrow", description="Affiche l'emploi du temps du lendemain")
async def tomorrow(interaction: discord.Interaction):
    date = datetime.datetime.now() + datetime.timedelta(days=1)
    await interaction.response.defer(ephemeral=True)
    get_role = interaction.user.roles
    get_name_roles = []
    for i in get_role:
        get_name_roles.append(i.name)
    if "Groupe: 5A" not in get_name_roles and "Groupe: 5B" not in get_name_roles and "Groupe: 6A" not in get_name_roles and "Groupe: 6B" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de classe, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Groupe: 5A":
                group = "5A"
            elif i == "Groupe: 5B":
                group = "5B"
            elif i == "Groupe: 6A":
                group = "6A"
            elif i == "Groupe: 6B":
                group = "6B"
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
    if "Projet: DAE" not in get_name_roles and "Projet: DEE" not in get_name_roles and "Projet: DI" not in get_name_roles and "Projet: DMS" not in get_name_roles:
        await interaction.followup.send("Vous n'avez pas de groupe de Projet, merci de le selectionner dans ce channel: <#1019985812269572126> !")
        return
    else:
        for i in get_name_roles:
            if i == "Projet: DAE":
                si = "DAE"
            elif i == "Projet: DEE":
                si = "DEE"
            elif i == "Projet: DI":
                si = "DI"
            elif i == "Projet: DMS":
                si = "DMS"
    try:
        ics_reader.getTimetable(int(date.year), int(date.month), int(date.day), group, english, si)
        await interaction.followup.send(f"Emploi du temps du {str(date.day)}/{str(date.month)}/{str(date.year)}, groupe {group}, anglais {english}, projet {si} :",file=discord.File(f'./calendar{group}.png'), ephemeral=True)
    except Exception as e:
        await interaction.followup.send("Erreur: " + str(e))

@bot.tree.command(name="delestage_setup", description="Affiche tous les jours à 19h et à 7h si les batiments seront ouverts ou non")
async def delestage_setup(interaction: discord.Interaction):
    dateofday = datetime.datetime.now()
    channel_connected = bot.get_channel(1061688892429967461)
    await interaction.response.send_message("Setup the bot for 'delestage', every day.", ephemeral=True)
    while True:
        dateofday = datetime.datetime.now()
        if dateofday.hour == 19 and dateofday.minute >= 1 and dateofday.minute <= 5 and dateofday.weekday() != 4 and dateofday.weekday() != 5:
            list_open_or_not = delestage.openornot()
            await interaction.channel.purge(limit=len(list_open_or_not)+1)
            await interaction.channel.send("Mes informations proviennent du site : https://www.univ-tours.fr/delestage-1, je les mets à jour à 7h et à 20h tous les jours sauf le week-end. Merci de vérifier sur le site par vous même.")
            for i in list_open_or_not:
                if "ouvert" in i:
                    await interaction.channel.send(i+"      :white_check_mark:")
                else:
                    await interaction.channel.send(i+"      :x:")
            print(f"Message bien envoyé à {interaction.channel.name} le {dateofday.day}/{dateofday.month}/{dateofday.year} à {dateofday.hour}:{dateofday.minute}:{dateofday.second}")
            print(f"Prochain message dans 11h.")
            await channel_connected.send(f"Delestage: Le prochain message sera envoyé dans 11h.")
            await asyncio.sleep(60*60*11)
        elif dateofday.hour == 6 and dateofday.minute >= 1 and dateofday.minute <= 5 and dateofday.weekday() != 5 and dateofday.weekday() != 6:
            list_open_or_not = delestage.openornot()
            await interaction.channel.purge(limit=len(list_open_or_not)+1)
            await interaction.channel.send("Mes informations proviennent du site : https://www.univ-tours.fr/delestage-1, je les mets à jour à 7h et à 20h tous les jours sauf le week-end. Merci de vérifier sur le site par vous même.")
            for i in list_open_or_not:
                if "ouvert" in i:
                    await interaction.channel.send(i+"      :white_check_mark:")
                else:
                    await interaction.channel.send(i+"      :x:")
            print(f"Message bien envoyé à {interaction.channel.name} le {dateofday.day}/{dateofday.month}/{dateofday.year} à {dateofday.hour}:{dateofday.minute}:{dateofday.second}")
            print(f"Prochain message dans 13h.")
            await channel_connected.send(f"Delestage: Le prochain message sera envoyé dans 13h.")
            await asyncio.sleep(60*60*13)
        else:
            time_sleep = 60*60*(19-dateofday.hour)+60*(1-dateofday.minute)+0-dateofday.second
            print(f"Le premier message sera envoyé dans {time_sleep} secondes.")
            await channel_connected.send(f"Delestage: Le premier message sera envoyé dans {time_sleep} secondes.")
            await asyncio.sleep(time_sleep)

bot.run('Token')