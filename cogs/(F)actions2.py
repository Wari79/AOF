import discord
from discord.ext import commands
import os
import pickle
import asyncio
import random


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
ins = "https://media.discordapp.net/attachments/814828851724943361/1038503971532324984/army-troops_2.gif"
inta = "https://media.discordapp.net/attachments/814828851724943361/1038503994751983707/tanks.gif"
inw = "https://media.discordapp.net/attachments/814828851724943361/1038503916230414428/wall.gif"



data_filename = "currency files/data.pickle"
data_filename4 = "currency files/specials"
data_filename5 = "currency files/medals"
data_filename6 = "currency files/counter"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, medals, crate, ca, scrap, cfc, cfca):
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
        self.cfc = cfc
        self.cfca = cfca



class actions2(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)


    @commands.command()
    @commands.guild_only()
    async def strike(self, ctx, member:discord.Member):
      member_data4 = load_member_data4(ctx.author.id)
      member_data6 = load_member_data6(ctx.author.id)
      victim_data = load_member_data(member.id)
      victim_data4 = load_member_data4(member.id)
      if member_data4.ca <= 0:
        error = discord.Embed(title="Insufficient Amount", description=f"Commander, you don't have any available {ca} to launch a Combat Aircraft", color=yellow)
        await ctx.reply(embed=error)

        
      else:
        check1 = discord.Embed(title="Warning",description=f"**Commander {ctx.author.name},**\n-\nAir strikes deal a total of `1000` HP damage to the mentioned comander's base. It will destroy several walls, soldiers, and tanks that user might have. Are you sure you want to proceed this action on {member.mention}", color=yellow)
        
        checkc = await ctx.send(embed=check1) 
        
        await checkc.add_reaction("✅")
        await checkc.add_reaction("❌")
        def check(reaction, user):
          return user == ctx.author

        reaction = None
        while True:  
          if str(reaction) == "✅":
            await checkc.clear_reactions()
            if victim_data.wall >= 5:
              async with ctx.typing():
                dw = random.randrange(3,5)
                destroying_walls = discord.Embed(description="Air Striking walls..", color=yellow)
                destroying_walls.set_image(url=inw)
                await checkc.edit(embed=destroying_walls)
                victim_data.wall -= int(dw)
                await asyncio.sleep(4)
                member_data4.ca -= 1
                save_member_data4(ctx.author.id, member_data4)
                save_member_data(member.id, victim_data)
            if victim_data.wall < 5:
              async with ctx.typing():
                    
                destroying_walls = discord.Embed(description="Air Striking walls..", color=yellow)
                destroying_walls.set_image(url=inw)
                war = await checkc.edit(embed=destroying_walls)
                victim_data.wall = 0
                await asyncio.sleep(4) 
                member_data4.ca -= 1
                save_member_data4(ctx.author.id, member_data4)
                save_member_data(member.id, victim_data)
                
            if victim_data.tanks >= 45:
                  
              dw2 = random.randrange(15,40)
              destroying_tanks = discord.Embed(description="Air Striking tanks..", color=yellow)
              destroying_tanks.set_image(url=inta)
              await checkc.edit(embed=destroying_tanks)
              victim_data.tanks -= int(dw2)
              await asyncio.sleep(3)
              
              save_member_data(member.id, victim_data)

            if victim_data.tanks < 45:
              destroying_tanks = discord.Embed(description="Air Striking tanks..", color=yellow)
              destroying_tanks.set_image(url=inta)
              await checkc.edit(embed=destroying_tanks)
              victim_data.tanks = 0
              await asyncio.sleep(3)
              
              save_member_data(member.id, victim_data)
                  
            if victim_data.soldiers >= 500:
              dw3 = random.randrange(250,500)
              destroying_soldiers = discord.Embed(description="Air Striking soldiers..", color=yellow)
              destroying_soldiers.set_image(url=ins)
              await checkc.edit(embed=destroying_soldiers)
              victim_data.soldiers -= int(dw3)
              await asyncio.sleep(3)
              
              save_member_data(member.id, victim_data)

                    
            if victim_data.soldiers < 500:
              destroying_soldiers = discord.Embed(description="Air Striking soldiers..", color=yellow)
              destroying_soldiers.set_image(url=ins)
              await checkc.edit(embed=destroying_soldiers)
              victim_data.soldiers = 0
              
              save_member_data(member.id, victim_data)
              await asyncio.sleep(3)




            finish = discord.Embed(title="Air Striked!", description=f"{member.mention}'s base's status\n-\n{victim_data.soldiers} {sold}\n{victim_data.tanks} {tank}\n{victim_data.wall} {wall}", color=green)
            await checkc.edit(embed=finish)

            emergency = discord.Embed(title="Emergency", description=f"Commander! you have been air striked!, you now have:\n-\n{victim_data.soldiers} {sold}\n{victim_data.tanks} {tank}\n{victim_data.wall} {wall}", color=red)
            await member.send(embed=emergency)



            if member_data6.cfca >= 3:
              pass
            if member_data6.cfca < 3:
              
              member_data6.cfca += 1
              save_member_data6(ctx.author.id, member_data6)
            
          
          elif str(reaction) == "❌":
            await checkc.clear_reactions()
            cancelled = discord.Embed(description="Cancelled air strikes operation.", color=green)
            await checkc.edit(embed=cancelled)
            
            ctx.command.reset_cooldown(ctx)
            return

          try:
             reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)
             await checkc.remove_reaction(reaction, user)
             ctx.command.reset_cooldown(ctx)
          except:
            break
          
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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
        pickle.dump(data, file)







def load_data6():
        if os.path.isfile(data_filename6):
            with open(data_filename6, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data6(member_ID):
    data = load_data6()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data6(member_ID, member_data6):
    data = load_data6()

    data[member_ID] = member_data6

    with open(data_filename6, "wb") as file:
        pickle.dump(data, file)