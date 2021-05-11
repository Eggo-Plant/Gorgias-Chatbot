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
        activity=discord.Activity(type=discord.ActivityType.playing, name="temp prefix"))
    print(bcolors.OKCYAN + "[INFO]: " + bcolors.ENDC + bcolors.OKGREEN + "Bot status set! " + bcolors.ENDC)
    print('----------------------------------------------------------------------')  # Just a hyphen seperator

@bot.command(name="chat")
async def on_message(ctx, *,message):
    author = ctx.message.author.id
    adjusted_message = message.replace(" ", "%20")
    response = requests.get(f'http://api.brainshop.ai/get?bid=156113&key=CF7GocywWwAY6Xut&uid={author}&msg={adjusted_message}').json()
    bot_response = response['cnt']
    await ctx.channel.send(bot_response)


# ---------- IMPORT TOKEN FROM ENV VARIABLE ---------- #

bot.run(os.getenv('TOKEN'))
