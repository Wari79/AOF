import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio



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
tree = "https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434"
medal = "🏅"
spy = "🕵️"
scrap = "⚙️"



green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
data_filename4 = "currency files/specials"
data_filename5 = "currency files/medals"
data_filename = "currency files/data.pickle"
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, crate, medals, scrap, ca):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.crate = crate
        self.medals = medals
        self.ca = ca
        self.scrap = scrap


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

      embed1 = discord.Embed(description=f"What shall we construct, commander?\n-\nTank = {tank}\nRobotic spy = 🕵️\nWall = {wall}\nStrike = {strike}\nCrate = {crates}\nScrap = {scrap}\nCombat Aircraft = {ca}\nItems/Costs = 📋\nCancel = ❌", color=0x309730)

      
      embed1.set_footer(icon_url=tree, text="In memory of General Tree")
      
      confirmation = await ctx.reply(embed = embed1)

      await confirmation.add_reaction("<:tank:994712805448093696>")
      await confirmation.add_reaction("🕵️")
      await confirmation.add_reaction("<:wall:1006892740375760959>")
      await confirmation.add_reaction("<:strike:1025877750298452028>")
      await confirmation.add_reaction("<:crate:1036330635238842478>")
      await confirmation.add_reaction("⚙️")
      await confirmation.add_reaction("<:ca:1036338258629632020>")
      await confirmation.add_reaction("📋")
      await confirmation.add_reaction("❌")

      
      def check(reaction, user):
        return user == ctx.author

      reaction = None

      while True:
      
        if str(reaction) == "<:tank:994712805448093696>":
            await confirmation.clear_reactions()
            # if member_data.resources >= 35:

            ask = discord.Embed(description=f"How many {tank} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 100

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {tank} for {calculation} {res}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data.resources:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {tank} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {tank} for ` {calculation} ` {res}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data.resources -= int(calculation)
                  member_data.tanks += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
              except:
                break
          
  
                                      
        elif str(reaction) == "🕵️":
            await confirmation.clear_reactions()
            ask = discord.Embed(description=f"How many {spy} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 190

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {spy} for {calculation} {res}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data.resources:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {spy} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {spy} for ` {calculation} ` {res}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data.resources -= int(calculation)
                  member_data.spy += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
              except:
                break
          













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
            ask = discord.Embed(description=f"How many {wall} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 950

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {wall} for {calculation} {res}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data.resources:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {wall} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {wall} for ` {calculation} ` {res}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data.resources -= int(calculation)
                  member_data.wall += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
                
              except:
                break  
        elif str(reaction) == "<:strike:1025877750298452028>":
            await confirmation.clear_reactions()
            ask = discord.Embed(description=f"How many {strike} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 1600

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {strike} for {calculation} {res}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data.resources:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {strike} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {strike} for ` {calculation} ` {res}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data.resources -= int(calculation)
                  member_data.strikes += int(amount.content)
                  save_member_data(ctx.author.id, member_data)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
              except:
                break
          
          

  
        elif str(reaction) == "<:ca:1036338258629632020>":
            await confirmation.clear_reactions()
            ask = discord.Embed(description=f"How many {ca} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 7

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {ca} for {calculation} {scrap}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data4.scrap:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {scrap}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {ca} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {ca} for ` {calculation} ` {scrap}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data4.scrap -= int(calculation)
                  member_data4.ca += int(amount.content)
                  save_member_data4(ctx.author.id, member_data4)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
              except:
                break
        elif str(reaction) == "⚙️":
            await confirmation.clear_reactions()
            ask = discord.Embed(description=f"How many {scrap} are you requesting to construct?", color=yellow)

            await confirmation.edit(embed=ask)
          
            amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          
            
            await confirmation.delete()


            calculation = int(amount.content) * 1000

            confirmation2 = discord.Embed(description=f"Are you sure you want to construct {amount.content} {scrap} for {calculation} {res}?", color=yellow)

            confirmation22 = await ctx.send(embed=confirmation2)

            await confirmation22.add_reaction("✅")
            await confirmation22.add_reaction("❌")
            def check(reaction, user):
              return user == ctx.author

            reaction = None

            while True:
              if str(reaction) == "✅":
                await confirmation22.clear_reactions()
                if calculation > member_data.resources:
                  
                  error = discord.Embed(title="Insufficient Amount", description=f"Sorry commander, you dont have the required resources!\n-\n> **You need: {calculation} {res}**", color=red)
                  await ctx.send(embed=error)
                  ctx.command.reset_cooldown(ctx)
                  return
                else:
                  async with ctx.typing():
                    start = discord.Embed(description=f"[C{tank2}]", color=green)
                    await confirmation22.edit(embed=start)
                    await asyncio.sleep(1.5)
                    start2 = discord.Embed(description=f"[Co{tank2}]", color=green)
                    await confirmation22.edit(embed=start2)
                    await asyncio.sleep(1.5)
                    start3 = discord.Embed(description=f"[Con{tank2}]", color=green)
                    await confirmation22.edit(embed=start3)
                    await asyncio.sleep(1.5)
                    start4 = discord.Embed(description=f"[Cons{tank2}]", color=green)
                    await confirmation22.edit(embed=start4)
                    await asyncio.sleep(1.5)
                    start5 = discord.Embed(description=f"[Const{tank2}]", color=green)
                    await confirmation22.edit(embed=start5)
                    await asyncio.sleep(1.5)
                    start6 = discord.Embed(description=f"[Constr{tank2}]", color=green)
                    await confirmation22.edit(embed=start6)
                    await asyncio.sleep(1.5)
                    start7 = discord.Embed(description=f"[Constru{tank2}]", color=green)
                    await confirmation22.edit(embed=start7)
                    await asyncio.sleep(1.5)
                    start8 = discord.Embed(description=f"[Construc{tank2}]", color=green)    
                    await confirmation22.edit(embed=start8)
                    await asyncio.sleep(1.5)
                    start9 = discord.Embed(description=f"[Construct{tank2}]", color=green)    
                    await confirmation22.edit(embed=start9)
                    await asyncio.sleep(1.5)
                    start10= discord.Embed(description=f"[Constructe{tank2}]", color=green)    
                    await confirmation22.edit(embed=start10)
                    await asyncio.sleep(1.5)
                    start11 = discord.Embed(description=f"[Constructed {scrap} !]", color=green)
                    await confirmation22.edit(embed=start11)
                    await asyncio.sleep(1.5)
                  success = discord.Embed(title="Completed Construction", description=f"**Succesfully constructed {amount.content} {scrap} for ` {calculation} ` {res}**", color=green)
                  await confirmation22.delete()
                  await ctx.reply(embed=success)

                  member_data.resources -= int(calculation)
                  member_data4.scrap += int(amount.content)
                  save_member_data4(ctx.author.id, member_data4)
                  return
              elif str(reaction) == "❌":
                
                await confirmation22.clear_reactions()
                await confirmation22.delete()
                cancel = discord.Embed(description="Construction cancelled :white_check_mark:", color=green)
                await confirmation22.edit(embed=cancel)
                ctx.command.reset_cooldown(ctx)
                return
              try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=15.0, check=check)
                await confirmation22.remove_reaction(reaction, user)
              except:
                break
        elif str(reaction) == "📋":
          await confirmation.clear_reactions()
          weapons = discord.Embed(description=f"Tank {tank} = **100 {res}**\n-\nRobotic Spy :detective: = **190** {res}\n-\nWall {wall} = **950** {res}\n-\nStrike {strike} = **1600** {res}\n-\nCrate {crates} = **6** {medal}\n-\nScrap {scrap} = **1000** {res}\n-\nCombat Aircraft {ca} = **7 {scrap}**", color=green)
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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data5(member_ID, member_data5):
    data = load_data5()

    data[member_ID] = member_data5

    with open(data_filename5, "wb") as file:
        pickle.dump(data, file)