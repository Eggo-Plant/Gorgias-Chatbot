# ---------- PREPARE DISCORD BOT ---------- #

# Load modules and ENV Variables:
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests

intents = discord.Intents.default()
load_dotenv()


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
    bot_id = ['<@841383624296497222>', '<@!841383624296497222>', '<@&841383624296497222>']
    if message.author == bot.user:
        return
    if message.content.split()[0] in bot_id:
        author = message.author.id
        adjusted_message = message.content
        for i in bot_id:
            adjusted_message = adjusted_message.replace(i, "")
        adjusted_message = adjusted_message.replace(" ", "%20")
        response = requests.get(f'http://api.brainshop.ai/get?bid=156113&key={api_key}&uid={author}&msg={adjusted_message}').json()
        bot_response = response['cnt']
        await message.channel.send(bot_response)


# ---------- IMPORT TOKEN FROM ENV VARIABLE ---------- #

bot.run(os.getenv('TOKEN'))
