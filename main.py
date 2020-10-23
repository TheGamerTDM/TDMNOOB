import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json

######################################## BRING TOEKN ########################################
owners = [561936690063605760]

with open('config.json', 'r') as f:
    TOKEN = json.load(f)['token']

######################################## BOT PREFIX ########################################
client_bot = commands.Bot(command_prefix='.', owner_ids=owners)


######################################## PING ########################################
@client_bot.command()
async def ping(ctx):
    await ctx.send(f'{round(client_bot.latency * 1000)} ms')

######################################## COGS ########################################
@client_bot.command()
async def load(ctx, extension):
    client_bot.load_extension(f'cogs.{extension}')


@client_bot.command()
async def unload(ctx, extension):
    client_bot.unload_extension(f'cogs.{extension}')


@client_bot.command()
async def reload(ctx, extension):
    client_bot.reload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client_bot.load_extension(f'cogs.{filename[:-3]}')

client_bot.run(TOKEN)
