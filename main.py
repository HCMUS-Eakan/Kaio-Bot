import discord
from discord.ext import commands
from private import*


bot = commands.Bot(command_prefix='$')

@bot.command()
async def hello(ctx):
	await ctx.reply('Hello!')

bot.run(TOKEN)