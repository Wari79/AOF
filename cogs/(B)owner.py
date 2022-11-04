import discord
from discord.ext import commands
import os
import pickle
import sys
import json
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
crate = "<:crate:1036330635238842478>"
dead = "<:dead:1025878302503739414>"
spy = "🕵️"
medal = "🏅"
data_filename = "data.pickle"
data_filename4 = "specials"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, ca, crate, scrap):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.crate = crate
        self.ca = ca
        self.scrap = scrap

def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)
class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)


    @commands.command()
    async def owner(self, ctx):
      og = discord.Embed(title="Bot Wise", description="These are sets of commands that are only compatibale with bot owners regarding the bot", color=green)
      
      og.add_field(name="`aof restart`", value="Restart full bot including Main.py file", inline=False)
      
      og.add_field(name="`aof refresh`", value="Refresh all cog files to save updats done to them", inline=False)




      og2 = discord.Embed(title="Server Wise", description="These are sets of commands that are only compatibale with bot owners regarding the server", color=green)

      og2.add_field(name="`aof lock #channel/id {reason}`", value="Locks channel with secified reason", inline=False)
      
      og2.add_field(name="`aof unlock #channel/id`", value="Unlocks channel", inline=False)
      
      og2.add_field(name="`aof dm @member/id {message}`", value="DM member with specified message", inline=False)


      
      og3 = discord.Embed(title="Currency Wise", description="These are sets of commands that are only compatibale with bot owners regarding the currency", color=green)
      
      og3.add_field(name="`aof get`", value="Interactive command to give you any weaponized object inside the pickle file", inline=False)
      
      og3.add_field(name="`aof give @member/id`", value="Interactive command to give the member any weaponized object inside the pickle file", inline=False)
      
      og3.add_field(name="`aof take @member/id`", value="Interactive command to take away any weaponized object inside the pickle file from the member", inline=False)
      
      og3.add_field(name="`aof subtract_q1 {amount} @member/id`", value="Subtracts amounts of messages sent by user in quest 1", inline=False)

      
      lists = [og, og2, og3]
      async with ctx.typing():
        await asyncio.sleep(1)
      message = await ctx.reply(embed=og)
      await message.add_reaction("⏮")
      await message.add_reaction("◀")
      await message.add_reaction("▶")
      await message.add_reaction("⏭")

      def check(reaction, user):
          return user == ctx.author

      i = 0
      reaction = None

      while True:
          if str(reaction) == "⏮":
              i = 0
              await message.edit(embed=lists[i])
          elif str(reaction) == "◀":
              if i > 0:
                  i -= 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "▶":
              if i < 2:
                  i += 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "⏭":
              i = 2
              await message.edit(embed=lists[i])

          try:
              reaction, user = await self.client.wait_for(
                "reaction_add", timeout=120.0, check=check
            )
              await message.remove_reaction(reaction, user)
          except:
              break
      await message.clear_reactions()

    


  
    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
      restart = discord.Embed(title="AOF Restart Protocol", description="Cog Folders = `3`\nPython Files = `11`\nJSON Files = `24`\nPickle Files = `3`\n-\n**Wait for the bot to send you a message saying it's online**", color=green)
      await ctx.message.add_reaction("✅")
      await ctx.send(embed=restart, delete_after=8)
      restart_bot() 
          


  
    @commands.command()
    @commands.is_owner()
    async def reset(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      member_data.soldiers = 0
      member_data.tanks = 0
      member_data.resources = 0
      member_data.spy = 0
      member_data.strikes = 0
      save_member_data(member.id, member_data)
      confirmation = discord.Embed(description=f"Successfully reseted `{member}'s` base :white_check_mark:")
      await ctx.reply(embed=confirmation)
      
      




      
    
    @commands.command()
    @commands.is_owner()
    async def get(self, ctx):
      member_data = load_member_data(ctx.author.id)
      member_data4 = load_member_data4(ctx.author.id)
      first = discord.Embed(description=f"What shall I give you, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy :detective:\nResources {res}\nWall {wall}\nStrike {strike}\nCrate {crate}\nca {ca}", color=green)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you are requesting?", color=green)
      await ctx.reply(embed=third)
      complete = discord.Embed(description="you have successfully been given what you requested. :white_check_mark:", color=green)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      if msg1.content.lower() == "tanks":
        member_data.tanks += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)  
        return
    
      elif msg1.content.lower() == "resources":
        member_data.resources += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "ca":
        member_data4.ca += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data4(ctx.author.id, member_data4)
        return
      elif msg1.content.lower() == "crate":
        member_data4.crate += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data4(ctx.author.id, member_data4)
        return
      elif msg1.content.lower() == "walls":
        member_data.wall += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return
      elif msg1.content.lower() == "spy":
        member_data.spy += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers":
        member_data.soldiers += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
      elif msg1.content.lower() == "strike":
        member_data.strikes += int(amount.content)
        await ctx.reply(embed=complete)
        save_member_data(ctx.author.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)
    

  
    @commands.command()
    @commands.is_owner()
    async def give(self, ctx, member:discord.Member):
      member_data = load_member_data(member.id)
      member_data4 = load_member_data4(member.id)
      first = discord.Embed(description=f"What shall I give this commander, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy :detective:\nResources {res}\nWall {wall}\nStrikes {strike}\nCrate {crate}", color=green)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you request?", color=green)
      await ctx.reply(embed=third)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      complete = discord.Embed(description="Commander recieved the demanded request. :white_check_mark:", color=green)
      if msg1.content.lower() == "tanks":
        member_data.tanks += int(amount.content)
        await ctx.reply(embed=complete)
        ss1 = discord.Embed(description=f"Commander, you were given {amount.content} {tank} from the system.", color=green)
        await member.send(embed=ss1)
        save_member_data(member.id, member_data)  
        return
    
      elif msg1.content.lower() == "resources":
        member_data.resources += int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were given {amount.content} {res} from the system", color=green)
        await member.send(embed=ss2)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "walls":
        member_data.wall += int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were given {amount.content} {wall} from the system.", color=green)
        await member.send(embed=ss3)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "crate":
        member_data4.crate += int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were given {amount.content} {crate} from the system.", color=green)
        await member.send(embed=ss3)
        save_member_data4(member.id, member_data4)
        return
      elif msg1.content.lower() == "spy":
        member_data.spy += int(amount.content)
        await ctx.reply(embed=complete)
        ss4 = discord.Embed(description=f"Commander, you were given {amount.content} :detective: from the system.", color=green)
        await member.send(embed=ss4)
        save_member_data(member.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers":
        member_data.soldiers += int(amount.content)
        await ctx.reply(embed=complete)
        ss5 = discord.Embed(description=f"Commander, you were given {amount.content} {sold} from the system.", color=green)
        await member.send(embed=ss5)
        save_member_data(member.id, member_data)
      elif msg1.content.lower() == "strike":
        member_data.strikes += int(amount.content)
        await ctx.reply(embed=complete)
        ss6 = discord.Embed(description=f"Commander, you were given {amount.content} {strike} from the system.", color=green)
        await member.send(embed=ss6)
        save_member_data(member.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)

  
    @commands.command()
    @commands.is_owner()
    async def take(self, ctx, member:discord.Member=None):
      if member == None:
        member = ctx.author
      member_data = load_member_data(member.id)
      member_data4 = load_member_data4(member.id)
      
      first = discord.Embed(description=f"What shall take from this user, general?\n-\nSoldiers {sold}\nTanks {tank}\nRobotic Spy :detective:\nResources {res}\nWalls {wall}\nStrike {strike}\ncrate {crate}", color=red)
      await ctx.reply(embed=first)
      msg1 = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)

      
      third = discord.Embed(description="What is the amount you request?", color=yellow)
      await ctx.reply(embed=third)
      
      amount = await self.client.wait_for("message",check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id,)
      complete = discord.Embed(description="Deletion successful. :white_check_mark:", color=red)
      if msg1.content.lower() == "tanks":
        member_data.tanks -= int(amount.content)
        await ctx.reply(embed=complete)
        ss1 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {tank} by the system operators.", color=yellow)
        await member.send(embed=ss1)
        save_member_data(member.id, member_data)  
        return



      elif msg1.content.lower() == "crate":
        member_data4.crate -= int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {crate} by the system operators", color=yellow)
        await member.send(embed=ss2)
        save_member_data4(member.id, member_data4)
        return
    
      elif msg1.content.lower() == "resources":
        member_data.resources -= int(amount.content)
        await ctx.reply(embed=complete)
        ss2 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {res} by the system operators", color=yellow)
        await member.send(embed=ss2)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "walls":
        member_data.wall -= int(amount.content)
        await ctx.reply(embed=complete)
        ss3 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {wall} by the system operators.", color=yellow)
        await member.send(embed=ss3)
        save_member_data(member.id, member_data)
        return
      elif msg1.content.lower() == "spy":
        member_data.spy -= int(amount.content)
        await ctx.reply(embed=complete)
        ss4 = discord.Embed(description=f"Commander, you were subtracted {amount.content} :detective: by the system operators.", color=yellow)
        await member.send(embed=ss4)
        save_member_data(member.id, member_data)
        return  
      elif msg1.content.lower() == "soldiers":
        member_data.soldiers -= int(amount.content)
        await ctx.reply(embed=complete)
        ss5 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {sold} by the system operators.", color=green)
        await member.send(embed=ss5)
        save_member_data(member.id, member_data)
      elif msg1.content.lower() == "strike":
        member_data.strikes -= int(amount.content)
        await ctx.reply(embed=complete)
        ss6 = discord.Embed(description=f"Commander, you were subtracted {amount.content} {strike} by the system operators.", color=green)
        await member.send(embed=ss6)
        save_member_data(member.id, member_data)
      else:
        error = discord.Embed(description="Sorry, couldn't identify the construction, **make sure there is no capital letters and try again!**", color=red)
        await ctx.reply(embed=error)


    


  
    @commands.command()
    @commands.is_owner()
    async def dm(self, ctx, member:discord.Member, *, message):
      await ctx.channel.purge(limit=1)
      confirmation = discord.Embed(title="Confirmation", description=f"Are you sure you want to send `{message}` to {member.name}?", color=yellow)
      comp = await ctx.send(embed=confirmation)
      await comp.add_reaction("✅")
      await comp.add_reaction("❌")

      def check(reaction, user):
        return user == ctx.author

      reaction = None
      while True:
        if str(reaction) == "✅":
          await comp.clear_reactions()
          reply = discord.Embed(title="Incoming DM", description=f"{message}\nBest Regards,\nArmy Of Freedom Administration", color=yellow)
          await member.send(embed=reply)
          done = discord.Embed(description="DM has been sent successfully :white_check_mark:\n-\n**This message is self-destructory and will be deleted in 8 seconds**", color=green)
          await comp.edit(embed=done, delete_after=8.0)
            
        elif str(reaction) == "❌":
          await comp.clear_reactions()
          cancel = discord.Embed(description="DM protocol cancelled. :white_check_mark:", color=red)
          await comp.edit(embed=cancel)

        try:
              reaction, user = await self.client.wait_for("reaction_add", timeout=35.0, check=check)

        except:
            break


  
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel, *, reason=None):
          await ctx.message.delete()
          channel = channel or ctx.channel
          overwrite = channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = False

          await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

          embed = discord.Embed(title="Channel lock", color=yellow)
          embed.add_field(
            name="Reason/message :arrow_heading_down:", value=f"{reason}", inline=False
        )
          await channel.send(embed=embed)

#-------------------------------------------------------------------------------------------------------------

  
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
            await ctx.message.delete()
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            embed = discord.Embed(title="Channel unlocked", color=yellow)
            await channel.send(embed=embed)


    





def setup(client):
    client.add_cog(owner(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)





#--------------



def load_data4():
        if os.path.isfile(data_filename4):
            with open(data_filename4, "rb") as file:
              return pickle.load(file)
        else:
            return dict()

def load_member_data4(member_ID):
    data = load_data4()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]


def save_member_data4(member_ID, member_data4):
    data = load_data4()

    data[member_ID] = member_data4

    with open(data_filename4, "wb") as file:
        pickle.dump(data, file)