# Imports
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import 56010f8cb62c4007995b3417edac68e4

# Bot Configuration
intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='/')

#Sync
@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Bot is running and has synced.')

# Establish Command Name and Description 
@bot.tree.command(name='ip lookup', description='my ip ดักพวกกระจอก')

# Bot Prompt, API Call, and Response Functionality
@app_commands.describe(user_input = "please enter ip addres: ")                 # Prompt User for Input
async def Ip_Lookup(interaction: discord.Interaction, user_input: str):                 

    # Use Requests to Obtain Data from API
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey{apikey}&ip={user_input}'
    response = requests.get(url)
    json_response = response.json()

    # Send Message Containing Requested Data to User
    await interaction.response.send_message(f'IP: {json response["IP"]}\nCountry: {json response["country name"]}\isp: {json response["isp"]}', ephemeral=True)
    return

bot.run(token) # Run Bot
