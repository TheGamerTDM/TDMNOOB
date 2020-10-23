import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json


class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def spam(self, ctx, times: int, content='repeating...'):
        if times <= 100:
            for i in range(times):
                await ctx.send(content)
        else:
            await ctx.send(f'Under 100 please. U {times}')


def setup(bot):
    bot.add_cog(Spam(bot))
