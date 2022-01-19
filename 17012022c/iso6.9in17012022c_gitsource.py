# modules
import os
import random
import discord
import asyncio
import datetime
import time
import cmath
import math
import string
import praw
import prawcore
from datetime import datetime
from random import randint
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands import *
from keep_alive import keep_alive

intents = discord.Intents(messages=True, members=True, guilds=True)

# var
token = "token"
cid = "client_id"
owner = ["αrchιshα#5518", "notsniped#4573", "thatOneArchUser#5794"]
oid = [706697300872921088, 738290097170153472, 705462972415213588]
reddit = praw.Reddit(client_id='reddit_client_id',
                     client_secret='reddit_client_secret',
                     user_agent='idk copied from thatOneArchUser', check_for_async=False)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# prefix and status setup
bot = commands.Bot(command_prefix=']', intents=intents)

# when ready
@bot.event
async def on_ready():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(f'\n> {bot.user} HAS CONNECTED TO DISCORD.\n\n> OWNER:\n')
    for i in owner:
        print(f"{i}\n")
    print("OWNER\'S ID:\n")
    for s in oid:
        print(f"{s}\n")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print(f'[log] Log is loading...')
    print(f'[log] {bot.user} changed its activity.')

@bot.event
async def on_guild_join(guild):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print(f'[log] {bot.user} changed its activity.')

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"everyone in {str(len(bot.guilds))} guilds | ]help"))
    print(f'[log] {bot.user} changed its activity.')
# end of startup

# error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument(s).')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permission to do that. :eyes:")
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, BotMissingPermissions):
        await ctx.send('I don\'t have the required permissions to use this.')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument')
        print(f'[log] {ctx.author} returned an error: {error}.')
    if isinstance(error, commands.CommandOnCooldown):
        if math.ceil(error.retry_after) < 60:
            await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
            print(f'[log] {ctx.author} returned an error: {error}.')
        elif math.ceil(error.retry_after) < 3600:
            ret = math.ceil(error.retry_after) / 60
            await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)} minutes')
            print(f'[log] {ctx.author} returned an error: {error}.')
        elif math.ceil(error.retry_after) >= 3600:
            ret = math.ceil(error.retry_after) / 3600
            if ret >= 24:
                r = math.ceil(ret) / 24
                await ctx.reply(f"This command is on cooldown. Please try after {r} days")
                print(f'[log] {ctx.author} returned an error: {error}.')
            else:
                await ctx.reply(f'This command is on cooldown. Please try after {math.ceil(ret)}')
                print(f'[log] {ctx.author} returned an error: {error}.')
            # How to use cooldowns:
            # after @bot.command() add @commands.cooldown(1, cooldown, commands.BucketType.user)
# end of error handler

# help cmd
bot.remove_command('help')

