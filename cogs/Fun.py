import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re
import praw
import json
import requests
from io import BytesIO
from discord.ext import commands

def setup(bot):
    bot.add_cog(Fun(bot))

agent = praw.Reddit(client_id='Ceva16eRbrWxog',
                    client_secret='0ZaRckgTXapz2D2z1N66UrNJHQQ',
                    user_agent='1.0.0')

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, *, pick):

        hep = ['help', 'HELP']
        # subreddit = ['dankmemes', 'memes', 'ohffensivememes', 'ksi']

        if pick in hep:
            await ctx.send('```py\n1. dankmemes\n2. memes\n3. offensivememes\n4. ksi\n5. Type what you want to see```')
            return

        if pick not in hep:
            # set the apikey and limit
            apikey = "6EFTON5B6X16"  # test value
            lmt = 30

            # our test search
            # _categories = ['excited', 'puppies']
            # rand = random.randint(0, len(_categories) - 1)
            search_term = pick  # _categories[rand]

            # get the top 8 GIFs for the search term
            r = requests.get(
                "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
            # load the GIFs using the urls for the smaller GIF sizes
            data = json.loads(r.content)
            total_gifs = len(data['results'])
            gif = data["results"][random.randint(0, total_gifs)]['url']

            await ctx.send(gif)
        else:
            top_8gifs = None

    @commands.command(aliases=['Reddit', 'rt'])
    async def reddit(self, ctx, *, memez):

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

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def viktor(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/547097300527349775/547576100792827915/video.gif')

    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer! 🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: paaaarty!🎉🍺")
        if user.id == self.bot.user.id:
            return await ctx.send("*drinks beer with you* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")

        beer_offer = f"**{user.name}**, you got a 🍺 offer from **{ctx.author.name}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely beer together 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a beer with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)




