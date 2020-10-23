import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json


class egithball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question):
        fuckyou = ['fuck you', 'FUCK YOU']
        python = ['python', 'PYTHON', 'py']
        if question in python:
            responses = [
                'Ask Gustav',
                'PYTHON IS THE BEST',
                'C# is trash',
                'C# users should programe in python',
                'python is good',
            ]
        elif question in fuckyou:
            responses = ['NO FUCK YOU', 'GO FUCK YOURSELF IDIOT']
        else:
            responses = [
                'As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.',
                "I don't know. Ask yourself",
                'WHAT THE FUCK DO YOU WANT FROM ME YOU FUCK HEAD?',
                'Fuck off',
                'Cunt',
                "Sorry i don't know :(",
                'Having a bad day?'
            ]
        await ctx.send(f'Question: {question}\nMy answer: {random.choice(responses)}')



def setup(bot):
    bot.add_cog(egithball(bot))
