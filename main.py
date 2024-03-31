from discord.ext import commands
from discord.ext import tasks
import discord
import config
import asyncio
import os
import random
import calendar
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents, application_id='934698201540362280', activity=discord.Activity(type=discord.ActivityType.watching, name="Nichijou"))

# Getting unix timestamp for when the bot started
datestart = datetime.datetime.utcnow()
utc_timestart = calendar.timegm(datestart.utctimetuple())

@bot.event
async def on_ready():
    print('shinonome nano desu!')
    nanohour.start() # starting hourly nano

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}') # loading cogs

@tasks.loop(hours=1)
async def nanohour():
    channel = bot.get_channel(1048088863312191648) # channel ID
    date = datetime.datetime.utcnow() 
    utc_time = calendar.timegm(date.utctimetuple())
    path = random.choice(os.listdir('./images/'))
    await channel.send(file=discord.File("./images/"+path), content='sending Nano every hour! <a:NanoHype:1121146993406918686>\n\ngoing since <t:' + str(utc_timestart) + ':F>\ncurrent time: <t:' + str(utc_time) + ':F>')
    print("Sent nano image at " + (str(datetime.datetime.now())))

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())