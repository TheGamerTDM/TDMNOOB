import discord
from time import sleep
import praw
import asyncio
import random
import os
import requests
from discord.ext import commands
import json
from main import client_bot


class Admin_Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mc(ctx, member: discord.Member, duration=0, *, unit=None):
        roleobject = discord.utils.get(ctx.message.guild.roles, id=769141888459866123)
        await ctx.send(f":white_check_mark: Muted {member} for {duration}{unit}")
        await member.add_roles(roleobject)
        if unit == "s":
            wait = 1 * duration
            await asyncio.sleep(wait)
        elif unit == "m":
            wait = 60 * duration
            await asyncio.sleep(wait)
        await member.remove_roles(roleobject)
        await ctx.send(f":white_check_mark: {member} was unmuted")

        ##################################################### MUTE/UNMUTE #####################################################
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await member.edit(mute=True, reason=reason)
        await ctx.send(f'Mutede {member.mention}. Reason: {reason}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions()
    async def unmute(self, ctx, member: discord.Member):
        await member.edit(mute=False)
        await ctx.send(f'Unmutede {member.mention}.')


    ##################################################### CLEAR #####################################################
    @commands.command(aliases=['dump', 'remove'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):
        if amount <= 100:
            if amount == 2:
                await ctx.send(f'Yes sir i well remove {amount} as default')
            else:
                await ctx.send(f'Yes sir i well remove {amount}')
            
            sleep(2)
            await ctx.channel.purge(limit=amount + 2)

        else:
            await ctx.send("100 or under please")

    ##################################################### SPAM #####################################################
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def spam(self, ctx, times: int, content='repeating...'):
        if times <= 100:
            for i in range(times):
                await ctx.send(content)
        else:
            await ctx.send(f'Under 100 please. U {times}')


    ##################################################### SAY #####################################################
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def say(self, ctx, *, say):
        await ctx.send(say)
        print(say)

    ##################################################### SEND #####################################################
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def send(self, ctx, channel, *, content):
        if channel == '':
            await ctx.send(content)
        elif "#" in channel:
            channel = client_bot.get_channel(int(channel[2:-1]))
            await channel.send(content)
        else:
            channel = client_bot.get_channel(int(channel))
            await channel.send(content)


    ##################################################### BAN #####################################################
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}. Reason: {reason}')


    ##################################################### KICK #####################################################
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicket {member.mention}. Reason: {reason}')
    

    ##################################################### UNBANN #####################################################
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


def setup(bot):
    bot.add_cog(Admin_Stuff(bot))
