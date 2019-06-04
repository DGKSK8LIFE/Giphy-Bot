import discord
from discord.ext import commands
from giphy import giphy

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Cakebot is ready to donate cakes.")

@client.event
async def on_member_join(member):
    print(f'Cakebot welcomes, {member}.')

@client.event
async def on_member_remove(member):
    print(f'Cakebot will miss you, {member}.')

@client.command()
async def cake(ctx):
    await ctx.send(embed = discord.Embed().set_image(url = giphy('cake')))

client.run('[token here]', bot = True)
