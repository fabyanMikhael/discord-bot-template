###############################
'''this loads the "DISCORD_TOKEN" string from the .env file'''

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"] #grabs the token after loading it with load_dotenv()
if TOKEN == "PASTE_TOKEN_HERE":
    print("Must add your own discord token in .env file!")
    exit()
###############################

import discord

from discord.ext import commands

intents = discord.Intents.all() # will require all intents by default, change this to match your bot's intents

bot = commands.Bot(
                    command_prefix="$",
                    intents=intents,
                    #help_command=None # <- uncomment this if you want to write your own help command
                    )

@bot.event # @bot.event attaches the function to the bot's event listener. 
async def on_ready(): #the name of the function denotes which event it listens to
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_message(message : discord.Message):
    if message.author == bot.user: #does not attempt to process any command called by the bot itself
        return
    await bot.process_commands(message=message)

bot.run(TOKEN) #runs a bot with the specified [TOKEN], this connects the wrapper to your bot 

