import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json


sold = "<:Soldier_Buzz:966705306342129704>"
res = "<:Resources:994990321240912052>"
tank = "<:tank:994712805448093696>"
strike = "<:strike:1025877750298452028>"
wall = "<:wall:1006892740375760959>"
data_filename = "data.pickle"
data_filename3 = "quest2"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, s, r):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.s = s
        self.r = r


class income(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type) 


    
          
          


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#------------------------------------------------------------------------- #-------------------------------------------------------------------------   




    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def bump(self, ctx, member:discord.Member):
      member_data = load_member_data(member.id)
      bumped = discord.Embed(description=f"Thank you for bumping our server!\n-\n**You recieved 100 {res} from system operators**", color=green)
      await member.send(embed=bumped)
      member_data.resources += 100
      save_member_data(member.id, member_data)
      completed = discord.Embed(description="Sent bump message to user successfully!", color=green)
      await ctx.reply(embed=completed)
      
      


      
    
    @commands.command(aliases = ["Recruit"])
    @commands.guild_only()
    @cooldown(1, per_min=3, type=commands.BucketType.user)
    # @cooldown(1, per_sec=5, type=commands.BucketType.user)
    async def recruit(self, ctx):
      
        member_data = load_member_data(ctx.author.id)
      
        option = random.randrange(10,25)
      
      
        member_data.soldiers += int(option)

        s2 = discord.Embed(description=f"**Recruit sequence completed**, you recruited **{option} {sold}**", color=0x567d46)
        s2.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

        await ctx.reply(embed=s2)
      
        save_member_data(ctx.author.id, member_data)
        member_data3 = load_member_data3(ctx.author.id)
        member_data3.s += 1
        save_member_data3(ctx.author.id, member_data3)

      
#-------------------------------------------------------------------------
#---------------------------------------------------------------------------

      
    
    @commands.command()
    @commands.guild_only()
    @cooldown(1, per_min=3, type=commands.BucketType.user)
    # @cooldown(1, per_sec=5, type=commands.BucketType.user)
    async def expedition(self, ctx):
      
       member_data = load_member_data(ctx.author.id)
      
       optionresult = random.randrange(20,35)
      
       search = discord.Embed(description=f"You have gone on a long journey to search for resources, after searching the land, you found **{optionresult} {res}**", color=0x309730)
       search.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
      
       await ctx.reply(embed=search)
      
       member_data.resources += int(optionresult)
      
       save_member_data(ctx.author.id, member_data) 
       member_data3 = load_member_data3(ctx.author.id)
       member_data3.r += 1
       save_member_data3(ctx.author.id, member_data3)

    
      


def setup(client):
    client.add_cog(income(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)







def load_data3():
        if os.path.isfile(data_filename3):
            with open(data_filename3, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data3(member_ID):
    data = load_data3()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data3(member_ID, member_data3):
    data = load_data3()

    data[member_ID] = member_data3

    with open(data_filename3, "wb") as file:
        pickle.dump(data, file)