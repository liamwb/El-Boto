import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

 
async def on_msg_del():
    with discord.on_message_delete(message) as f:
        print(f)
    


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MjE4NjQ3NDE1NjM5NTA2OTQ0.CqGhfQ.1DQ5-4GGCQaSc7VWcIEUdXuT6nI')



