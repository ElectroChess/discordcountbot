import discord
from discord.ext import commands
import asyncio
bot = commands.Bot(command_prefix='c.')
token = 'NzUyMjA4OTUyMDQ0ODE0NDg2.X1UTLQ.XzVG4aUU0ik6MSbP5xLj784pQLw'

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

