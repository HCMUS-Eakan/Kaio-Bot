import discord
import OS
client = discord.Client()
@client.event

async def on_ready():
	print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startwith('kHello'):
		await message.channel.send('Hello')

client.run(os.getenv('TOKEN'))