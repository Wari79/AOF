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
tank2 = "<:tank2:995097737974521948>"
hearts = ":helmet_with_cross:"
dead = "<:dead:1021894878294183987>"
wall = "<:wall:1006892740375760959>"
strike = "<:strike:1025877750298452028>" 
ca = "<:ca:1036338258629632020>"
crates = "<:crate:1036330635238842478>"
dead = "<:dead:1025878302503739414>"
spy = "🕵️"


data_filename = "data.pickle"
data_filename3 = "quest2"
data_filename4 = "specials"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, s, r, crate, ca, scrap):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.s = s
        self.r = r
        self.crate = crate
        self.ca = ca
        self.scrap = scrap


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

    @commands.command()
    @commands.guild_only()
    @cooldown(1, per_sec=30, type=commands.BucketType.user)
    async def open(self, ctx, crate=None):
      member_data = load_member_data(ctx.author.id)
      member_data4 = load_member_data4(ctx.author.id)
      if crate != "crate":
        return
      if member_data4.crate <= 0:
        error = discord.Embed(title="Error!", description=f"Commander, you don't have a {crate} to open", color=yellow)
        await ctx.reply(embed=error)
      else:
        async with ctx.typing():
          start = discord.Embed(description=f"[C-------- {crates}]", color=green)
          message = await ctx.reply(embed=start)
          await asyncio.sleep(1.5)
          start2 = discord.Embed(description=f"[Co------- {sold}]", color=green)
          await message.edit(embed=start2)
          await asyncio.sleep(1.5)
          start3 = discord.Embed(description=f"[Com------ {spy}]", color=green)
          await message.edit(embed=start3)
          await asyncio.sleep(1.5)
          start4 = discord.Embed(description=f"[Comp----- {tank}]", color=green)
          await message.edit(embed=start4)
          await asyncio.sleep(1.5)
          start5 = discord.Embed(description=f"[Compl---- {res}]", color=green)
          await message.edit(embed=start5)
          await asyncio.sleep(1.5)
          start6 = discord.Embed(description=f"[Comple--- {strike}]", color=green)
          await message.edit(embed=start6)
          await asyncio.sleep(1.5)
          start7 = discord.Embed(description=f"[Complet-- {wall}]", color=green)
          await message.edit(embed=start7)
          await asyncio.sleep(1.5)
          start8 = discord.Embed(description=f"[Complete- {tank2}]", color=green)
          await message.edit(embed=start8)
          await asyncio.sleep(1.5)
          start9 = discord.Embed(description=f"[Completed openning {crates}!]", color=green)
          await message.edit(embed=start9)
          await asyncio.sleep(1.5)

          option_s = random.randrange(90,175)
          rare_list = ["strike", "wall"]
          option_rare = random.choice(rare_list)
          option_rare2 = random.randrange(3,4)
          option_t = random.randrange(4,6)
          
          option_r = random.randrange(150,350)
          option_Spy = random.randrange(3,4)
          if option_rare == "strike":
            r_emoji = strike
            member_data.strikes += int(option_rare2)
            save_member_data(ctx.author.id, member_data)
          if option_rare == "wall":
            r_emoji = wall
            member_data.wall += int(option_rare2)
            save_member_data(ctx.author.id, member_data)

          
          fin = discord.Embed(description=f"Crate Contained:\n-\n{option_r} {res}\n{option_s} {sold}\n{option_t} {tank}\n{option_Spy} {spy}\n{option_rare2} {r_emoji}", color=green)
          await message.edit(embed=fin)

          #result
          member_data.soldiers += int(option_s)
          member_data.tanks += int(option_t)
          member_data.spy += int(option_Spy)
          member_data.resources += int(option_r)
          member_data4.crate -= 1


          
          save_member_data(ctx.author.id, member_data)
          save_member_data4(ctx.author.id, member_data4)
        

    
      
#----Data

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)




#-----Data 3


def load_data3():
        if os.path.isfile(data_filename3):
            with open(data_filename3, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data3(member_ID):
    data = load_data3()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data3(member_ID, member_data3):
    data = load_data3()

    data[member_ID] = member_data3

    with open(data_filename3, "wb") as file:
        pickle.dump(data, file)





#-----Data 4

def load_data4():
        if os.path.isfile(data_filename4):
            with open(data_filename4, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data4(member_ID):
    data = load_data4()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
        pickle.dump(data, file)