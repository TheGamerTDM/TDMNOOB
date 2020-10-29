import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands

######################################## BOT PREFIX ########################################
bot = commands.Bot(command_prefix=os.getenv('PREFIX'))


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="with my dick"))
    print(f'Logged in as {bot.user}')
    
    bot.load_extension('Music')

######################################## PING ########################################
@bot.command()
async def ping(ctx):
    """Showes the ping for the bot"""
    await ctx.send(f'{round(bot.latency * 1000)} ms')

######################################## COGS ########################################
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('BOT_TOKEN'))
