### Modules ###
import os
import time
import praw
import math
import random
import pickle
import os.path
import discord
import datetime
import requests
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext.commands import *
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
### Modules end ###

### Startup/variables ###
ids = [
    705462972415213588,
    796097512355266602,
    821635924039434261,
    852586561610055699,
    816941773032390676,
    738290097170153472
]
bad = [
    'fuck',
    'asshole',
    'nigga',
    'motherfucker',
    'fuckyou'
]
console = False
log = True
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('Enable logging?')
print('=====================')
print('Default is True')
print('1. Yes')
print('2. No')
print('=====================')
con = int(input('Input: '))
if con == 1:
    pass
elif con == 2:
    log = not log
intents = discord.Intents.all()
errHandlerVer = 'v1.1'
botVer = 'v1.3'
currencyVer = 'v1.0'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
owner = 'NotHecker#8051'
homedir = os.path.expanduser("~")
client = commands.Bot(command_prefix=";", intents=intents)
slash = SlashCommand(client, sync_commands=True)
global startTime
startTime = time.time()
client.remove_command('help')
reddit = praw.Reddit(client_id='_pazwWZHi9JldA',
                     client_secret='1tq1HM7UMEGIro6LlwtlmQYJ1jB4vQ',
                     user_agent='idk', check_for_async=False)
### Startup/variables end ###

### Command variables ###
beg = True
fish = True
work = True
daily = True
monthly = True
weekly = True
snipe = True
edit = True
shop = True
inventory = True
buy = True
networth = True
lbin = True
ah = True
### Functions and classes ###
if os.name == 'nt':
    data_filename = homedir + "\\database.pickle"
else:
    data_filename = "/sdcard/Download/database.pickle"


class Data:
    def __init__(self, wallet, bank, xp, level, op):
        self.wallet = wallet
        self.bank = bank
        self.xp = xp
        self.level = level
        self.op = op

class colors:
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

# def consoleFunc():
#     while True:
#         cmd = input(f'{colors.cyan}[{colors.end}{colors.green}Console{colors.end}{colors.cyan}]>{colors.end}')
#         if cmd == 'shutdown':
#             conf = input('Are you sure? (y/n)')
#             if conf == 'y':
#                 # raise SystemExit
#                 exit()
#             elif conf == 'n':
#                 pass
#             else:
#                 print(f'What is {conf}')
#         elif cmd == 'clear':
#             os.system('cls')
#         elif cmd == 'viewLog':
#             os.system('notepad F:\\bot\\logs\\log.txt')
#         elif cmd == 'clearLog':
#             conf = input('Are you sure (y/n)')
#             if conf == 'y':
#                 os.system('del F:\\bot\\logs\\log.txt -f')
#                 print('Log file deleted')
#             elif conf == 'n':
#                 pass
#             else:
#                 print(f'What is {conf}')

### Functions and classes end ###

currency = True

## Events ###
@client.event
async def on_ready():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=";help"))
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f'Currency system version: {colors.cyan}{currencyVer}{colors.end}')
    print(f'Username: {colors.green}{client.user.name}{colors.end}\nId: {colors.green}{client.user.id}{colors.end}\nDeveloper name: {colors.green}{owner}{colors.end}')
    print('==================')
    print('Server list:')
    print('------------------')
    for guild in client.guilds:
        guild_owner = client.get_user(guild.owner.id)
        print(f'Server name: {colors.green}{guild.name}{colors.end}\nServer id: {colors.cyan}{guild.id}{colors.end}\nMember count: {colors.green}{guild.member_count}{colors.end}\nServer owner: {colors.cyan}{guild_owner}{colors.end}')
        print('----------------')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    print(f'Server count: {str(len(client.guilds))}')
    print('------------------')
    if bool(currency) == True:
        print(f'Currency: {colors.green}{currency}{colors.end}')
    else:
        print(f'Currency: {colors.red}{currency}{colors.end}')
    print('------------------')
    if bool(log) == True:
        print(f'Logging: {colors.green}{log}{colors.end}')
        print('------------------')
    else:
        print(f'Logging: {colors.red}{log}{colors.end}')
        print('------------------')
    if bool(console) == True:
        print(f'Console: {colors.green}{console}{colors.end}')
        print('==================')
        threading.Thread(target=consoleFunc).start()
    else:
        print(f'Console: {colors.red}{console}{colors.end}')
        print('==================')
        pass
    print('Bot admins')
    print('------------------')
    print(colors.cyan)
    for id in ids:
        print(id)
    print(colors.end)
    print('==================')
    print('System info')
    print('Running as: ' + str(os.system("whoami")))
    print('------------------')
    print('Os name: ' + str(os.name))
    print('------------------')
    print('Current working dir: ' + str(os.getcwd()))
    print('------------------')
    try:
        botpath = 'F:\\bot\\src\\bot\.py'
        botsize = os.path.getsize(botpath)
        print('Bot file size: ' + botsize)
        print('------------------')
    except FileNotFoundError:
        if os.name == 'posix':
            try:
                 print('Bot file size: ' + os.path.getsize('/sdcard/bot/bot.py'))
                 print('------------------')
            except FileNotFoundError:
                print('Bot file size: ' + os.path.getsize(str(os.getcwd() + '/bot.py')))
                print('------------------')

