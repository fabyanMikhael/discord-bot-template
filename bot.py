###############################
"""this loads the "DISCORD_TOKEN" string from the .env file"""

# you can remove this try-catch once you have python-dotenv installed
import os
import discord
from discord.ext import commands  # module that contains the Bot class we need
from dotenv import load_dotenv

from Utils.HotReload import HotLoad
from Utils.errorhandling import ErrorHandle


load_dotenv()  # Loads anything in .env file

TOKEN = os.environ[
    "DISCORD_TOKEN"
]  # grabs the token after loading it with load_dotenv()
if TOKEN == "PASTE_TOKEN_HERE":
    print("Must add your own discord token in .env file!")
    exit()
###############################


intents = (
    discord.Intents.all()
)  # will require all intents by default, change this to match your bot's intents

bot = commands.Bot(
    command_prefix="$",
    intents=intents,
    # help_command=None # <- uncomment this if you want to write your own help command
)


@bot.event  # @bot.event attaches the function to the bot's event listener.
async def on_ready():  # the name of the function denotes which event it listens to
    print(f"{bot.user.name} has connected to Discord!")

    error_channel = None  # change this to be any channel_id you want to see your errors or leave it as None
    ErrorHandle(bot, error_channel)  # will error handle for the bot
    await HotLoad(bot)  # will load the cogs and enable hot-reload


@bot.event
async def on_message(message: discord.Message):
    if (
        message.author == bot.user
    ):  # does not attempt to process any command called by the bot itself
        return
    await bot.process_commands(
        message=message
    )  # since we have overwritten the on_message event, we need to call this to process commands


#################Commands#################
"""@bot.command decorator adds this function as a command"""


@bot.command(
    aliases=["hello"]
)  # we can give the aliases key argument a list of alternative command names, such as $hello
async def Hi(
    ctx: commands.Context,
):  # The name of the function is the command, so the `Hi` function is the $Hi command
    await ctx.reply(
        "hello!"
    )  # ctx is the context this command was ran in, .reply() will reply to the user!
    raise Exception()


# ^^^ await is needed to call async functions!
##########################################

bot.run(
    TOKEN
)  # runs a bot with the specified [TOKEN], this connects the wrapper to your bot
