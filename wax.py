import discord
from time import sleep
import praw
import random
import os
import requests
from discord.ext import commands
import json
import requests



######################################## BRING TOEKN ########################################
TOKEN = ''
with open ('config.json', 'r') as f:
    TOKEN = json.load(f)['token']


######################################## BOT PREFIX ########################################
client_bot = commands.Bot(command_prefix='.')


######################################## BOT LOGIN ########################################
@client_bot.event
async def on_ready():
    await client_bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="porn with .help ;)"))
    print(f'Logged in as {client_bot.user}')


######################################## PING ########################################
@client_bot.command()
async def ping(ctx):
    await ctx.send(f'{round(client_bot.latency * 1000)} ms')


####################################### 8BALL ########################################
@client_bot.command(aliases=['8ball', '8BALL'])
async def _8ball(ctx, *, question):
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


####################################### CLEAR ########################################
@client_bot.command(aliases=['dump', 'remove'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    if amount <= 100:
        if amount == 2:
            await ctx.send(f'Yes sir i well remove {amount} as default')
        else:
            await ctx.send(f'Yes sir i well remove {amount}')
        
        sleep(2)
        await ctx.channel.purge(limit=amount + 2)

    else:
        await ctx.send("100 or under please")



######################################## KICK ########################################
@client_bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicket {member.mention}. Reason: {reason}')


######################################## BAN ########################################
@client_bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}. Reason: {reason}')


######################################## UNBAN ########################################
@client_bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


######################################## SEND ########################################
@client_bot.command()
@commands.has_permissions(administrator=True)
async def send(ctx, channel, *, content):
    if channel == '':
        await ctx.send(content)
    elif "#" in channel:
        channel = client_bot.get_channel(int(channel[2:-1]))
        await channel.send(content)
    else:
        channel = client_bot.get_channel(int(channel))
        await channel.send(content)


######################################## SAY ########################################
@client_bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, say):
    await ctx.send(say)


######################################## SPAM ########################################
@client_bot.command()
async def spam(ctx, times: int, content='repeating...'):
    if times <= 100:
        for i in range(times):
            await ctx.send(content)
    else:
        await ctx.send(f'Under 100 please. U {times}')


######################################## img request ########################################
@client_bot.command()
async def cat(ctx):
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    await ctx.send(url)


@client_bot.command()
async def dog(ctx):
    r = requests.get('https://api.thedogapi.com/v1/images/search')
    url = r.json()[0]['url']
    await ctx.send(url)


######################################## ADD ROLE WHEN REACT ########################################
@client_bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 766229056273645568:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client_bot.guilds)

        if payload.emoji.name == 'Amongus':
            role = discord.utils.get(guild.roles, name='Amongus')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print('member not found')
        else:
            print('role not found')


@client_bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 766229056273645568:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client_bot.guilds)

        if payload.emoji.name == 'Amongus':
            role = discord.utils.get(guild.roles, name='Amongus')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print('member not found')
        else:
            print('role not found')


######################################## Reddit meme ########################################
agent = praw.Reddit(client_id='Ceva16eRbrWxog',
                     client_secret='0ZaRckgTXapz2D2z1N66UrNJHQQ',
                     user_agent='1.0.0')

@client_bot.command(aliases=['MEME','memes','MEMES'])
async def meme(ctx, *, memez=None):

    hep = ['help', 'HELP']

    if memez == 'dankmemes':
        memes_submissions = agent.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)
    elif memez == 'memes':
        memes_submissions = agent.subreddit('memes').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)
    elif memez == 'ohffensivememes':
        memes_submissions = agent.subreddit('ohffensivememes').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)
    elif memez == 'ksi':
        memes_submissions = agent.subreddit('ksi').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)
    elif memez in hep:
        await ctx.send('```py\n1. dankmemes\n2. memes\n3. ohffensivememes\n4. ksi\n5. Type what subreddit you want```')
    else:
        await ctx.send('Please type a subreddit or do ".meme help" for more help')
        return
            
    
    if memez in hep:
        return
    else:
        memes_submissions = agent.subreddit(memez).hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)



######################################## TESTING PLACE ########################################



######################################## TOKEN ########################################
client_bot.run(TOKEN)
