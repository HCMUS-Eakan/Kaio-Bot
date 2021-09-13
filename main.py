import discord
from discord.ext import commands
from private import*
import random

bot = commands.Bot(command_prefix='x', case_insensitive=True)

#Greeting commands
@bot.command(aliases=['Hi', 'Chao', 'Chào', 'Ê', 'Hú'])
async def hello(ctx):
	messages = ['Hello UwU', 'Hi :)', 'Chào à!', 'Gì?!', 'Cái gì mày?', 'Alo tui nghe nè!', 'Muốn gì?', 'Cắn mày giờ chứ kêu.']
	await ctx.reply(random.choice(messages))# + ctx.author.name + '!')

bot.run(TOKEN)