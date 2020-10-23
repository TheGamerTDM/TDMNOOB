import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json
from main import client_bot

agent = praw.Reddit(client_id='Ceva16eRbrWxog',
                    client_secret='0ZaRckgTXapz2D2z1N66UrNJHQQ',
                    user_agent='1.0.0')
class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['MEME','memes','MEMES'])
    async def meme(self, ctx, *, memez):

        hep = ['help', 'HELP']
        subreddit = ['dankmemes', 'memes', 'ohffensivememes', 'ksi']
        banndelist = '' #['porn','furry','pornhub','thick','dick','gonewild','']

        if memez in hep:
            await ctx.send('```py\n1. dankmemes\n2. memes\n3. ohffensivememes\n4. ksi\n5. Type what subreddit you want```')
            return
        if memez not in banndelist:
            if memez not in subreddit:
                memes_submissions = agent.subreddit(memez).hot()
                post_to_pick = random.randint(1, 30)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
            elif memez in subreddit:
                memes_submissions = agent.subreddit(memez)
                post_to_pick = random.randint(1, 30)
                for i, j in enumerate(memes_submissions.hot(limit=30)):
                    if i == post_to_pick:
                        await ctx.send(j.url)
            else:
                await ctx.send("Not a valid subreddit")
        else:
            await ctx.send('U BANDE MF')


def setup(bot):
    bot.add_cog(Memes(bot))
