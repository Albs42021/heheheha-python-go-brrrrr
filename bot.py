from discord.ext import commands
from dotenv import load_dotenv
import aiohttp
import discord
from discord import app_commands
import os
import datetime
import asyncio
import math

load_dotenv()

def get_token():
    return os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '|', intents = intents)
bot.activity = discord.Game("/help")

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        print("Worked")

@bot.listen()
async def on_message_delete(message: discord.Message):
    if not message.guild:
        return
    
    bot.last_deleted_message = message

@bot.listen()
async def on_message_edit(before:discord.Message, after:discord.Message):
    if not before.guild:
        return

    bot.last_edited_message_before = before
    bot.last_edited_message_after = after

@bot.listen()
async def on_message(message: discord.Message):
    if message.author.bot:
        return

@bot.event
async def on_command_error(ctx:commands.Context, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You are missing the permissions required to run this command.")

    elif isinstance(error, commands.BadArgument):
        await ctx.reply("Bad argument.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing a required argument for this command.")

    elif isinstance(error, commands.CommandNotFound):
        await ctx.reply("Invalid command.")

    else:
        await ctx.reply(f"Error: {error}")

async def startup():
    await bot.load_extension("cogs.snipeDeletecog")
    await bot.load_extension("cogs.kickcog")
    await bot.load_extension("cogs.mutecog")
    await bot.load_extension("cogs.unmutecog")
    await bot.load_extension("cogs.bancog")
    await bot.load_extension("cogs.unbancog")
    await bot.load_extension("cogs.generateInvitecog")
    await bot.load_extension("cogs.dmcog")
    await bot.load_extension("cogs.spamcog")
    await bot.load_extension("cogs.spamPingcog")
    await bot.load_extension("cogs.spamDMcog")
    await bot.load_extension("cogs.spamPingDMcog")
    await bot.load_extension("cogs.idcog")
    await bot.load_extension("cogs.saycog")
    await bot.load_extension("cogs.calculatorcog")
    await bot.load_extension("cogs.definecog")
    await bot.load_extension("cogs.jokecog")
    await bot.load_extension("cogs.extensionManager")
    await bot.load_extension("cogs.pingcog")
    await bot.load_extension("cogs.snipeEditcog")
    await bot.load_extension("cogs.helpcog")
    await bot.load_extension("cogs.triviacog")
    await bot.load_extension("cogs.memecog")
    await bot.load_extension("cogs.roastcog")
    await bot.load_extension("cogs.roastDMcog")

    async with aiohttp.ClientSession() as session:
        bot.session = session

        await bot.start(get_token())

asyncio.run(startup())