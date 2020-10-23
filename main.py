import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json

######################################## BRING TOEKN ########################################
TOKEN = ''
with open('config.json', 'r') as f:
    TOKEN = json.load(f)['token']

######################################## BOT PREFIX ########################################
client_bot = commands.Bot(command_prefix='.')


######################################## PING ########################################
@client_bot.command()
async def ping(ctx):
    await ctx.send(f'{round(client_bot.latency * 1000)} ms')


@client_bot.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def viktor(ctx):
    await ctx.send('https://media.discordapp.net/attachments/547097300527349775/547576100792827915/video.gif')


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