# Error handler #
@client.event
async def on_command_error(ctx, error):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isinstance(error, CommandNotFound):
        pass
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please try after {math.ceil(error.retry_after)} seconds')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}]Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown\n')
                f.close()
        else:
            pass
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Missing required argument(s)')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}]Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing\n')
                f.close()
        else:
            pass
    if isinstance(error, MissingPermissions):
        await ctx.send('You dont have permissions to use this')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}]Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions')
                f.close()
        else:
            pass
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument')
        if os.name == 'nt':
            with open('F:\\bot\\logs\\errors.txt', 'a') as f:
                f.write(f'[{current_time}]Ignoring exception at BadArgument')
                f.close()
        else:
            pass
    if isinstance(error, BotMissingPermissions):
        await ctx.send('I don\'t have the required permissions to use this.')
# Error handler end #

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = client.guilds[0]
    channel = message.channel
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]Message deleted by {snipe_message_author[channel.id]}.\n   Content:{snipe_message_content[channel.id]}\n')
        #     f.close()
        if message.guild.id == 876826249207640096:
            c = client.get_channel(881181406582165525)
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_message_edit(message_before, message_after):
    global author
    author = message_before.author
    guild = message_before.guild.id
    channel = message_before.channel
    global before
    before = message_before.content
    global after
    after = message_after.content
    if any(x in message_after.content.lower() for x in bad):
        await message_after.delete()
    if bool(log):
        if guild == 876826249207640096:
            c = client.get_channel(881199227190013992)
            em = discord.Embed(description = f"**Message before**: {message_before.content}\n**Message after**: {message_after.content}")
            em.set_footer(text = f"This message was edited by {message_before.author}")
            await c.send(embed = em)
        else:
            pass
    else:
        pass

