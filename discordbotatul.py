import discord 
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_reday():
    print("bot is ready")

@client.command()
async def pro(ctx):
    await ctx.send("text..")
client.run("token...")