import discord
from discord.ext import commands
import asyncio
import os
bot = commands.Bot(command_prefix='c.')
token = os.environ.get('token')

@bot.event 
async def on_ready():
    print('Ready!!')

@bot.command() 
async def count(ctx, count):
    count = int(count)
    await ctx.message.delete()
    while True:
        await ctx.send(str(count))
        await asyncio.sleep(1)
        count = count+1
bot.run(token)

