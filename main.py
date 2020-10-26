import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json

######################################## BRING TOEKN ########################################
with open('config.json', 'r') as f:
    TOKEN = json.load(f)['token']

######################################## BOT PREFIX ########################################
client_bot = commands.Bot(command_prefix='.')

######################################## PING ########################################
@client_bot.command()
async def ping(ctx):
    """Showes the ms"""
    await ctx.send(f'{round(client_bot.latency * 1000)} ms')

######################################## COGS ########################################
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client_bot.load_extension(f'cogs.{filename[:-3]}')

client_bot.run(TOKEN)
