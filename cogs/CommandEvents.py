import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json
from main import client_bot

commands_tally = {

}

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await client_bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="porn with .help ;)"))
        print(f'Logged in as {client_bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + " was invoked incorrectly.")
        print(error)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(commands_tally)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + " was invoked successfully.")

def setup(bot):
    bot.add_cog(CommandEvents(bot))