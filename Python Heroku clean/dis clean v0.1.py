import discord
import logging
import requests
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from discord import Status

####################
###Outputs logs into console as not done by default
logging.basicConfig(level=logging.INFO)

###Variables and pre-commands
description = "A bot that announces when Dr.Sweet touch is online plus more"
bot = commands.Bot(command_prefix='~~', description=description)
bot.remove_command('help')
channel=discord.Object(451922147107930123)


###Info about bot
@bot.command()
async def info():
    embed
    embed.add_field(name="Author", value="oats")
    await bot.say(embed=embed)
    

###Bot's 'help' command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="IDS", description=description)
    embed.add_field(name="~~greet", value="The bot will greet you!", inline=True)
    embed.add_field(name="~~info", value="Prints out some information on the bot", inline=True)
    embed.add_field(name="~~help", value="Returns this message :p", inline=True)

    await ctx.send(embed=embed)


#Says hello if u type ~~greet!
@bot.command()
async def greet():
    await bot.say("Hello!")
    

#Checks if Sweets has gone online or not and sends message
@bot.event
async def on_member_update(member : discord.Member, after):
    m = "Dr. Sweet Touch"
    is_sweet = member.name
    if is_sweet == m and str(after.status) != "offline":
        msg = "{} is {}! <@!439074559577030666>".format(after.name, after.status)
        await bot.send_message(channel, msg)
        

###Logs the bot into the server
@bot.event
async def on_ready():
    print('Logged in as')
    #print(bot.user.name)
    print(bot.user.id)
    print('------')
 

#adds authentication token
bot.run('')

