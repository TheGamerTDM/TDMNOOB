import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json


class Randomapirequests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        r = requests.get('https://api.thecatapi.com/v1/images/search')
        url = r.json()[0]['url']
        await ctx.send(url)


    @commands.command()
    async def dog(self, ctx):
        r = requests.get('https://api.thedogapi.com/v1/images/search')
        url = r.json()[0]['url']
        await ctx.send(url)

def setup(bot):
    bot.add_cog(Randomapirequests(bot))
