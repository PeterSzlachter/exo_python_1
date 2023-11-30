import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


# Le bot est-il prêt ?
@client.event
async def on_ready():
    print("le bot est prêt")


@client.event
async def on_member_join(member):
    channel_test = client.get_channel(1166651979884404786)
    await channel_test.send(content=f"Salut {member.display_name}")

# Event interaction de message
@client.event
async def on_message(message):
    if message.content.capitalize() == "Ping":
        await message.reply("Pong !")

    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages =[message async for message in message.channel.history(limit=number + 1)]
        print(messages)
        for each_message in messages:
            await each_message.delete()


client.run('MTE2NjM4ODk4NzAxMTgwNTI2NQ.GqNPKO.udlhrVwNTVMf-SnvSIIB82VOOCOEeAmnt-f_GA')
