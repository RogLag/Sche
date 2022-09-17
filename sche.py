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

@tree.command(name='timetable', guild=discord.Object(id=1018837382633627658))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('test')
    
    
##Run Bot

bot.run("MTAyMDA0NzI1OTE1NDUzNDU2Mg.GbPWMW.JEq7sHkId4KolE7kZnFNU59dOTsWAJyQvDUC1U")