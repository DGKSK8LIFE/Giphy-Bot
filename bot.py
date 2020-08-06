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

@client.command()
async def help(ctx):
    await ctx.send("""                              
        Commands:
        !help
        !cake
        !vanilla
        !chocolate
        !strawberry
                            
                            
                            
                        """)

@client.command()
async def cake(ctx):
    await ctx.send(embed = discord.Embed().set_image(url = giphy('cake')))

@client.command()
async def vanilla(ctx):
    await ctx.send(embed = discord.Embed().set_image(url = giphy('vanilla cake')))

@client.command()
async def chocolate(ctx):
    await ctx.send(embed = discord.Embed().set_image(url = giphy('chocolate cake')))

@client.command()
async def strawberry(ctx):
    await ctx.send(embed = discord.Embed().set_image(url = giphy('strawberry cake')))

client.run(deserialize()['bot-token']), bot = True)
