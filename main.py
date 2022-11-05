import discord
from discord.ext import commands
from replit import db
import requests
import random
import json
import asyncio
from keep_alive import keep_alive
import os
from discord.utils import find
import datetime
from datetime import datetime
import traceback
import pickle
from discord.ext.commands import (
    has_permissions,
    MissingPermissions,
    has_role,
    MissingRole,
    cooldown,
    BucketType,
    NotOwner,
    CommandNotFound,
    MissingRequiredArgument,
)
import time
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
owners = [569970865744248837, 798280308071596063]
client = commands.Bot(
    command_prefix=["aof ", "Aof "], owner_ids=set(owners),intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("We Breamed in as {0.user}".format(client))
    await client.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="The Mighty War!"))
    ham = client.get_user(798280308071596063)
    tree = client.get_user(569970865744248837)
    embed = discord.Embed(description="**I am now online.**", color=0x00C4B8)
    await ham.send(embed=embed)
    await tree.send(embed=embed)
    aof = client.get_guild(939972627563417651)
    for guild in client.guilds:
      if guild != aof:
        await guild.leave()
        await ham.send(f"Left a server called {guild.name}")
    client.launch_time = datetime.utcnow()
def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
    return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)





    

@client.command()
@commands.is_owner()
async def r(ctx):
  first = discord.Embed(description="On it..", color=yellow)
  second = await ctx.reply(embed=first)
  client.reload_extension("cogs.(A)system")
  client.reload_extension("cogs.(B)owner")
  client.reload_extension("cogs.(C)income")
  client.reload_extension("cogs.(D)info")
  client.reload_extension("cogs.(E)shop")
  client.reload_extension("cogs.(F)actions")
  client.reload_extension("cogs.(G)ranks")
  client.reload_extension("cogs.(H)quest")
  client.reload_extension("cogs.(I)clans")
  client.reload_extension("cogs.(F)actions2")
  await asyncio.sleep(2)
  third = discord.Embed(description="Refreshed **9** cog files", color=green)
  await second.edit(embed=third)




for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    (f"cogs.{filename[:-3]}")
  
keep_alive()
try:
  client.run(os.getenv("TOKEN"))
except:
    os.system("kill 1")