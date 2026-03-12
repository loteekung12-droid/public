import discord
from discord import app_commands
from discord.ext import commands
import requests

from config import token, apikey

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is running and synced")

@bot.tree.command(name="iplookup", description="lookup ip address")
@app_commands.describe(user_input="enter ip address")

async def ip_lookup(interaction: discord.Interaction, user_input: str):

    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={apikey}&ip={user_input}"
    response = requests.get(url)
    data = response.json()

    await interaction.response.send_message(
        f"IP: {data['ip']}\nCountry: {data['country_name']}\nISP: {data['isp']}"
    )

bot.run(token)
