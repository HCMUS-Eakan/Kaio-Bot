import discord
from discord.ext import commands
from private import*
import random
import json
import time

def get_prefix(client, message): ##first we define get_prefix
    with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f) #load the json as prefixes
    return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given

client = commands.Bot(command_prefix = (get_prefix), case_insensitive=True)

@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '$'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


#Greeting commands
@client.command(aliases=['Hi', 'Chao', 'Chào', 'Ê', 'Hú'])
async def hello(ctx):
	messages = ['Hello UwU', 'Hi :)', 'Chào à!', 'Gì?!', 'Cái gì mày?', 'Alo tui nghe nè!', 'Muốn gì?', 'Cắn mày giờ chứ kêu.']
	await ctx.reply(random.choice(messages))# + ctx.author.name + '!')


#Changing prefix
@client.command(aliases=['cp', 'change'], pass_context=True)
@commands.has_permissions(administrator=True) #ensure that only administrators can use this command
async def set_prefix(ctx, prefix): #command: $set_prefix ...
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}') #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname
    # name=f'{prefix}BotBot'

@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    #await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

client.run(TOKEN)