@client.event
async def on_member_join(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if bool(log) == True:
        if os.name == 'nt':
            with open('F:\\bot\\logs\\log.txt', 'a') as f:
                f.write(f'[{current_time}]{member} joined {guild.name}\n')
                f.close()
        else:
            pass
    else:
        pass

@client.event
async def on_member_remove(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if bool(log) == True:
        if os.name == 'nt':
            with open('F:\\bot\\logs\\log.txt', 'a') as f:
                f.write(f'[{current_time}]{member}{colors.end} left {guild.name}\n')
                f.close()
        else:
            pass
    else:
        pass

@client.event
async def on_message(message):
    if not message.author.bot:
        member_data = load_member_data(message.author.id)
        member_data.xp += 1
        if member_data.level == 0:
            if member_data.xp >= 25:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 1:
            if member_data.xp >= 50:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 2:
            if member_data.xp >= 100:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level == 3:
            if member_data.xp >= 500:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
        elif member_data.level == 4:
            if member_data.xp >= 750:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
            else:
                pass
        elif member_data.level >= 5:
            if member_data.xp >= 1000:
                member_data.xp -= member_data.xp
                member_data.level += 1
                await message.channel.send(f"<@{message.author.id}> You leveled up to level {member_data.level}")
        else:
            pass

        save_member_data(message.author.id, member_data)
        if '<@705462972415213588>' not in message.content:
            pass
        else:
            print(f'{message.author.display_name} pinged you!\n     Content: {message.content}')
    else:
        pass
    await client.process_commands(message)

@client.event
async def on_message(message):
    if not message.author.bot:
        if any(x in message.content.lower() for x in bad):
            await message.delete()
            await message.channel.send(f'{message.author.mention} watch your language')
        else:
            pass
    else:
        pass

    await client.process_commands(message)

### Events end ###

### Commands ###
# @client.command()
# async def disable(ctx):
#     def check(msg):
#         return msg.author == ctx.message.author and (msg.content)
#     msg = await client.wait_for("message", check=check)
#     if str(msg.content) == 'testcmd':
#         test = not test
#         await ctx.send('Command testcmd has been disabled')
#         if bool(log) == True:
#             print(f'{text} command has been disabled by {ctx.message.author.display_name}')
#         else:
#             pass
#     else:
#         await ctx.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

@client.command(aliases=['goldfish'])
async def fstab(ctx):
    await ctx.reply('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

@client.command(aliases=['xp', 'level'])
async def rank(ctx, user : discord.User=None):
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        if member_data.level <= 5:
            rank = "New person"
        elif member_data.level >= 10 and member_data.level > 5:
            rank = "Active"
        elif member_data.level >= 20 and member_data.level > 10:
            rank = "Active af!!"
        if member_data.level == 0:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\25")
        elif member_data.level == 1:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\50")
        elif member_data.level == 2:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\100")
        elif member_data.level == 3:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\500")
        elif member_data.level == 4:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\750")
        elif member_data.level >= 5:
            e = discord.Embed(title=f"{ctx.message.author.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\1000")
        await ctx.send(embed=e)
    else:
        if member_data.level <= 5:
            rank = "New person"
        elif member_data.level >= 10 and member_data.level > 5:
            rank = "Active"
        elif member_data.level >= 20 and member_data.level > 10:
            rank = "Active af!!"
        member_data = load_member_data(user.id)
        if member_data.level == 0:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\25")
        elif member_data.level == 1:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\50")
        elif member_data.level == 2:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\100")
        elif member_data.level == 3:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\500")
        elif member_data.level == 4:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\750")
        elif member_data.level >= 5:
            e = discord.Embed(title=f"{user.display_name}'s xp", description=f"{rank}\nLevel: {member_data.level}\nXp: {member_data.xp}\\1000")
        await ctx.send(embed=e)

@client.command()
async def add_xp(ctx, user : discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.xp += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'{arg1} is not a number')

@client.command()
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@client.command()
async def add_lvl(ctx, user : discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.level += int(arg1)
            save_member_data(user.id, member_data)
        else:
            await ctx.reply(f'{arg1} is not a number')

@client.command()
async def invite(ctx):
    await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot")
    #await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=881092078132670484&permissions=0&scope=bot")

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')

@client.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(uptime)

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

@client.command()
async def whoAmI(ctx):
    await ctx.send(f"I am: {client.user.name}\nMy id is: {client.user.id}\nMy developer is: {owner}\nMy ping is {client.latency}ms\nYour name is: {'saneite#5077 (not my dev)' if ctx.message.author.id == 795986008680300565 else ctx.message.author}\nYour id is: {ctx.message.author.id}")

@client.command()
async def ping(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')
    if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]Bot ping is {round(client.latency * 1000)}ms\n')
        #     f.close()
        pass
    else:
        return

@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(title='**COMMAND LIST**', description='Economy\nBeg, bal, hunt, daily, weekly, monthly, postmeme\n\nModeration\nban, kick, nuke\n\nMisc\n8ball, meme, softwaregore')
    await ctx.send(embed = helpEmbed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
            "no?????.",
            "when you grow a braincell, yes",
            "you stupid, of course not",
            "lol no",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "try again",
            "ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good."
  ]
  ballEmbed= discord.Embed(title=f'{question}', description=f'{random.choice(responses)}')
  await ctx.send(embed=ballEmbed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("This channel has been nuked!")
        await ctx.send("Nuked the Channel sucessfully!")
        if bool(log) == True:
            # with open('F:\\bot\\logs\\log.txt', 'a') as f:
            #     f.write(f'[{current_time}]{ctx.message.author.display_name}nuked{nuke_channel}\n')
            #     f.close()
            print(f'[{current_time}]{ctx.message.author.display_name} nuked {nuke_channel}')
        else:
            pass
    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@client.command()
async def invites(ctx, *, user : discord.User=None):
    totalInvites = 0
    if user == None:
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        e = discord.Embed(title=f'{ctx.message.author.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
        await ctx.reply(embed=e)
    elif user.bot:
        await ctx.reply('This is a bot not a user')
        return
    else:
        for i in await ctx.guild.invites():
            if i.inviter == user:
                totalInvites += i.uses
        e = discord.Embed(title=f'{user.display_name}\'s total invites', description=f"{totalInvites} invite{'' if totalInvites == 1 else 's'}")
        await ctx.reply(embed=e)

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@client.command()
async def ihadastroke(ctx):
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@client.command()
async def shutdown(ctx):
    if ctx.message.author.id == 705462972415213588:
        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
        
        await ctx.send('You sure?')
        msg = await client.wait_for("message", check=check)
        if msg.content == 'y' or msg.content == 'yes':
            await ctx.send('Shutting down the bot...')
            time.sleep(0.5)
            raise SystemExit('Bot shutdown')
        elif msg.content == 'n' or msg.content == 'no':
            await ctx.send('ok')
        else:
            await ctx.send(f'What is {msg.content}? You are supposed to reply with yes or no')
    else:
        await ctx.send(f'101% that this command doesn\'t exist :eyes:')

@client.command(aliases=['hl'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def highlow(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    numb = randint(1, 100)
    numb2 = randint(1, 100)
    id = ctx.message.author.id
    coins = randint(300, 1000)
    member_data = load_member_data(id)

    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)

    await ctx.send(f'Your number is {numb} choose if the other is lower, higher or jackpot')
    msg = await client.wait_for("message", check=check)
    if msg.content == 'low':
        if numb > numb2:
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
            member_data.wallet += coins
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins\n')
                    #     f.close()
                print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
            else:
                pass
        elif numb < numb2:
            await ctx.send(f'Incorrect the number was {numb2}')
        elif numb == numb2:
            await ctx.send(f'You stupid you could won 1 mil coins if you choose jackpot')
    if msg.content == 'jackpot':
        if numb == numb2:
            coins2 = randint(1000000, 5000000)
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins2} coins gg!')
            member_data = load_member_data(id)
            member_data.wallet += coins2
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}]{ctx.message.author.display_name} earned {coins2} coins\n')
                    #     f.close()
                print(f'[{current_time}]{ctx.message.author.display_name} earned {coins2} coins')
            else:
                pass
        else:
            await ctx.send(f'Incorrect the number was {numb2}')
    if msg.content == 'high':
        if numb < numb2:
            await ctx.send(f'Congrats, your number was {numb2} and you earned {coins} coins')
            member_data = load_member_data(id)
            member_data.wallet += coins
            save_member_data(id, member_data)
            if bool(log) == True:
                    # with open('F:\\bot\\logs\\log.txt', 'a') as f:
                    #     f.write(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins\n')
                    #     f.close()
                print(f'[{current_time}]{ctx.message.author.display_name} earned {coins} coins')
            else:
                pass
        else:
            await ctx.send(f'Incorrect your number was {numb2}')
    else:
        await ctx.send(f'{msg.content} is not an option')

@client.command()
async def kill(ctx, user : discord.User):
    if user == None:
        await ctx.send('Please tag someone to kill')
    elif user.id == ctx.message.author.id:
        await ctx.send('Ok you are dead, please tag someone else to kill')
    else:
        responses2 = [
            f"<@{user.id}> died from a dang baguette",
            f"<@{ctx.message.author.id}> strikes <@{user.id}> with the killing curse... *Avada Kedavra!*",
            f"<@{user.id}> dies from dabbing too hard",
            f"<@{user.id}> ripped their own heart out to show their love for <@{ctx.message.author.id}>"
        ]
        await ctx.send(f'{random.choice(responses2)}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, *, member : discord.Member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        raise BadArgument
    else:
        await member.kick()
    await ctx.send(f'{member} has been kicked from the server')
    if bool(log) == True:
        # with open('F:\\bot\\logs\\log.txt', 'a') as f:
        #     f.write(f'[{current_time}]{ctx.message.author.display_name} kicked {member} from {ctx.message.guild.name}')
        #     f.close()
        print(f'[{current_time}]{ctx.message.author.display_name} kicked {member.display_name} from {ctx.message.guild.name}')
    else:
        pass

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, *, member=discord.Member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        raise BadArgument
    else:
        await member.ban()
        await ctx.send(f'{member} has been banned from the server')
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} banned {member.display_name} from {ctx.message.guild.name}')
        else:
            pass 

@client.command()
async def slap(ctx, user : discord.User):
    responses3 = [
        "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
        "https://cdn.weeb.sh/images/SJlkNkFwb.gif",
        "https://cdn.weeb.sh/images/rJ4141YDZ.gif",
        "https://cdn.weeb.sh/images/HJKiX1tPW.gif"
    ]
    e = discord.Embed(title=f'{ctx.message.author} slaps {user}')
    e.set_image(url=f'{random.choice(responses3)}')
    await ctx.send(embed = e)

@client.command(aliases=['sg'])
async def softwaregore(ctx):
    sg_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sg_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def guess(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    if int(member_data.wallet) >= value:
        await ctx.reply(f'You have reached max value for your wallet ({value})')
        return
    else:
        pass
    await message.channel.send('Guess a number from 1 to 10')

    def check(msg):
        return msg.author == message.author and msg.channel == message.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == x:
        coins = randint(1, 100)
        await message.channel.send(f"Correct, you earned {coins} coins")
        member_data.wallet += coins
        save_member_data(message.author.id, member_data)
    else:
        await message.channel.send(f"Nope it was {x}")

@client.command(aliases=['sus'])
async def isSus(ctx, *, user : discord.User):
    susvar = [
        True,
        False
    ]
    sus = random.choice(susvar)
    if bool(sus) == True:
        await ctx.send(f'{user.mention} is very sus')
    elif bool(sus) == False:
        await ctx.send(f'{user.mention} isn\'t sus')
    else:
        await ctx.reply('undefined')

@client.command(aliases=['pm'])
@commands.cooldown(1, 40, commands.BucketType.user)
async def postmeme(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)
    if int(member_data.wallet) >= value:
        await ctx.reply(f'You have reached max value for your wallet ({value})')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'{ctx.message.author.mention} What type of meme you want to post?\n`f` Fresh meme\n`d` Dank meme\n`c` Copypasta\n*more comming soon*')

    def check(msg):
        return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content) in ['f', 'd', 'c']
    
    msg = await client.wait_for("message", check=check)

    x = randint(0, 200)
    if x == 0:
        await ctx.send(f'{ctx.message.author.mention} You earned 0 coins xD')
    else:
        await ctx.send(f'You earned {x} coins')
        member_data.wallet += x
        save_member_data(id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} has earned {colors.green}{x}{colors.end} coins')
        else:
            pass

@client.command()
async def null(ctx):
    await ctx.reply('You got **null** coins dood.')

@client.command(aliases=['gift'])
async def give(ctx, user : discord.User, *, arg1):
    if user.id == ctx.message.author.id:
        await ctx.reply('You can\'t give coins to yourself')
        return
    else:
        if arg1.isdigit:
            member_data = load_member_data(ctx.message.author.id)
            if member_data.wallet < int(arg1):
                await ctx.reply('You don\'t have that many coins in your wallet')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me **dood**')
            elif int(arg1) == 0:
                await ctx.reply('You can\'t gift 0 coins')
            else:
                member_data.wallet -= int(arg1)
                save_member_data(ctx.message.author.id, member_data)
                user_data = load_member_data(user.id)
                user_data.wallet += int(arg1)
                save_member_data(user.id, user_data)
                await ctx.reply(f'You gave {arg1} coins to {user.display_name}')
        else:
            await ctx.reply(f'{arg1} is not a digit **dood**')

@client.command()
async def add(ctx, user : discord.User, *, arg1=None):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'101% sure that this command doesn\'t exist :eyes:')
        return
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if arg1.startswith('0x') or arg1.startswith('-0x'):
            try:
                hexv = int(f'{arg1}', 16)
                member_data = load_member_data(user.id)
                member_data.wallet += int(hexv)
                save_member_data(user.id, member_data)
                await ctx.send(f'Added {hexv} coins to {user.display_name}\'s account')
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{hexv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send(f'Invalid hex value')
        elif arg1.startswith('0b') or arg1.startswith('-0b'):
            try:
                binv = int(f'{arg1}', 2)
                member_data = load_member_data(user.id)
                member_data.wallet += int(binv)
                save_member_data(user.id, member_data)
                await ctx.send(f'Added {binv} coins to {user.display_name}\'s account')
                print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{binv}{colors.end} coins to {colors.cyan}{user.display_name}\'s{colors.end} account')
            except ValueError:
                await ctx.send('Invalid binary value')
        elif arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.wallet += int(arg1)
            save_member_data(user.id, member_data)
            await ctx.send(f'Added {arg1} coins to {user.display_name}\'s account')
            if bool(log) == True:
                print(f"[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} added {colors.green}{arg1}{colors.end} coins to {colors.cyan}{user.display_name}{colors.end}\'s account")
            else:
                pass
        elif arg1 == None:
            await ctx.reply('Usage: `;add <user> binary\\hex\\decimal`')
            return
        else:
            await ctx.send('Invalid value.')
        

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def work(ctx):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1000, 25000)
    member_data.wallet += coins
    await ctx.send(f"You earned {coins} coins.")
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
    else:
        pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(1, 500)
    if int(member_data.wallet) >= value:
        await ctx.reply(f'You reached max wallet value. ({value})')
        return
    else:
        member_data.wallet += coins
        await ctx.send(f'You earned {coins} coins.')

        save_member_data(ctx.message.author.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} coins')
        else:
            pass

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    if bool(currency) == False:
        await ctx.reply('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    member_data = load_member_data(message.author.id)
    member_data.wallet += 10000
    await ctx.send('You claimed 10,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}]{ctx.message.author.display_name} claimed 10k coins from daily command')
    else:
        pass

@client.command()
async def fish(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    items = [
        "nothing",
        "fish",
        "rare fish"
    ]
    item = random.choice(items)
    if item == 'nothing':
        await message.channel.send('You got nothing XD')
    elif item == 'fish':
        await message.channel.send(f'You caught a fish and sold it for 100 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 100
        save_member_data(message.author.id, member_data)
    elif item == 'rare fish':
        member_data = load_member_data(message.author.id)
        await message.channel.send(f'You caught a rare fish and sold it for 300 coins')
        member_data.wallet += 300
        save_member_data(message.author.id, member_data)

@client.command(aliases=['dep'])
async def deposit(ctx, *, arg1):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.wallet == 0:
                await ctx.send('You don\'t have any coins in your wallet')
                return
            else:
                if member_data.wallet == 1:
                    await ctx.reply(f'You deposited {member_data.wallet} coin')
                else:
                    await ctx.reply(f'You deposited {member_data.wallet} coins')    
                member_data.bank += int(member_data.wallet)
                member_data.wallet -= int(member_data.wallet)
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.wallet:
                await ctx.reply('You don\'t have that many coins in your wallet')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.send(f'You deposited {arg1} coins')
                member_data.wallet -= int(arg1)
                member_data.bank += int(arg1)
                save_member_data(ctx.message.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command(aliases=['with'])
async def withdraw(ctx, *, arg1):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        member_data = load_member_data(ctx.message.author.id)
        if arg1 == 'all' or arg1 == 'max':
            if member_data.bank == 0:
                await ctx.send('You don\'t have any coins in your bank')
                return
            else:
                if member_data.bank == 1:
                    await ctx.reply(f'You withdrawn {member_data.bank} coin')
                else:
                    await ctx.reply(f'You withdrawn {member_data.bank} coins')    
                member_data.wallet += int(member_data.bank)
                member_data.bank -= int(member_data.bank)
                save_member_data(ctx.message.author.id, member_data)
                return
        elif arg1.isdigit:
            if int(arg1) > member_data.bank:
                await ctx.reply('You don\'t have that many coins in your bank')
                return
            elif int(arg1) < 0:
                await ctx.reply('Don\'t try to break me dood')
                return
            else:
                await ctx.send(f'You withdrawn {arg1} coins')
                member_data.wallet += int(arg1)
                member_data.bank -= int(arg1)
                save_member_data(ctx.message.author.id, member_data)
                return
        else:
            raise BadArgument

@client.command()
async def rob(ctx, *, user : discord.User):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if ctx.message.author.id == user.id:
        await ctx.send('you cant rob yourself xd')
        return
    elif user.id == 705462972415213588:
        await ctx.send('You can\'t rob the bot developer')
        return
    else:
        vic_data = load_member_data(user.id)
        if vic_data.wallet < 500:
            save_member_data(user.id, vic_data)
            await ctx.send('This user has less than 500 coins')
        elif vic_data.wallet >= 500:
            coins = randint(500, vic_data.wallet)
            if bool(log) == True:
                print(f'[{current_time}]{ctx.message.author.display_name} stole {coins} coins from {user.display_name}')
            else:
                pass
            vic_data.wallet -= coins
            save_member_data(user.id, vic_data)
            member_data = load_member_data(ctx.message.author.id)
            member_data.wallet += coins
            save_member_data(ctx.message.author.id, member_data)
            await ctx.send(f'You stole {coins} coins from **{user.display_name}**')

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hunt(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    items = [
        "nothing",
        "skunk",
        "boar",
        "dragon",
        "died"
    ]
    item = random.choice(items)
    if item == 'nothing':
        await message.channel.send('You got nothing XD')
    elif item == 'skunk':
        await message.channel.send('You went for hunting and got a skunk. You sold it and earned 200 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 200
        save_member_data(message.author.id, member_data)
    elif item == 'boar':
        await message.channel.send('You went for hunting and got a boar. You sold it and earned 500 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 500
        save_member_data(message.author.id, member_data)
    elif item == 'dragon':
        await message.channel.send('You went for hunting and got a dragon wtf. You sold it and earned 5000 coins')
        member_data = load_member_data(message.author.id)
        member_data.wallet += 5000
        save_member_data(message.author.id, member_data)
    elif item == 'died':
        await message.channel.send('You went for hunting but you died. You lost 420 coins.')
        member_data = load_member_data(message.author.id)
        member_data.wallet -= 420
        save_member_data(message.author.id, member_data)

@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(message.author.id)
    member_data.wallet += 50000
    await message.channel.send('You claimed 50,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}]{message.author.display_name} claimed 50k coins from weekly command')
    else:
        pass

@client.command()
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthly(message):
    if bool(currency) == False:
        await message.channel.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(message.author.id)
    member_data.wallet += 100000
    await message.channel.send('You claimed 100,000 coins')
    save_member_data(message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}]{message.author.display_name} claimed 100k coins from monthly command')
    else:
        pass

@client.command()
async def dev_claim(message):
    if message.author.id == 705462972415213588:
        member_data = load_member_data(message.author.id)
        member_data.wallet += 69420
        await message.channel.send('You claimed 69,420 coins :sunglasses:')
        save_member_data(message.author.id, member_data)
    elif message.author.id == 795986008680300565:
        member_data = load_member_data(message.author.id)
        member_data.wallet += 69
        await message.channel.send('You claimed 69 coins')
        save_member_data(message.author.id, member_data)
    else:
        await message.channel.send('Are you bot developer?')

@client.command()
async def wipe_user(ctx, *, user : discord.User):
    if ctx.message.author.id == 705462972415213588:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        member_data = load_member_data(user.id)
        member_data.wallet -= member_data.wallet
        member_data.bank -= member_data.bank
        await ctx.send(f"Wiped {user}'s account")
        save_member_data(user.id, member_data)
        if bool(log) == True:
            print(f'[{current_time}]{ctx.message.author.display_name} wiped {user.display_name}\'s profile')
        else:
            pass
    else:
        await ctx.send('I dont think you are my dev')

@client.command(aliases=['bal'])
async def balance(ctx, user : discord.User=None):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.message.author.id)

        embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance")
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)

        embed = discord.Embed(title=f"{user.display_name}'s Balance")
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)

@client.command(aliases=['inv'])
async def inventory(ctx):
    await ctx.reply(f'this command is disabled')
    returns
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    member_data = load_member_data(ctx.message.author.id)

    e = discord.Embed(title=f"{ctx.message.author.display_name}'s Inventory", description=f'op item\n{member_data.op}')
    await ctx.send(embed=e)

@client.command()
async def shop(ctx):
    await ctx.reply(f'this command is disabled')
    return
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    e = discord.Embed(title='Shop', description="**Items:\nop item: 69,420 coins\nid: `op`") #will edit later
    await ctx.send(embed=e)

@client.command()
async def buy(ctx, *, arg1):
    if bool(currency) == False:
        await ctx.send('Currency is disabled')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if str(arg1) == 'op':
        member_data = load_member_data(ctx.message.author.id)
        if member_data.wallet < 69420:
            await ctx.send('You don\'t have 69,420 coins to buy this')
        else:
            member_data.wallet -= 69420
            member_data.op += 1
            save_member_data(ctx.message.author.id, member_data)
            await ctx.send(f'You bought 1 {msg.content}')
            if bool(log) == True:
                print(f'[{current_time}]{ctx.message.author.display_name} bought 1 {msg.content} from shop')
            else:
                pass
    elif str(arg1) == 'rich_person':
        member_data = load_member_data(ctx.message.author.id)
        if member_data_wallet < 1000000:
            await ctx.reply('You don\'t have enough coins in your wallet to buy this')
            return
        elif "rich person" in ctx.message.author.roles:
            await ctx.reply('You already bought this')
            return
        else:
            member_data.wallet -= 1000000
            save_member_data(ctx.message.author.id, member_data)
            await ctx.message.author.add_roles("rich person")
            await ctx.reply('You bought the role \'rich person\' for 1,000,000 coins')
    else:
        await ctx.send(f's')

@client.command(aliases=["lm"])
async def linuxmeme(ctx):
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

#hypixel skyblock api key: e7ca6250-5641-4e3e-ab5d-6e6c90502273
@client.command(aliases=["nw"])
async def networth(ctx, *, arg1, arg2=None):
    if arg2 == None:
        url = f'https://nariah-dev.com/api/networth/total/{arg1}/?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            total = jsonr["total"]
            e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
            await ctx.send(embed=e)
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        elif r.status_code == 404:
            jsonr = r.json()
            cause = jsonr["cause"]
            await ctx.reply(f'Error\nStatus code: {r.status_code}\nCause: {cause}')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to NotHecker#0001')
    else:
        url = f'https://nariah-dev.com/api/networth/total/{arg1}/{arg2}?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
        r = requests.get(url)
        if r.status_code == 200:
            r.raise_for_status()
            jsonr = r.json()
            total = jsonr["total"]
            e = discord.Embed(title=f'{arg1}\'s Hypixel Skyblock networth', description=f'{total} coins')
            e.set_footer(text=f'Profile: {arg2}')
            await ctx.send(embed=e)
        elif r.status_code == 500:
            await ctx.reply('An internal error occured')
        elif r.status_code == 404:
            await ctx.reply('Invalid username or profile')
        else:
            await ctx.reply(f'Undefined status code: {r.status_code}\ndm this to NotHecker#0001')

@client.command(aliases=['ah'])
async def auctionhouse(ctx, *, arg1):
    url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        # data of jsonr["data"]
        average = data["average"] #average price of an item
        minimum = data["min"] #minimum price of an item
        maximum = data["max"] #maximum price of an item
        item = arg1.replace("_", " ")
        e = discord.Embed(title=f'Auction house stats for {item}', description=f'Average price: {average}\nLowest price: {minimum}\nHighest price: {maximum}')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.reply(f'No such item ({id})')
    elif r.status_code == 500:
        await ctx.reply('An internal error occured')
    else:
        await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to NotHecker#0001') #possible status codes: 400, bad request

@client.command()
async def lbin(ctx, *, arg1):
    url = f'https://nariah-dev.com/api/auctions/statistics/{arg1}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        lbin = data["min"]
        item = arg1.replace("_", " ")
        e = discord.Embed(title=f'Lowest BIN for {item}', description=f'{lbin} coins')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.reply(f'No such item ({arg1})')
    elif r.status_code == 500:
        await ctx.reply('An internal error occured')
    else:
        await ctx.reply(f'Undefined status code: {r.status_code}\nsend this to NotHecker#0001')

@client.command()
async def tempadmin(ctx, user : discord.User, arg1):
    if ctx.message.author.id == 705462972415213588:
        if arg1 == 'add':
            if user.id not in ids:
                ids.append(user.id)
                await ctx.reply(f'**{user.display_name}** is now a bot admin for this session')
            else:
                await ctx.reply(f'**{user.display_name}** is already a bot admin')
        elif arg1 == 'remove' or 'delete':
            if user.id not in ids:
                await ctx.reply(f'**{user.display_name}** is not a bot admin')
                return
            else:
                ids.remove(user.id)
                await ctx.reply(f'{user.display_name} is not a bot admin anymore')
    else:
        await ctx.reply('i am 101%% sure that this command doesn\'t exist :eyes:')
### Commands end ###        

### Slash commands ###
# option types:
# sub command: 1
# sub command group: 2
# string: 3
# int: 4
# bool: 5
# user: 6
# channel: 7
# role: 8
@slash.slash(name="snipe", description="Shows the most recent deleted message")
async def snipe(ctx: SlashContext):
    channel = ctx.channel
    try:
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except:
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

@slash.slash(
    name="balance",
    description="Shows the money amount of a user",
    options=[
        create_option(
            name="user",
            description="Select a user",
            option_type=6,
            required=False
        )
    ]
)
async def balance(ctx: SlashContext, user:str):
    if user == None:
        member_data = load_member_data(ctx.message.author.id)

        embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Balance")
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)

        embed = discord.Embed(title=f"{user.display_name}'s Balance")
        embed.add_field(name="Wallet", value=str(member_data.wallet))
        embed.add_field(name="Bank", value=str(member_data.bank))
        embed.set_footer(text=f'Currency api made by {owner}')
        await ctx.send(embed=embed)

@slash.slash(
    name="edit",
    description="Shows the most recent edited message"
)
async def edit(ctx: SlashContext):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}')
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
    except:
        await ctx.reply('No recent edited messages here :eyes:')

@slash.slash(
    name="say",
    description="null",
    options=[
        create_option(
            name="text",
            description="null",
            option_type=3,
            required=True
        )
    ]
)
async def say(ctx: SlashContext, text:str):
    await ctx.send(text)

@slash.slash(
    name="sus",
    description="tells if a user is sus",
    options=[
        create_option(
            name="user",
            description="is sus user",
            option_type=6,
            required=True
        )
    ]
)
async def sus(ctx: SlashContext, user:str):
    susbool = [
        True,
        False
    ]
    isSus = random.choice(susbool)
    if isSus == True:
        await ctx.send(f'{user.mention} is very sus')
    else:
        await ctx.send(f'{user.mention} isn\'t sus')

@slash.slash(
    name="fstab",
    description="fstab.goldfish"
)
async def fstab(ctx: SlashContext):
    await ctx.send('https://cdn.discordapp.com/attachments/878297190576062515/879845618636423259/IMG_20210825_005111.jpg')

@slash.slash(
    name="ping",
    description="shows bot ping",
)
async def ping(ctx: SlashContext):
    await ctx.send(f'Pong! My ping is {round(client.latency * 1000)}ms')

@slash.slash(
    name="meme",
    description="sends a meme from r/memes"
)
async def meme(ctx: SlashContext):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@slash.slash(
    name="softwaregore",
    description="sends a random image from r/softwaregore"
)
async def softwaregore(ctx: SlashContext):
    memes_submissions = reddit.subreddit('softwaregore').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@slash.slash(
    name="ihadastroke",
    description="sends a random image from r/ihadastroke"
)
async def ihadastroke(ctx: SlashContext):
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@slash.slash(
    name="invite",
    description="sends invite of bot"
)
async def invite(ctx: SlashContext):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=859869941535997972&permissions=8&scope=bot")

@slash.slash(
    name="uptime",
    description="shows bot uptime"
)
async def uptime(ctx: SlashContext):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(uptime)

@slash.slash(
    name="null",
    description="null"
)
async def null(ctx: SlashContext):
    await ctx.send("You got __null__ coins **dood**")

@slash.slash(
    name="networth",
    description="shows the networth of a user",
    options=[
        create_option(
            name="username",
            description="show networth of a player",
            option_type=3,
            required=True
        )
    ]
)
async def networth(ctx: SlashContext, username:str):
	url = f'https://nariah-dev.com/api/networth/total/{username}/?key=e7ca6250-5641-4e3e-ab5d-6e6c90502273'
	r = requests.get(url)
	if r.status_code == 200:
	 	  r.raise_for_status()      
	 	  jsonr = r.json()
	 	  total = jsonr["total"]
	 	  e = discord.Embed(title=f'{username}\'s Hypixel Skyblock networth', description=f'{total} coins')
	 	  await ctx.send(embed=e)
	elif r.status_code == 500:
	    await ctx.send('An internal error occured')
	elif r.status_code == 404:
         jsonr = r.json()
         cause = jsonr["cause"]
         await ctx.send(f'Error\nStatus code: {r.status_code}\nCause: {cause}')
	else:
		await ctx.send(f'Undefined status code: {r.status_code}\ndm this to NotHecker#0001')

@slash.slash(
	name="auction",
	description="shows the auction house stats for an item",
	options=[
        create_option(
            name="item id",
            description="item id",
            option_type=3,
            required=True
		)
	]
)
async def auction(ctx: SlashContext, id:str):
    url = f'https://nariah-dev.com/api/auctions/statistics/{id}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        # data of jsonr["data"]
        average = data["average"]
        minimum = data["min"]
        maximum = data["max"]
        newstring = id.replace("_", " ")
        e = discord.Embed(title=f'Auction house stats for {newstring}', description=f'Average price: {average}\nLowest price: {minimum}\nHighest price: {maximum}')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.send(f'No such item ({id})')
    elif r.status_code == 500:
        await ctx.send('An internal error occured')
    else:
        await ctx.send(f'Undefined status code: {r.status_code}\ndm this to NotHecker#0001')

@slash.slash(
    name="linuxmeme",
    description="sends a random image from r/linuxmemes"
)
async def linuxmeme(ctx: SlashContext):
    memes_submissions = reddit.subreddit('linuxmemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title = submission.title)
    embed.set_image(url=submission.url)
    await ctx.send(embed = embed)

@slash.slash(
    name="lbin",
    description="shows the lowest BIN price of an item",
    options=[
        create_option(
            name="item id",
            description="item id",
            option_type=3,
            required=True
		)
	]
)
async def lbin(ctx, id:str):
    url = f'https://nariah-dev.com/api/auctions/statistics/{id}'
    r = requests.get(url)
    if r.status_code == 200:
        r.raise_for_status()
        jsonr = r.json()
        data = jsonr["data"]
        lbin = data["min"]
        item = id.replace("_", " ")
        e = discord.Embed(title=f'Lowest BIN for {item}', description=f'{lbin} coins')
        await ctx.send(embed=e)
    elif r.status_code == 404:
        await ctx.send(f'No such item ({id})')
    elif r.status_code == 500:
        await ctx.send('An internal error occured')
    else:
        await ctx.send(f'Undefined status code: {r.status_code}\nsend this to NotHecker#0001')
