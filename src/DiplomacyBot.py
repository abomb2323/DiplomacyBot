"""
    This file handles all of the I/O with the server and its users
"""
import asyncio
import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='A bot owned by the Overwatch Krew and Alex')


@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('```Format has to be in NdN!```')
        return
    if rolls > 100:
        await bot.say('``Max number of rolls is 100```')
    else:
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await bot.say('```' + result + '```')


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say('```' + random.choice(choices) + '```')


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run('MjY4MTI1MzY3MjI5ODc0MTc2.C1WPGA.nlEGD69vO-8ah9beTslqr1XeBug')