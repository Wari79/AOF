import discord
from discord.ext import commands
import os
import pickle
import random



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
medal = "🏅"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
data_filename4 = "specials"
data_filename5 = "medals"
data_filename = "data.pickle"
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, crate, medals):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.crate = crate
        self.medals = medals


class shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)

    @commands.command()
    @commands.guild_only()
    @cooldown(1, per_sec=40, type=commands.BucketType.user)
    async def construct(self, ctx):
      member_data = load_member_data(ctx.author.id)
      member_data4 = load_member_data4(ctx.author.id)
      member_data5 = load_member_data5(ctx.author.id)

      embed1 = discord.Embed(description=f"What shall we construct, commander?\n-\nTank = <:tank:994712805448093696>\nRobotic spy = 🕵️\nWall = <:wall:1006892740375760959>\nStrike = <:strike:1025877750298452028>\nCrate = {crates}\nItems/Costs = 📋\nCancel = ❌", color=0x309730)
      embed1.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
      
      confirmation = await ctx.reply(embed = embed1)

      await confirmation.add_reaction("<:tank:994712805448093696>")
      await confirmation.add_reaction("🕵️")
      await confirmation.add_reaction("<:wall:1006892740375760959>")
      await confirmation.add_reaction("<:strike:1025877750298452028>")
      await confirmation.add_reaction("<:crate:1036330635238842478>")
      await confirmation.add_reaction("📋")
      await confirmation.add_reaction("❌")

      
      def check(reaction, user):
        return user == ctx.author

      reaction = None

      while True:
      
        if str(reaction) == "<:tank:994712805448093696>":
          await confirmation.clear_reactions()
          if member_data.resources >= 75:
          # if member_data.resources >= 35:

            done = discord.Embed(description=f"Congratulations commander! you succesfully crafted **1 tank {tank}**", color=0x309730)
            done.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=done)
            
              
            member_data.resources -= 75
            # member_data.resources -= 35
            member_data.tanks += 1
            save_member_data(ctx.author.id, member_data)
            
          else:
            error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {res} to construct a tank.", color=0xFFD700)
            error.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=error)  
            
            ctx.command.reset_cooldown(ctx)
                                      
        elif str(reaction) == "🕵️":
          await confirmation.clear_reactions()
          if member_data.resources >= 150:
          # if member_data.resources >= 90:
            dones = discord.Embed(description=f"Congratulations commander! you succesfully crafted **1 robotic spy** :detective:", color=0x309730)
            dones.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=dones)
            
              
            member_data.resources -= 150
            # member_data.resources -= 90
            member_data.spy += 1
            save_member_data(ctx.author.id, member_data)
          else:
            error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {res} to construct a robotic spy.", color=0xFFD700)
            error.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=error)  
            ctx.command.reset_cooldown(ctx)













        elif str(reaction) == "<:crate:1036330635238842478>":
          await confirmation.clear_reactions()
          if member_data5.medals >= 6:
          # if member_data.resources >= 90:
            
            dones = discord.Embed(description=f"Congratulations commander! you succesfully crafted **1 Crate** {crates}", color=0x309730)
            dones.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=dones)
            
              
            member_data5.medals -= 6
            # member_data.resources -= 90
            member_data4.crate += 1
            save_member_data4(ctx.author.id, member_data4)
            save_member_data5(ctx.author.id, member_data5)
          else:
            error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {medal} to construct a crate.", color=0xFFD700)
            error.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=error)  
            ctx.command.reset_cooldown(ctx)





            

        elif str(reaction) == "<:wall:1006892740375760959>":
          await confirmation.clear_reactions()
          if member_data.resources >= 800:
          # if member_data.resources >= 550:
            donew = discord.Embed(description=f"Congratulations commander! you succesfully crafted **1 wall** {wall}", color=0x309730)
            donew.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=donew)

            
              
            member_data.resources -= 800
            # member_data.resources -= 550
            member_data.wall += 1
            save_member_data(ctx.author.id, member_data)
          else:
            error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {res} to construct a wall.", color=0xFFD700)
            await confirmation.edit(embed=error)  
            ctx.command.reset_cooldown(ctx)   
        elif str(reaction) == "<:strike:1025877750298452028>":
          await confirmation.clear_reactions()
          if member_data.resources >= 1200:
          # if member_data.resources >= 735:
            dones = discord.Embed(description=f"Congratulations commander! you succesfully recieved **1 strike** {strike}", color=0x309730)
            dones.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=dones)

            
              
            member_data.resources -= 1200
            # member_data.resources -= 735
            member_data.strikes += 1
            save_member_data(ctx.author.id, member_data)
          else:
            error = discord.Embed(title="INSUFFICIENT AMOUNT", description=f"Sorry commander, you don't have enough {res} to construct a strike.", color=0xFFD700)
            error.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
            await confirmation.edit(embed=error)  
            ctx.command.reset_cooldown(ctx)
          

  
        elif str(reaction) == "📋":
          await confirmation.clear_reactions()
          weapons = discord.Embed(description=f"Tank {tank} = **75 {res}**\nRobotic Spy :detective: = **150** {res}\nWall {wall} = **800** {res}\nStrike {strike} = **1200** {res}\nCrate {crates} = **6** {medal}", color=green)
          weapons.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
          await confirmation.edit(embed=weapons)
          ctx.command.reset_cooldown(ctx)
            
        elif str(reaction) == "❌":
          await confirmation.clear_reactions()
          cancel = discord.Embed(description="Cancelled construction :thumbsup:", color=0xFF0000)
          cancel.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")
          await confirmation.edit(embed=cancel)
          ctx.command.reset_cooldown(ctx)

        try:
              reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
              await confirmation.remove_reaction(reaction, user)
        except:
               break
      await confirmation.clear_reactions()








def setup(client):
    client.add_cog(shop(client))   

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






def load_data4():
        if os.path.isfile(data_filename4):
            with open(data_filename4, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data4(member_ID):
    data = load_data4()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
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
        return Data(0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data5(member_ID, member_data5):
    data = load_data5()

    data[member_ID] = member_data5

    with open(data_filename5, "wb") as file:
        pickle.dump(data, file)