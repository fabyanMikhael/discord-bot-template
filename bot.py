###############################
'''this loads the "DISCORD_TOKEN" string from the .env file'''

# you can remove this try-catch once you have python-dotenv installed
try:
    from dotenv import load_dotenv
except:
    raise ModuleNotFoundError(
        "No module named 'dotenv'\nYou do not have the dotenv module installed!\nUse 'pip install python-dotenv' to install the module."
    )
import os

load_dotenv() #Loads anything in .env file

TOKEN = os.environ["DISCORD_TOKEN"] #grabs the token after loading it with load_dotenv()
if TOKEN == "PASTE_TOKEN_HERE":
    print("Must add your own discord token in .env file!")
    exit()
###############################

import discord

from discord.ext import commands #module that contains the Bot class we need

intents = discord.Intents.all() # will require all intents by default, change this to match your bot's intents

bot = commands.Bot(
                    command_prefix="$",
                    intents=intents,
                    #help_command=None # <- uncomment this if you want to write your own help command
                    )

@bot.event # @bot.event attaches the function to the bot's event listener. 
async def on_ready(): #the name of the function denotes which event it listens to
    print(f"{bot.user.name} has connected to Discord!")
    from Utils.HotReload import HotLoad
    await HotLoad(bot) # will load the cogs and enable hot-reload

@bot.event
async def on_message(message : discord.Message):
    if message.author == bot.user: #does not attempt to process any command called by the bot itself
        return
    await bot.process_commands(message=message) #since we have overwritten the on_message event, we need to call this to process commands


#################Commands#################
'''@bot.command decorator adds this function as a command'''
@bot.command(aliases=["hello"])  #we can give the aliases key argument a list of alternative command names, such as $hello
async def Hi(ctx : commands.Context):  #The name of the function is the command, so the `Hi` function is the $Hi command
    await ctx.reply("hello!") #ctx is the context this command was ran in, .reply() will reply to the user!
   #^^^ await is needed to call async functions!
##########################################

bot.run(TOKEN) #runs a bot with the specified [TOKEN], this connects the wrapper to your bot 

