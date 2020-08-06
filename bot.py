import discord
from discord.ext import commands
from giphy import giphy
from deserialize_yaml import deserialize

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'Giphybot ready to assist!')


@client.event
async def on_member_join(member):
    await member.send(f'Giphybot welcomes {member.display_name}.')


@client.event
async def on_member_remove(member):
    print(f'Giphybot is sad to see {member.display_name} go.')


@client.command()
async def gif(ctx, rating):
    if rating == 'g' or rating == 'pg' or rating == 'r':
        await ctx.send(giphy(rating))
    else:
        await ctx.send('Please input a valid rating')

client.run(deserialize('bot-token'))
