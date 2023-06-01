import discord 
from discord.ext import commands 


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("BOT IS UP AND RUNNING")
    print("---------------------")

@client.command()
async def hi(ctx):
    await ctx.send("Hey. How are you?")

@client.command()
async def khsft(ctx):
    await ctx.send("Hey Khsft. What's your name again?")

@client.command()
async def coding_progress(ctx):
    await ctx.send("I currently know HTML, some CSS, and Some Python. This bot was made using Python! To see all my projects and work, you can check it out on Gituhb using !github_page.")    

@client.command()
async def github_page(ctx):
    await ctx.send("https://github.com/AverageMonkey")

client.run("MTExMzkyMDI4MTUxODU1OTMxMw.GhwhCo.NbHNSFIgS5sHuRmCtz-vrvRcuTCpeHhqETGGck")