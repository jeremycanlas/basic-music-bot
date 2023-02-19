import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
# from help_cog import help_cog
from music_cog import music_cog

load_dotenv()

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="$", intents = intents)

# bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#   await bot.change_presence(activity=nextcord.Game(name="on " + str(len(bot.guilds)) + " Servers", type=0))

bot.run(os.getenv("WINTER_TOKEN"))