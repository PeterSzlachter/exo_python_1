import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv(dotenv_path="config")
token = os.getenv("TOKEN")


class PytBot(commands.Bot):

    def __init__(self):
        super().__init__(intents=intents, command_prefix="/")

        async def on_ready(self):
            print(f"{self.user.display_name} est connecté au serveur")

pbot = PytBot()
pbot.run(token)