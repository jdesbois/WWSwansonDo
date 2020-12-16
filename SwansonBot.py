import os
import requests
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='wwsd', help='Responds with a random Ron Swanson quote!')
async def wwsd(ctx):
    response = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
    quote = response.json()[0]
    print(quote)
    await ctx.send(quote)


@bot.command(name='wwsdsearch', help="Responds with a Ron Swanson quote associated with the search word (accepts only one word)")
async def wwsdsearch(ctx, arg):
    response = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes/search/" + arg)
    quote = response.json()[0]
    print(quote)
    await ctx.send(quote)


bot.run(TOKEN)