@bot.command(aliases=['help'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed(ctx):
    embed=discord.Embed(title="**help command list of iso6.9**", description="version: 17012022c\ncurrent prefix: `]`", color=discord.Color.blue())
    embed.add_field(name='moderation:', value="kick, ban, unban, purge, mute, unmute, warn, lock, unlock", inline=False)
    embed.add_field(name='informative:', value="testcmd, ping, serverlist, morebots, serverinfo, userinfo, invites, avatar, cmdinfo", inline=False)
    embed.add_field(name='misc:', value="snipe (channel), edit_snipe (global), 8ball, fstab, roll, say, null, sus, notify, stroke, randnum, kill, amogus, guess, duel, cup, lick, spam, encode, decode, stroktranslate, reddit", inline=False)
    embed.add_field(name='mathematics:', value="sum, subtract, multiply, divide, power, squareroot", inline=False)
    embed.add_field(name='advanced maths:', value="quadratic, straightline", inline=False)
    embed.add_field(name='administrator:', value="> use `sudo help` to get details about admin commands.", inline=False)
    embed.set_footer(text="> type ]ahelp to get alias list.\n(Information requested by: {})".format(ctx.author))
    await ctx.reply(embed=embed)
    print(f'[log] {ctx.author} requested ]help.')

@bot.command(aliases=['ahelp'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed77(ctx):
    embed=discord.Embed(title='**alias list of iso6.9**', description='> use aliases to shorten commands', color=discord.Color.blue())
    embed.add_field(name='moderation:', value='kick, ban, unban, clear, shutup, unmute, warn, lock, unlock', inline=False)
    embed.add_field(name='informative:', value="test, ping, slist, bots, sinfo, whois, invites, av, cinfo", inline=False)
    embed.add_field(name='misc:', value="snipe (channel), edit_snipe (global), 8ball, fstab, roll, say, null, sus, notify, stroke, randgen, kill, amogus, guess, duel, cup, lick, spam, enc, dec, stroktrans, reddit", inline=False)
    embed.add_field(name='mathematics:', value="+, -, *, /, **, sqrt", inline=False)
    embed.add_field(name='advanced maths:', value="quad, stline", inline=False)
    embed.add_field(name='administrator:', value="> use `sudo help` to get details about admin commands.", inline=False)
    embed.set_footer(text='> type ]help to get the original list.\n(Information requested by: {})'.format(ctx.author))
    await ctx.reply(embed=embed)
    print(f'[log] {ctx.author} requested ]ahelp.')

@bot.command(aliases=['cinfo'])
async def cmdinfo(ctx, search: str):
    if search == "cmdinfo" or search == "cinfo":
        embed=discord.Embed(title="\"cmdinfo\" command:", description="did you expected me to write something interesting here", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]cmdinfo <command_name_or_aliases>`\ncooldown (second): `none`\ncatagory: `informative`\naliases: `cinfo`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "help":
        embed=discord.Embed(title="\"help\" command:", description="why do you even need help on help command", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]help`\ncooldown (second): `none`\ncatagory: `none`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "kick":
        embed=discord.Embed(title="\"kick\" command:", description="kicks a user out the ~~Linux~~ server", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]kick <mention_user>/<user_id>/<user_name> [reason]`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "ban":
        embed=discord.Embed(title="\"ban\" command:", description="uses ban hammer on a user", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]ban <mention_user>/<user_id>/<user_name> [reason]`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "unban":
        embed=discord.Embed(title="\"unban\" command:", description="unbans a user from banned list ~~of not using Arch Linux~~", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]unban <mention_user>/<user_id>/<user_name>`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "purge" or search == "clear":
        embed=discord.Embed(title="\"purge\" command:", description="clears an amount of messages in the channel", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]purge <amount(int)>`\ncooldown (second): `3`\ncatagory: `moderation`\naliases: `clear`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "mute" or search == "shutup":
        embed=discord.Embed(title="\"mute\" command:", description="mutes a user so that they can shut up", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]mute <mention_user>/<user_id>/<user_name> [reason]`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `shutup`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "unmute":
        embed=discord.Embed(title="\"unmute\" command:", description="unmutes a user so they can be free to talk again", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]unmute <mention_user>/<user_id>/<user_name>`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "warn":
        embed=discord.Embed(title="\"warn\" command:", description="warns the user if they did something wrong", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]warn <mention_user>/<user_id>/<user_name> [reason]`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "lock":
        embed=discord.Embed(title="\"lock\" command:", description="locks specific channel so people are unable to talk in it", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]lock <mention_channel>/<channel_id>/<channel_name>`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "unlock":
        embed=discord.Embed(title="\"unlock\" command:", description="unlocks specific channel so people can talk in it again", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]unlock <mention_channel>/<channel_id>/<channel_name>`\ncooldown (second): `10`\ncatagory: `moderation`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "ping":
        embed=discord.Embed(title="\"ping\" command:", description="shows bot's ping", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]ping`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "serverlist" or search == "slist":
        embed=discord.Embed(title="\"serverlist\" command:", description="101% not advertising servers by the owner", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]serverlist`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `slist`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "morebots" or search == "bots":
        embed=discord.Embed(title="\"morebots\" command:", description="im 101% sure im not advertising my partner's bots", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]morebots`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `bots`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "userinfo" or search == "whois":
        embed=discord.Embed(title="\"userinfo\" command:", description="shows info about the user", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]userinfo <mention_user>/<user_id>/<user_name>`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `whois`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "invites":
        embed=discord.Embed(title="\"invites\" command:", description="shows a user's invited count (people)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]invites [mention_user]/[user_id]`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "avatar" or search == "av":
        embed=discord.Embed(title="\"avatar\" command:", description="shows a user's avatar", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]avatar [mention_user]/[user_id]`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `av`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "snipe":
        embed=discord.Embed(title="\"snipe\" command:", description="snipes the last deleted message in current channel that you're in", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]snipe`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "serverinfo" or search == "sinfo":
        embed=discord.Embed(title="\"serverinfo\" command:", description="shows info about the server", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]serverinfo`\ncooldown (second): `5`\ncatagory: `informative`\naliases: `sinfo`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "edit_snipe":
        embed=discord.Embed(title="\"edit_snipe\" command:", description="snipes the last edited message (sync in global)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]edit_snipe`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "8ball":
        embed=discord.Embed(title="\"8ball\" command:", description="ask the bot something to get a response from it", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]8ball <question>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "fstab":
        embed=discord.Embed(title="\"fstab\" command:", description="fstab.goldfish", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]fstab`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "roll":
        embed=discord.Embed(title="\"roll\" command:", description="rolls dice", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]roll <number_of_dice> <sides_of_dice>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "say":
        embed=discord.Embed(title="\"say\" command:", description="makes the bot say something", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]say <message>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "null":
        embed=discord.Embed(title="\"null\" command:", description="imagine trying to get a null", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]null`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "sus":
        embed=discord.Embed(title="\"sus\" command:", description="you are sus", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]sus <mention_user>/<user_id>/<user_name>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "stroke":
        embed=discord.Embed(title="\"stroke\" command:", description="generates a stroke", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]stroke <length>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "randnum" or search == "randgen":
        embed=discord.Embed(title="\"randnum\" command:", description="a random number generator", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]randnum <minimum_value> <maximum_value>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `randgen`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "kill":
        embed=discord.Embed(title="\"kill\" command:", description="kills specific user with custom weapon", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]kill <mention_user> <weapon>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "amogus":
        embed=discord.Embed(title="\"amogus\" command:", description="amogus twirk", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]amogus`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "guess":
        embed=discord.Embed(title="\"guess\" command:", description="the bot picks one number from 1 to 9, guess what it picked", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]guess <value>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "duel":
        embed=discord.Embed(title="\"duel\" command:", description="duels with other user (auto fight system btw)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]duel <mention_user>/<user_id>/<user_name>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "cup":
        embed=discord.Embed(title="\"cup\" command:", description="the bot puts a ball in 1 of the 3 cups, guess which cup the ball is in", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]ball`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "lick":
        embed=discord.Embed(title="\"lick\" command:", description="a random nsfw command, why would you lick someone though", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]lick <mention_user>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "encode" or search == "enc":
        embed=discord.Embed(title="\"encode\" command:", description="encodes a message with Archiescript (about the method on encoding please ask thatOneArchUser#5794)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]encode <message>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `enc`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "decode" or search == "dec":
        embed=discord.Embed(title="\"decode\" command:", description="decodes a message encoded with Archiescript (about tge method on decoding please ask thatOneArchUser#5794)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]decode <message>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `dec`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "stroktranslate" or search == "stroktrans":
        embed=discord.Embed(title="\"stroktranslate\" command:", description="a translator that translates word strokes to another word stroke", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]stroktranslate <message>`\ncooldown (second): `5`\ncatagory: `misc`\naliases: `stroktrans`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "sum" or search == "+":
        embed=discord.Embed(title="\"sum\" command:", description="sums up 2 or more numbers", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]sum <value1> <value2> [value3_or_more]`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `+`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "subtract" or search == "-":
        embed=discord.Embed(title="\"subtract\" command:", description="subtracts 2 or more numbers", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]subtract <value1> <value2> [value3_or_more]`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `-`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "multiply" or search == "*":
        embed=discord.Embed(title="\"multiply\" command:", description="multiplies 2 numbers", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]multiply <value1> <value2>`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `*`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "divide" or search == "/":
        embed=discord.Embed(title="\"divide\" command:", description="divides 2 numbers", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]divide <value1> <value2>`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `/`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "power" or search == "**":
        embed=discord.Embed(title="\"power\" command:", description="powers 2 numbers", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]power <value1> <value2>`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `**`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "squareroot" or search == "sqrt":
        embed=discord.Embed(title="\"squareroot\" command:", description="squareroots 1 number", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]squareroot <value>`\ncooldown (second): `5`\ncatagory: `mathematics`\naliases: `sqrt`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "quaduatic" or search == "quad":
        embed=discord.Embed(title="\"quaduatic\" command:", description="solve a quaduatic equation by typing its a value, b value, and c value (y=ax^2+bx+c/y=a(x-h)^2+k)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]quaduatic <a> <b> <c>`\ncooldown (second): `5`\ncatagory: `advanced maths`\naliases: `quad`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "straightline" or search == "stline":
        embed=discord.Embed(title="\"straightline\" command:", description="find the details from a straight line equation (y=mx+c/ax+bx+c=0)", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]straightline <a> <b> <c>`\ncooldown (second): `5`\ncatagory: `advanced maths`\naliases: `stline`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    elif search == "reddit":
        embed=discord.Embed(title="\"reddit\" command:", description="gets a subreddit post", color=discord.Color.blue())
        embed.add_field(name=".", value='usage: `]reddit <subreddit_name>`\ncooldown (second): `none`\ncatagory: `misc`\naliases: `none`', inline=False)
        embed.set_footer(text='*<> is required, [] is optional.\nnone means None.*')
        await ctx.send(embed=embed)
        print(f"[log] {ctx.author} requested ]cmdinfo.")
    else:
        await ctx.reply(f"no such command ({search})")
        print(f"[log] {ctx.author} returned an error: Bad argument.")


# sudo
@bot.event
async def on_message(message):
    embed=discord.Embed(title='**admin command list of iso6.9**', description='admin prefix: `sudo\{space\}`', color=discord.Color.green())
    embed.add_field(name='control:', value='shutdown', inline=False)
    embed.set_footer(text='you\'re an admin, wow')
    await bot.process_commands(message) # add this if you're also using cmd decorators
    if message.content.startswith("sudo help") and not message.author.bot:
        if message.author.id in oid:
            await message.reply(embed=embed)
            print(f'[{message.author.name}@iso6.9 ~] requested sudo command.')
        else:
            await message.reply(f'{message.author.name} you are not an admin!')
            print(f'[log] Beware! Non-admin using sudo command detected. Requested by: {message.author}')
    if message.content.startswith("sudo shutdown") and not message.author.bot:
        def check(msg): return msg.author == message.author and msg.channel == message.channel and (msg.content)
        if message.author.id in oid:
            await message.reply('You sure?')
            msg = await bot.wait_for("message", check=check)
            if msg.content == 'y' or msg.content == 'yes':
                await message.reply('Shutting down the bot...')
                time.sleep(0.5)
                print(f'[{message.author.name}@iso6.9 ~] SystemExit triggered in sudo command.')
                raise SystemExit('Bot shutdown')
            elif msg.content == 'n' or msg.content == 'no': await message.reply('ok')
            else:
                await message.reply(f'What is {msg.content}? You are supposed to reply with yes or no')
                print(f'[log] {message.author} returned an error: Bad argument.')
        else:
            await message.reply(f'hOW AboUt nO :eyes:')
            print(f'[log] {message.author} returned an error: User not admin.')
    # auto response
    if message.content.startswith("ayo") and not message.author.bot:
        await message.reply("ayo")
        print(f"[interact] {bot.user} reacted.")
    if message.content.startswith("👀") and not message.author.bot:
        await message.reply(":eues: :eyes:")
        print(f"[interact] {bot.user} reacted.")
    if message.content.startswith("wtf") and not message.author.bot:
        await message.reply("what the actual fuck?")
        print(f"[interact] {bot.user} reacted.")
    if message.content.startswith("hmm") and not message.author.bot:
        await message.reply("hmmmmmmmm :thinking:")
        print(f"[interact] {bot.user} reacted.")
    if message.content.startswith("strok") or message.content.startswith("strole") or message.content.startswith("strokw") and not message.author.bot:
        await message.reply("imagine having a stroke, lol eyieyulgkbnkdhd")
        print(f"[interact] {bot.user} reacted.")
    if message.content.startswith("iso") and not message.author.bot:
        await message.reply("who summoned me :face_with_raised_eyebrow:")
        print(f"[interact] {bot.user} reacted.")

# cmds
@bot.command(aliases=['test'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def testcmd(ctx):
    await ctx.send(random.choice(['this is a test command', 'did u just used ]test?']))
    print(f'[log] {ctx.author} requested ]test.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    print(f'[log] {ctx.author} requested ]roll.')

@bot.command(aliases=['8ball'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def _8ball(ctx, *, question):
    responses = [
            "no?????",
            "When you grow a braincell, yes",
            "You stupid, of course not",
            "lol no",
            "Absolutely!",
            "Bet on it",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Idfk",
            "Try again",
            "Not today.",
            "I\'m not very sure, but I think the answer is no.",
            "I\'m not very sure, but I think the answer is yes!",
            "brain.exe stopped responding.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Its a secret :>",
            "Can\'t tell you lmao",
            "Is Trump\'s skin orange?",
            "What do you think",
            "No. Just, no",
            "I'\m an 8ball, not a dealwithyourcrap ball",
            "if not not False:",
            "if not not True:",
            "null",
            "Imagine me not wanting to answer this question"
    ]
    ballEmbed = discord.Embed(title=f':8ball: {question}', description=f'{random.choice(responses)}')
    await ctx.send(embed=ballEmbed)
    print(f'[log] {ctx.author} requested ]8ball.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(f'Client Latency: {round(bot.latency * 1000)}ms')
    print(f'[log] {ctx.author} requested ]ping.')

# fstab var
fstaburl1 = "https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg"
fstaburl2 = "https://media.discordapp.net/attachments/876826249820004385/884040441195003954/Screenshot_158.png"
fstaburl3 = "https://media.discordapp.net/attachments/915898952182796298/916626889165115422/Screenshot_2017-10-10-01-22-57_com.speedsoftware.explorer_1507591405249.jpg"
fstaburl4 = "https://media.discordapp.net/attachments/915898952182796298/916626889412599858/644b5b9e083e806173eabcde0b6b5f0c_720w.png"

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def fstab(ctx):
    await ctx.send(random.choice([fstaburl1, fstaburl2, fstaburl3, fstaburl4]))
    print(f'[log] {ctx.author} requested ]fstab.')

# slist var
archlink = "<https://discord.gg/aw4AcZys6p>"
smlink = "<https://discord.gg/tJqDMucEYG>"
isolink = "<https://discord.gg/zTqZqQCcAg>"

@bot.command(aliases=["serverlist", "slist"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed_2(ctx):
    embed=discord.Embed(title="**server list**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch Island (aka Hecker\'s Hub\):", value=f"{archlink}", inline=False)
    embed.add_field(name=f"2. Scope Media (aka SM\):", value=f"{smlink}", inline=False)
    embed.add_field(name=f"3. iso.bot (aka isobot\'s supporting server\):", value=f"{isolink}", inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]serverlist.')

# bots var
archbot = "https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot"
isobot = "https://discord.com/api/oauth2/authorize?client_id=896437848176230411&permissions=8&scope=bot"
isobot2 = "https://discord.com/oauth2/authorize?client_id=915488087554002956&permissions=8&scope=bot"

@bot.command(aliases=["morebots", "bots"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def embed_3(ctx):
    embed=discord.Embed(title="**Discover more bots!**", description="~~(101% not advertising)~~", color=0xFF5733)
    embed.add_field(name=f"1. Arch bot#6142 (aka Archbot\):", value=f"{archbot}", inline=False)
    embed.add_field(name=f"2. isobot#6851 (aka Official isobot\):", value=f"{isobot}", inline=False)
    embed.add_field(name=f"3. iso6.9#4895 (aka isobot v6.9\):", value=f"{isobot2}", inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]morebots.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')
    print(f'[log] {ctx.author} requested ]say, content: {ctx.message_content}.')

@bot.command(aliases=["null"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def null_1(ctx):
    await ctx.send(random.choice(["Oh so you want a **null**? Here you are: ", "You got **null**! Congratulations!", "Ok here is your **null**, enjoy!", "**null**.", "Well, you don\'t know what is null? Here is your **null**..."]))
    print(f'[log] {ctx.author} requested ]null.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked successfully.')
    print(f'[log] {ctx.author} requested ]kick.')

@bot.command(pass_context=True, aliases=['clear'])
@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_permissions(administrator=True, manage_channels=True)
async def purge(ctx, amount: int):
    if int(amount) == 0: return await ctx.reply("You can\'t purge 0 messages **dood**.")
    elif int(amount) < 0: return await ctx.reply("You can\'t spawn messages, lol.")
    elif int(amount) > 500: return await ctx.reply("You can\'t purge more than 500 messages :face_with_raised_eyebrow:")
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    em = discord.Embed(title='Purge Successful', description=f'Purged {amount} messages from this channel.', color=discord.Colour.random())
    await ctx.send(embed = em)

@bot.command(aliases=['shutup'])
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels: await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted successfully.", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]mute.')
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"you have been muted from: {guild.name}\n reason: {reason}")
    print(f'[log] {ctx.author} \'s DM has successfully sent.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: - {ctx.guild.name}")
   print(f'[log] {ctx.author} \'s DM has successfully sent.')
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)
   print(f'[log] {ctx.author} requested ]unmute.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned successfully.')
    print(f'[log] {ctx.author} requested ]ban.')

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.reply(f"I unbanned {user}")
    print(f'[log] {ctx.author} requested ]unban.')

# snipe
snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(title = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
        print(f'[log] {ctx.author} requested ]snipe.')
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")
        print(f'[log] {ctx.author} returned an error: No recently deleted messages.')
# end of snipe

# edit_snipe
@bot.event
async def on_message_edit(message_before, message_after):
    if not message_after.author.bot:
        global author
        author = message_before.author
        guild = message_before.guild.id
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
        print(f'[log] {ctx.author} requested ]edit_snipe.')
    except:
        await ctx.reply('No recently edited messages here :eyes:')
        print(f'[log] {ctx.author} returned an error: No recently edited messages.')
# end of edit_snipe

@bot.command(aliases=['sinfo'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    gowner = str(ctx.guild.owner)
    gid = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(
        title=name + " Server Information",
         description=description,
         color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=gowner, inline=True)
    embed.add_field(name="Server ID", value=gid, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]serverinfo.')

@bot.command(aliases=['whois'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, *, member:discord.Member = None):
    if member == None: member = ctx.message.author
    embed=discord.Embed(
        title="User Information", 
        timestamp=datetime.utcnow(),
        color=discord.Color.random()
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Username:", value=member.name, inline=False)
    embed.add_field(name="Nickname (Displayed Name As):", value=member.nick, inline=False)
    embed.add_field(name="User ID:", value=member.id, inline=False)
    embed.add_field(name="Account Created At:",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Joined Server At:",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
    await ctx.send(embed=embed)
    print(f'[log] {ctx.author} requested ]userinfo.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user:discord.User = None, *, warn_reason=None):
    if user == None:
        await ctx.reply('Please mention a user when you want to warn someone next time.')
        print(f'[log] {ctx.author} returned an error: No user mentioned.')
        return
    try:
        if warn_reason == None: warn_reason = '*Not provided*'
        embed67 = discord.Embed(title=f'You were warned in {ctx.guild}.', description=f'Reason: {warn_reason}', color=discord.Color.blue())
        await user.send(embed = embed67)
        print(f'[log] {ctx.author} \'s DM has successfully sent.')
        embed70 = discord.Embed(title=f':white_check_mark: I successfully warned **{user}**.', color=discord.Color.green())
        await ctx.send(embed = embed70)
        print(f'[log] {ctx.author} requested ]warn.')
    except:
        embed71 = discord.Embed(title=f':x: Hold up!', description=f'I was unable to warn {user}.\nThis is usually caused due to the user not accepting DMs.', color=discord.Color.red())
        await ctx.send(embed = embed71)
        print(f'[log] {ctx.author} returned an error: DM not opened.')


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def notify(ctx, user:discord.User = None, *, message):
    if user == None:
        await ctx.reply('If you want to notify a user, you need to mention someone.')
        return print(f'[log] {ctx.author} returned an error: No user mentioned.')
    embed64 = discord.Embed(title=f'{ctx.message.author} notified you!', description=f'Message: {message}', color=discord.Color.blue())
    await user.send(embed = embed64)
    print(f'[log] {ctx.author} \'s DM has successfully sent.')

    embed61 = discord.Embed(title=f':white_check_mark: I notified **{user}**', description=f'Message content: {message}', color=discord.Color.green())
    await ctx.channel.send(embed = embed61)
    print(f'[log] {ctx.author} requested ]notify, content: {ctx.message_content}.')

@bot.command(aliases=['sus'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def isSus(ctx, *, user: discord.User):
    sus = random.choice([True, False])
    if bool(sus) == True:
        await ctx.send(f'{user.mention} is very sus')
    elif bool(sus) == False:
        await ctx.send(f'{user.mention} isn\'t sus')
    else:
        await ctx.reply('undefined')
    print(f'[log] {ctx.author} requested ]sus.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed72 = discord.Embed(title='Channel locked successfully.')
    await ctx.send(embed=embed72)
    print(f'[log] {ctx.author} requested ]lock.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed73 = discord.Embed(title='Channel unlocked successfully.')
    await ctx.send(embed=embed73)
    print(f'[log] {ctx.author} requested ]unlock.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def stroke(ctx, size: int):
    def random_string_generator(str_size, allowed_chars): return ''.join(random.choice(allowed_chars) for x in range(str_size))
    chars = string.ascii_letters + string.punctuation
    if size > 550:
        await ctx.send(f'{size} is more than the limit. The max character limit is set to 550 to avoid spam.')
        print(f'[log] {ctx.author} returned an error: Max character limit reached.')
    else:
        await ctx.send(random_string_generator(size, chars))
        print(f'[log] {ctx.author} requested ]stroke.')

# maths cmds
@bot.command(aliases=['+'])
async def sum(ctx, *nums:float):
    ans = 0
    arr = list()
    for num in nums:
        ans += num
        arr.append(str(num))
    var = ' + '.join(arr)
    await ctx.send(f"`{var} = {ans}`\n--end of calculation--")
    print(f'[log] {ctx.author} requested ]sum.')

@bot.command(aliases=['-'])
async def subtract(ctx, *nums:float):
    nums = list(nums)
    arr = list()
    arr.append(str(nums[0]))
    ans = nums[0]
    nums.remove(nums[0])
    for num in nums:
        ans -= num
        arr.append(str(num))
    var = ' - '.join(arr)
    await ctx.send(f"{var} = {ans}\n--end of calculation--")
    print(f'[log] {ctx.author} requested ]subtract.')

@bot.command(aliases=['*'])
async def multiply(ctx, num1: float, num2: float):
    ans = str(num1 * num2)
    await ctx.send(f'`{num1} × {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]multiply.')

@bot.command(aliases=['/'])
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send("math error: it can\'t be divided by zero.")
        print(f'[log] {ctx.author} returned an math error: Divide by zero.')
        return
    ans = str(num1 / num2)
    await ctx.send(f'`{num1} ÷ {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]divide.')

@bot.command(aliases=['**'])
async def power(ctx, num1: float, num2: int):
    ans = str(num1 ** num2)
    await ctx.send(f'`{num1} ^ {num2}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]power.')

@bot.command(aliases=['sqrt'])
async def squareroot(ctx, num: float):
    ans = cmath.sqrt(num)
    await ctx.send(f'`√ {num}` = __{ans}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]squareroot.')

@bot.command(aliases=['quad'])
async def quadratic(ctx, a: float, b: float, c: float):
    delta = (b**2) - (4*a*c)
    r1 = (-b+cmath.sqrt(delta)) / (2*a)
    r2 = (-b-cmath.sqrt(delta)) / (2*a)
    await ctx.send(f'The roots of `({a})x^(2)+({b})x+({c})` are __{r1}__ and __{r2}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]quadratic.')

@bot.command(aliases=['stline'])
async def straightline(ctx, A: float, B: float, C: float):
    x = -C / A
    y = -C / B
    m = -A / B
    await ctx.send(f'x-intercept = __{x}__\ny-intercept = __{y}__\nslope of straight line= __{m}__\n\n--end of calculation--')
    print(f'[log] {ctx.author} requested ]straightline.')
# end of maths

@bot.command(aliases=['randgen'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def randnum(ctx, range1: int, range2: int):
    num = random.randint(range1, range2)
    await ctx.send(f'{num} is being picked.')
    print(f'[log] {ctx.author} requested ]randnum.') 

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kill(ctx, user: discord.User, weapon: str):
    await ctx.send(f'{ctx.author} killed {user} with {weapon}, ouch.')
    print(f'[log] {ctx.author} requested ]kill.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def amogus(ctx):
    await ctx.reply("https://c.tenor.com/1iSARWJr-TEAAAAC/among-us-twerk.gif")
    print(f'[log] {ctx.author} requested ]amogus.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def guess(ctx, num: int):
    rand = random.randint(1, 9)
    if num == rand: await ctx.reply(f'Your choice is {num}, you guessed it right!')
    else: await ctx.reply(f'Your choice is {num}, wrong!\nMy choice is {rand}.')
    print(f'[log] {ctx.author} requested ]guess.')

# duel
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def duel(ctx, player2: discord.User):
    if ctx.author == player2:
        await ctx.reply('Imagine fighting against yourself :eyes:', mention_author=False)
        print(f'[log] {ctx.author} returned an error: Bad argument.')
        raise InvalidArgument
# var
    normal = ['Eclipse', 'Magic Attack', 'Power Burst', 'Dragon Slayer', 'Time Stealer']
    special = ['Arch Strike', 'Arch Morph', 'Arch Aptitude', 'Fstab', 'Sudo Attack']
#
    definer1 = random.randint(1, 2)
    definer2 = random.randint(1, 2)
    definer3 = random.randint(1, 2)
    definer4 = random.randint(1, 2)

    if definer1 == 1: pick1 = random.choice(special)
    elif definer1 == 2: pick1 = random.choice(normal)
    if definer2 == 1: pick2 = random.choice(special)
    elif definer2 == 2: pick2 = random.choice(normal)
    if definer3 == 1: pick3 = random.choice(special)
    elif definer3 == 2: pick3 = random.choice(normal)
    if definer4 == 1: pick4 = random.choice(special)
    elif definer4 == 2: pick4 = random.choice(normal)
#
    if pick1 in normal: hplost1 = random.randint(0, 30)
    elif pick1 in special: hplost1 = random.randint(30, 50)
    if pick2 in normal: hplost2 = random.randint(0, 30)
    elif pick2 in special: hplost2 = random.randint(30, 50)
    if pick3 in normal: hplost3 = random.randint(0, 30)
    elif pick3 in special: hplost3 = random.randint(30, 50)
    if pick4 in normal: hplost4 = random.randint(0, 30)
    elif pick4 in special: hplost4 = random.randint(30, 50)
#
    hplast1 = 100 - hplost2 - hplost4
    hplast2 = 100 - hplost1 - hplost3
#
    if hplast1 > hplast2: winner = ctx.author
    elif hplast1 < hplast2: winner = player2
    elif hplast1 == hplast2: winner = "No one"
#
    await ctx.send(f'{ctx.author} used {pick1}, dealt {hplost1}!')
    await ctx.send(f'{player2} used {pick2}, dealt {hplost2}!')
    await ctx.send(f'{ctx.author} used {pick3}, dealt {hplost3}!')
    await ctx.send(f'{player2} used {pick4}, dealt {hplost4}!')
    if hplast1 < 0 and hplast2 < 0: return await ctx.send(f"{ctx.author} and {player2} both died, LOL.")
    else: await ctx.send(f'{ctx.author}\'s hp: {hplast1}\n{player2}\'s hp: {hplast2}\n\n{winner} won!')
    print(f'[log] {ctx.author} requested ]duel with {player2}')
# end of duel

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def invites(ctx, *, user : discord.User=None):
    totalInvites = 0
    if user == None:
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author: totalInvites += i.uses
        e = discord.Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
        await ctx.reply(embed=e)
        print(f'[log] {ctx.author} requested ]invites.')
    elif user.bot:
        await ctx.reply('This is a bbotnot a user')
        print(f'[log] {ctx.author} returned an error: Bad argument.')
    else:
        for i in await ctx.guild.invites():
            if i.inviter == user: totalInvites += i.uses
        e = discord.Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
        await ctx.reply(embed=e)
        print(f'[log] {ctx.author} requested ]invites.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cup(ctx):
    await ctx.send("i put a ball in one of the three cups, guess which cup the ball is placed inside. (1/2/3)")
    ballincup = random.randint(1, 3)
    def check(msg): return msg.author == ctx.author and msg.channel == ctx.channel and (msg.content)
    msg = await bot.wait_for("message", check=check)
    try: int(msg.content)
    except ValueError:
        await ctx.reply(f"wtf is {msg.content}")
        print(f'[log] {ctx.author} returned an error: Invaild argument.')
    if int(msg.content) not in range(4):
        await ctx.reply(f"{msg.content} is not a valid number")
        print(f'[log] {ctx.author} returned an error: Bad argument.')
    elif int(msg.content) == ballincup:
        await ctx.reply("correc, gg")
        print(f'[log] {ctx.author} requested ]cup.')
    else:
        await ctx.reply("incorrec, oof")
        print(f'[log] {ctx.author} requested ]cup.')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def lick(ctx, user: discord.User=None):
    if user == None:
        await ctx.reply(f'{ctx.author} don\'t try to lick people dood.')
        print(f'[log] {ctx.author} returned an error: Missing required argument.')
    elif user == bot.user:
        await ctx.reply(f'You licked me- WAIT A SECOND, EW!', mention_author=False)
        print(f'[log] {ctx.author} requested ]lick.')
    elif user == ctx.author:
        await ctx.reply(f'You can\'t lick yourself dood, no one would like to lick themselves...')
        print(f'[log] {ctx.author} returned an error: Bad argument.')
    else:
        await ctx.reply(f'You licked {user}... Are you sure that\'s ok...? Ew.', mention_author=False)
        print(f'[log] {ctx.author} requested ]lick.') 

@bot.command(aliases=['av'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, username: discord.User=None):
    if username == None:
        userAvatar = ctx.message.author.avatar_url
        embed182 = discord.Embed(title=f'{ctx.message.author}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)
        print(f'[log] {ctx.author} requested ]avatar.')
    else:
        userAvatar = username.avatar_url
        embed182 = discord.Embed(title=f'{username}\'s avatar')
        embed182.set_image(url=userAvatar)
        await ctx.send(embed = embed182)
        print(f'[log] {ctx.author} requested ]avatar.')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def spam(ctx, message: str):
    times = random.randint(0, 10)
    while times < 11:
        times = times + 1
        await ctx.send(message)
    print(f'[log] {ctx.author} requested ]spam.')

# archiescript
# encode
@bot.command(aliases=['enc'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def encode(ctx, *, text:str):
    if len(text) > 200: return
    value = 0
    arr = []
    for i in text:
        if i == "a": arr.append("+#")
        elif i == "b": arr.append("++#")
        elif i == "c": arr.append("+++#")
        elif i == "d": arr.append("++++#")
        elif i == "e": arr.append("+++++#")
        elif i == "f": arr.append("++++++#")
        elif i == "g": arr.append("+++++++#")
        elif i == "h": arr.append("++++++++#")
        elif i == "i": arr.append("+++++++++#")
        elif i == "j": arr.append("++++++++++#")
        elif i == "k": arr.append("+++++++++++#")
        elif i == "l": arr.append("++++++++++++#")
        elif i == "m": arr.append("+++++++++++++#")
        elif i == "n": arr.append("++++++++++++++#")
        elif i == "o": arr.append("+++++++++++++++#")
        elif i == "p": arr.append("++++++++++++++++#")
        elif i == "q": arr.append("+++++++++++++++++#")
        elif i == "r": arr.append("++++++++++++++++++#")
        elif i == "s": arr.append("+++++++++++++++++++#")
        elif i == "t": arr.append("++++++++++++++++++++#")
        elif i == "u": arr.append("+++++++++++++++++++++#")
        elif i == "v": arr.append("++++++++++++++++++++++#")
        elif i == "w": arr.append("+++++++++++++++++++++++#")
        elif i == "x": arr.append("++++++++++++++++++++++++#")
        elif i == "y": arr.append("+++++++++++++++++++++++++#")
        elif i == "z": arr.append("++++++++++++++++++++++++++#")
        elif i == "A": arr.append("+@")
        elif i == "B": arr.append("++@")
        elif i == "C": arr.append("+++@")
        elif i == "D": arr.append("++++@")
        elif i == "E": arr.append("+++++@")
        elif i == "F": arr.append("++++++@")
        elif i == "G": arr.append("+++++++@")
        elif i == "H": arr.append("++++++++@")
        elif i == "I": arr.append("+++++++++@")
        elif i == "J": arr.append("++++++++++@")
        elif i == "K": arr.append("+++++++++++@")
        elif i == "L": arr.append("++++++++++++@")
        elif i == "M": arr.append("+++++++++++++@")
        elif i == "N": arr.append("++++++++++++++@")
        elif i == "O": arr.append("+++++++++++++++@")
        elif i == "P": arr.append("++++++++++++++++@")
        elif i == "Q": arr.append("+++++++++++++++++@")
        elif i == "R": arr.append("++++++++++++++++++@")
        elif i == "S": arr.append("+++++++++++++++++++@")
        elif i == "T": arr.append("++++++++++++++++++++@")
        elif i == "U": arr.append("+++++++++++++++++++++@")
        elif i == "V": arr.append("++++++++++++++++++++++@")
        elif i == "W": arr.append("+++++++++++++++++++++++@")
        elif i == "X": arr.append("++++++++++++++++++++++++@")
        elif i == "Y": arr.append("+++++++++++++++++++++++++@")
        elif i == "Z": arr.append("++++++++++++++++++++++++++@")
        elif i == " ": arr.append("*")
        elif i.isdigit:
            if i == 0: arr.append("!&")
            else:
                var = "+"*int(i) + "&!"
                arr.append(var)
    arr.append(".;")
    var = ''.join(arr)
    await ctx.reply(f"`{var}`")
    print(f'[log] {ctx.author} requested ]encode.')
# end of encode

# decode
@bot.command(aliases=['dec'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def decode(ctx, code: str):
    value = 0
    cmd = code
    l = []
    for i in cmd: l.append(i)
    text = []
    for c in l:
        if c == "+":
            value += 1
        elif c == "-":
            value -= 1
        elif c == ".":
            print(''.join(text))
        elif c == '#':
            if value == 1: text.append("a")
            elif value == 2: text.append("b")
            elif value == 3: text.append("c")
            elif value == 4: text.append("d")
            elif value == 5: text.append("e")
            elif value == 6: text.append("f")
            elif value == 7: text.append("g")
            elif value == 8: text.append("h")
            elif value == 9: text.append("i")
            elif value == 10: text.append("j")
            elif value == 11: text.append("k")
            elif value == 12: text.append("l")
            elif value == 13: text.append("m")
            elif value == 14: text.append("n")
            elif value == 15: text.append("o")
            elif value == 16: text.append("p")
            elif value == 17: text.append("q")
            elif value == 18: text.append("r")
            elif value == 19: text.append("s")
            elif value == 20: text.append("t")
            elif value == 21: text.append("u")
            elif value == 22: text.append("v")
            elif value == 23: text.append("w")
            elif value == 24: text.append("x")
            elif value == 25: text.append("y")
            elif value == 26: text.append("z")
            value = 0
        elif c == '@':
            if value == 1: text.append("A")
            elif value == 2: text.append("B")
            elif value == 3: text.append("C")
            elif value == 4: text.append("D")
            elif value == 5: text.append("E")
            elif value == 6: text.append("F")
            elif value == 7: text.append("G")
            elif value == 8: text.append("H")
            elif value == 9: text.append("I")
            elif value == 10: text.append("J")
            elif value == 11: text.append("K")
            elif value == 12: text.append("L")
            elif value == 13: text.append("M")
            elif value == 14: text.append("N")
            elif value == 15: text.append("O")
            elif value == 16: text.append("P")
            elif value == 17: text.append("Q")
            elif value == 18: text.append("R")
            elif value == 19: text.append("S")
            elif value == 20: text.append("T")
            elif value == 21: text.append("U")
            elif value == 22: text.append("V")
            elif value == 23: text.append("W")
            elif value == 24: text.append("X")
            elif value == 25: text.append("Y")
            elif value == 26: text.append("Z")
            value = 0
        elif c == ";":
            await ctx.send(''.join(text))
            print(f'[log] {ctx.author} requested ]decode.')
            quit()
        elif c == "*": text.append(" ")
        elif c == "!": value = 0
        elif c == "&": text.append(str(value))
# end of decode
# end of archiescript

# stroketranslate
@bot.command(aliases=['stroktrans'])
async def stroktranslate(ctx, *, strok: str):
# var
    a = ["amogus ", "are ", "arcane ", "am ", "archie ", "Arch ", "arg1 ", "apt ", "afk ", "autocorrect ", "a ", "archbot ", "autocarrot "]
    b = ["BadArgument ", "bytes ", "bot ", "but ", "beg ", "bored ", "baka ", "bye ", "bad ", "btw ", "boolean ", "bootloader ", "because ", "boot ", "balls ", "black ", "back ", "backspace ", "\\b "]
    c = ["CommandOnCooldown ", "cum ", "cat ", "cock ", "chat ", "cyan ", "cpp ", "command ", "client ", "copy ", "copyright ", "code ", "config ", "click ", "cursed ", "cursor "]
    d = ["daemon ", "dog ", "dumb ", "database ", "do ", "dood ", "directory ", "discord ", "distro ", "delete ", "deez nuts ", "dont "]
    e = ["exit ", "eat ", "easy ", "error ", "eyes ", "epic ", "evaluate ", "english "]
    f = ["fuck ", "fish ", "false ", "fucking ", "frick ", "file ", "false ", "firmware ", "find ", "fstab ", "fire ", "forkbomb ", "fucked "]
    g = ["good ", "github ", "give ", "gcc (compiler) ", "garbage ", "game ", "GNU/Linux ", "gentoo ", "guild ", "gonna ", "gay "]
    h = ["how ", "(r/TheLetter)H ", "hello ", "hub ", "head ", "header (file) ", "home ", "h4xx0r ", "hack ", "heck ", "hell "]
    i = ["InvaildArgument ", "i ", "integer ", "imposter ", "image ", "is ", "idk ", "imagine ", "im ", "install ", "int ", "in ", "init.d ", "isobot ", "import ", "ImportError "]
    j = ["json ", "java ", "javascript ", "just ", "Joe ", "join "]
    k = ["ok ", "kwargs ", "keyword ", "karma ", "kreate (because i use kde) ", "Kde ", "Kali ", "kill ", "kernel ", "kick "]
    l = ["lol ", "like ", "Linux ", "lag ", "lagging ", "lick ", "love "]
    m = ["MissingPermissions ", "MissingRequiredArgument ", "me ", "my ", "more ", "mate ", "meme ", "masterhacker ", "micro$hit ", "minecraft "]
    n = ["null ", "nuts ", "never ", "no ", "not ", "newline ", "nano (open-source garbage) ", "nexus ", "new ", "name ", "nuke ", "nitro ", "nt (kernel is bad) ", "notsniped ", "node.js ", "\\n "]
    o = ["os ", "or ", "only ", "Operating System ", "open-source ", "omg ", "of ", "openSUSE ", "offline ", "on ", "open ", "ok "]
    p = ["penis ", "people ", "prompt ", "python ", "purge ", "pacman ", "piracy ", "ping ", "problem ", "pog ", "poggers "]
    q = ["quit ", "quadratic ", "quadra "]
    r = ["reddit ", "remove ", "root ", "real ", "really ", "random ", "rip ", "rank ", "return ", "repositories ", "raise "]
    s = ["sus ", "suspicious ", "sussy ", "say ", "sudo ", "superuser ", "script ", "stroke ", "send ", "systemd ", "snipe ", "string ", "space ", "stackoverflow ", "software ", "studio ", "suck ", "snake ", "semicolon ", "shit ", "str ", "SystemExit "]
    t = ["true ", "tank ", "that ", "the ", "terminal ", "token ", "time ", "test ", "text "]
    u = ["you ", "ueventd ", "your ", "youre ", "unicode ", "use ", "user ", "undefined ", "unixporn ", "Ubuntu ", "up "]
    v = ["version ", "variable ", "very ", "void ", "visual ", "value ", "ValueError"]
    w = ["why ", "welp ", "well ", "wget ", "what ", "wtf ", "winshit ", "wait ", "word ", "windows ", "who ", "while ", "when ", "warn "]
    x = ["xorg ", "xbox "]
    y = ["why ", "you ", "your ", "youre ", "yes "]
    z = ["zip ", "zeta "]

    arr = []
    for letter in strok:
        if letter == "a": arr.append(random.choice(a))
        elif letter == "b": arr.append(random.choice(b))
        elif letter == "c": arr.append(random.choice(c))
        elif letter == "d": arr.append(random.choice(d))
        elif letter == "e": arr.append(random.choice(e))
        elif letter == "f": arr.append(random.choice(f))
        elif letter == "g": arr.append(random.choice(g))
        elif letter == "h": arr.append(random.choice(h))
        elif letter == "i": arr.append(random.choice(i))
        elif letter == "j": arr.append(random.choice(j))
        elif letter == "k": arr.append(random.choice(k))
        elif letter == "l": arr.append(random.choice(l))
        elif letter == "m": arr.append(random.choice(m))
        elif letter == "n": arr.append(random.choice(n))
        elif letter == "o": arr.append(random.choice(o))
        elif letter == "p": arr.append(random.choice(p))
        elif letter == "q": arr.append(random.choice(q))
        elif letter == "r": arr.append(random.choice(r))
        elif letter == "s": arr.append(random.choice(s))
        elif letter == "t": arr.append(random.choice(t))
        elif letter == "u": arr.append(random.choice(u))
        elif letter == "v": arr.append(random.choice(v))
        elif letter == "w": arr.append(random.choice(w))
        elif letter == "x": arr.append(random.choice(x))
        elif letter == "y": arr.append(random.choice(y))
        elif letter == "z": arr.append(random.choice(z))
        elif letter == "1": arr.append("1 ")
        elif letter == "2": arr.append("2 ")
        elif letter == "3": arr.append("3 ")
        elif letter == "4": arr.append("4 ")
        elif letter == "5": arr.append("5 ")
        elif letter == "6": arr.append("6 ")
        elif letter == "7": arr.append("7 ")
        elif letter == "8": arr.append("8 ")
        elif letter == "9": arr.append("9 ")
        elif letter == "0": arr.append("0 ")
        elif letter == " ": arr.append("{space} ")
        elif letter == "~": arr.append("{tilde} ")
        elif letter == "`": arr.append("{acute} ")
        elif letter == "!": arr.append("{exclamation_mark} ")
        elif letter == "@": arr.append("{at} ")
        elif letter == "#": arr.append("{sharp} ")
        elif letter == "$": arr.append("{dollar_sign} ")
        elif letter == "%": arr.append("{percent} ")
        elif letter == "^": arr.append("{caret} ")
        elif letter == "*": arr.append("{asterisk} ")
        elif letter == "(": arr.append("{open_parenthesis} ")
        elif letter == ")": arr.append("{close_parenthesis} ")
        elif letter == "_": arr.append("{underscore} ")
        elif letter == "-": arr.append("{hyphen} ")
        elif letter == "+": arr.append("{plus_sign} ")
        elif letter == "=": arr.append("{equal_sign} ")
        elif letter == "{": arr.append("{open_curly_bracket} ")
        elif letter == "}": arr.append("{close_curly_bracket} ")
        elif letter == "[": arr.append("{open_bracket} ")
        elif letter == "]": arr.append("{close_bracket} ")
        elif letter == "|": arr.append("{vertical_bar} ")
        elif letter == "\\": arr.append("{backslash} ")
        elif letter == "/": arr.append("{slash} ")
        elif letter == ":": arr.append("{colon} ")
        elif letter == ";": arr.append("{semicolon} ")
        elif letter == "\"": arr.append("{quote} ")
        elif letter == "\'": arr.append("{apostrophe} ")
        elif letter == "<": arr.append("{left_angle_bracket} ")
        elif letter == ">": arr.append("{right_angle_bracket} ")
        elif letter == ",": arr.append("{comma} ")
        elif letter == ".": arr.append("{dot} ")
        elif letter == "?": arr.append("{question_mark} ")

    var = ''.join(arr)
    await ctx.reply(f"{var}")
    print(f'[log] {ctx.author} requested ]stroktranslate.')

@bot.command(name="reddit")
async def _reddit(ctx, sub:str):
    nsfw = [
        "porn",
        "sex",
        "nude",
        "nudes",
        "cock",
        "penis",
        "nsfw", 
        "cum"
    ]
    whitelist = [
          "unixporn"
    ]

    if any(x in sub.lower() for x in nsfw):
        if any(x in sub.lower() for x in whitelist): pass
        else: 
            await ctx.reply("no nsfw")
            print(f"[log] blocked an reddit command by {ctx.author}.")
            return 
    async with ctx.typing():
        try:
            submissions = reddit.subreddit(sub).hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

            embed = discord.Embed(title=submission.title)
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)
            print(f"[log] {ctx.author} requested ]reddit.")
        except Exception as e:
            await ctx.send(e)
            print(f"[log] {ctx.author} returned an error: {e}.")

# start
keep_alive()
bot.run(token)



# btw i use arch
