# ---------- PREPARE DISCORD BOT ---------- #

# Load modules and ENV Variables:
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import hashlib

intents = discord.Intents.default()
load_dotenv() # This loads the .env variables


# Declare bot prefix:
bot = commands.Bot(command_prefix="g!", description='A chat bot by Eggo-Plant', intents=intents, case_insensitive=True)


# Add coloring to logs:
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'


# ----------- INITIALIZE BOT ---------- #

# Commands to be run on boot:
@bot.event
async def on_ready():
    # Booting info:
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + bcolors.OKGREEN + bcolors.BOLD + "Successful Login! " + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + "Logged in as: " + bcolors.OKCYAN + bcolors.HEADER + bcolors.ITALIC + "{bot_username}".format(
            bot_username=bot.user.name) + bcolors.ENDC)
    print(
        bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + "Bot ID: " + bcolors.OKCYAN + bcolors.HEADER + bcolors.ITALIC + "{bot_user_id}".format(
            bot_user_id=bot.user.id) + bcolors.ENDC)

    # Set bot's status
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="Ping me with a message to talk to me!"))
    print(bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + bcolors.OKGREEN + "Bot status set! " + bcolors.ENDC)
    print('----------------------------------------------------------------------')  # Just a hyphen seperator


# ---------- BOT COMMANDS ---------- #

@bot.event
async def on_message(message):
    api_key = os.getenv('API_KEY')
    bot_id = os.getenv('BOT_ID')
    bot_mention = [f'<@{bot_id}>', f'<@!{bot_id}>', f'<@&{bot_id}>'] # Discord has symbols to indicate how the bot was mentioned, this list should cover all of them
    if message.author == bot.user: # Takes no action if the bot is the author of the message
        return
    if message.content.split()[0] in bot_mention:
        author = str(message.author.id).encode() # You can provide a unique identifier for individual users to the chatbot using any sort of UUID, I use the Discord user ID in this case
        hashed_author = (hashlib.sha256(author)).hexdigest()
        print(hashed_author)
        adjusted_message = message.content
        for i in bot_mention: # This loop removes the bot mention from the message
            adjusted_message = adjusted_message.replace(i, "")
        adjusted_message = adjusted_message.replace(" ", "%20") # Replace spaces in the user input with %20 (The escape code in URLs for spaces)
        response = requests.get(f'http://api.brainshop.ai/get?bid=156113&key={api_key}&uid={hashed_author}&msg={adjusted_message}').json()
        bot_response = response['cnt']
        await message.channel.send(bot_response)


# ---------- IMPORT TOKEN FROM ENV VARIABLE ---------- #

bot.run(os.getenv('TOKEN'))
