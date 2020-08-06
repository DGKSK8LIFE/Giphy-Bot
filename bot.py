import discord
from discord.ext import commands
from giphy import giphy
from deserialize_yaml import deserialize

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Cakebot is ready to donate cakes.")

@client.event
async def on_member_join(member):
    await member.send("A new member has joined")

@client.event
async def on_member_remove(member):
    print("A member has left.")

client.run(deserialize('bot-token'))
