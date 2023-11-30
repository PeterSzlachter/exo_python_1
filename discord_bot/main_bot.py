from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("le bot est prêt")


@bot.command(name="del")
async def delete(ctx, number_of_messages: int):
    messages = [message async for message in ctx.channel.history(limit=number_of_messages + 1)]

    for each_message in messages:
        await each_message.delete()

bot.run(token)