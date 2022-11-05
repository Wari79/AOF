import discord
from discord.ext import commands
import os
import pickle
import asyncio


sold = "<:Soldier_Buzz:966705306342129704>"
res = "<:Resources:994990321240912052>"
tank = "<:tank:994712805448093696>"
tank2 = "<:tank2:995097737974521948>"
hearts = ":helmet_with_cross:"
dead = "<:dead:1025878302503739414>"
wall = "<:wall:1006892740375760959>"
strike = "<:strike:1025877750298452028>" 
ca = "<:ca:1036338258629632020>"
crate = "<:crate:1036330635238842478>"
medal = "🏅"
spy = "🕵️"



data_filename = "currency files/data.pickle"
data_filename4 = "currency files/specials"
data_filename5 = "currency files/medals"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, medals, crate, ca, scrap):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.medals = medals
        self.crate = crate
        self.ca = ca
        self.scrap = scrap



class actions2(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)


    # @commands.command()
    # @commands.guild_only()
    # async def strike(self, ctx, member:discord.Member):
    #   member_data4 = load_member_data4(ctx.author.id)
    #   member_data = load_member_data(member.id)

      
    #   if member_data4.ca <= 0:
    #     error = discord.Embed(title="Insufficient Amount", description=f"Commander, you don't have any available {ca} to launch a Combat Aircraft", color=yellow)
    #     await ctx.reply(embed=error)
    #   else:
    #     check1 = discord.Embed(description=f"Commander {ctx.author.name}, are you sure you want to proceed this action? **there will be no cancel option if you continue**", color=yellow)
    #     checkc = await ctx.send(embed=ground4) 
    #     await checkc.add_reaction("✅")
    #     await checkc.add_reaction("❌")
    #     def check(reaction, user):
    #       return user == ctx.author

    #     reaction = None
    #     while True:  
    #       if str(reaction) == "✅":
    #         await checkc.clear_reactions()
            
            


            
    #         completed = discord.Embed()

    #       try:
    #          reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
    #          await war.remove_reaction(reaction, user)
    #          ctx.command.reset_cooldown(ctx)
    #       except:
    #         break
          
def setup(client):
    client.add_cog(actions2(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)


def load_data5():
        if os.path.isfile(data_filename5):
            with open(data_filename5, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data5(member_ID):
    data = load_data5()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data5(member_ID, member_data5):
    data = load_data5()

    data[member_ID] = member_data5

    with open(data_filename5, "wb") as file:
        pickle.dump(data, file)





#--------------------------------

def load_data4():
        if os.path.isfile(data_filename4):
            with open(data_filename4, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data4(member_ID):
    data = load_data4()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
        pickle.dump(data, file)