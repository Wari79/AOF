import discord
from discord.ext import commands
import os
import pickle
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
data_filename = "data.pickle"
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        


class info(commands.Cog):
    def __init__(self, client): 
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)






    @commands.command()
    @commands.guild_only()
    async def help(self, ctx): 
      intro = discord.Embed(title="**Freedom Bot’s Helping guide**",description=f"Welcome, Commander {ctx.author.name} to Freedom Bot’s Helping guide.\n-\nThis guide will explain Freedom Bot, its basics, and the elements it contains.\n-\nNavigate the guide using the reactions below.", color=0x567d46)
      intro.set_thumbnail(url="https://media.discordapp.net/attachments/941054208327696395/1003781301494632579/unknown.png")
      intro.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")


      p2 = discord.Embed(description="**Freedom Bot**\nFreedom Bot is an interactive role play custom bot made specially for Army Of Freedom, it is a war simulation game that contains simple yet fun gameplay.\n-\nYour mission is to become the greatest commander out there, and Freedom Bot is here to assist you in completing this ambitious mission.", color = 0x89CFF0) 
      p2.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p3 = discord.Embed(description="**The Base And Resources**\n**The Base**\nThe base is where you make your plans and next attacks, it contains all your soldiers, tanks, resources, defenses and spies, use ` aof base ` to see your base.\n-\n**Resources**\nYour army’s existence depends on the resources you have, it is what makes the difference in battle, so you have to make sure you always have enough, use ` aof expedition ` to search for resources.\nresources can also be earned after a successful attack, it is used to to construct different items that will help you in your mission, use ` aof construct ` to see all the items.", color = 0x89CFF0) 

      p3.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p4 = discord.Embed(description="**Soldiers and Tanks**\n**The Soldiers**\nSoldiers are the backbone of your army, you need to make sure they are in great numbers when planning to attack, use ` aof recruit ` to recruit soldiers.\n-\n**Tanks**\nTanks are heavy weapons made from hard metal, it increases the power of your army dramatically, use ` aof construct ` and click on the reaction that corresponds to the tank to successfully construct one.", color = 0x89CFF0)
      
      p4.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p5 = discord.Embed(description="**Walls and Spies**\n**Walls**\nWalls are a very effective way to stop an attack, they completely stop an attack, but get destroyed in the process, use ` aof construct ` and click on the reaction that corresponds to the wall to successfully construct one.\n-\n**Spies**\nUse spies to get all the information you need to know about another commander’s  base, this is a very helpful tool which is most effective before declaring an attack, use ` aof construct ` and click on the reaction that corresponds to the robotic spy to successfully construct one. and use ` aof spy ` and then mention the commander you want to spy on.",color = 0x89CFF0)

      p5.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p6 = discord.Embed(description= "**Strikes and Attacks**\n**Strikes**\nStrikes are the item needed for launching an attack, they are limited so use them wisely, you can construct them using ` aof construct ` and click on the reaction that corresponds to the strike to successfully construct one, but the main way to get them is through promotions and ranking up.\n-\n**Attacks**\nTo declare an attack and start war, use ` aof attack ` and mention the commander you want to attack, but you have to play it smart and choose the right moment to strike a blow.", color = 0x89CFF0)
      
      p6.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p77 = discord.Embed(description="**Trading and Quests**\n**Trading**\nWith trading, things will get easier for weapon transfering. This command allows you to trade a certain amount of item for another user's item. This can be used via ` aof trade @member/id {trader item amount} {trader item name} {user item amount} {user item name} `\n-\n**Quests**\nQuests are weekly missions that all commanders can complete in order to gain a big amount of goodies, they last for a short time, but there rewards will benefit you for awhile, use ` aof view quests ` to view all the quests available at that time, your progress and the rewards you get for completing each one of them.", color=0x89CFF0)
      p77.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p7 = discord.Embed(description="**Rewards & Promotions**\nEach time you rank up to a higher rank, you get rewards, the rewards increases as the ranking gets harder, to make the ranking feel rewarding, to redeem the rewards of a rank after achieving it, use ` aof redeem_ ` and then write the name of the rank you want to redeem without spaces.\n-\nIf it’s your first time reading this, use `aof redeem_pvt ` for a boost to start your journey with.", color = 0x89CFF0)

      p7.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p8= discord.Embed(description= "**Tips**\nHere are a few tips that might help you in your mission:\n\n-Whenever you use a command on another commander, it’s preferable to use their ID and not to mention them, when mentioning them, they might have time to react or they will seek revenge, using their ID makes it harder to know how attacked them.\n\n-Using a spy before declaring an attack is the best time to use it, you will know all the base information, so you can prepare depending on it.\n\n-Don’t rush, use your resources wisely and make the right decisions, to become the greatest commander of them all.",  color = 0x89CFF0)

      p8.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      p9 = discord.Embed(description = "**Brigadier General Application**\nIf you would like to help us and become a general to improve Army Of Freedom’s experience, use `aof apply ` and follow the applying process.", color = 0x89CFF0)

      p9.set_footer(icon_url="https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434", text="In memory of General Tree")

      

      lists = [intro, p2, p3, p4, p5, p6, p77, p7, p8, p9]
      async with ctx.typing():
        await asyncio.sleep(1)
      message = await ctx.reply(embed=intro)
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
              if i < 9:
                  i += 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "⏭":
              i = 9
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
    @commands.guild_only()
    async def base(self, ctx):
      member_data = load_member_data(ctx.author.id)
      health1 = member_data.soldiers * 1
      health2 = member_data.soldiers * 1 + member_data.tanks * 10

      if member_data.strikes < 0:
        member_data.strikes = 0
      if member_data.resources < 0:
        member_data.resources = 0
    
      embed = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embed.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = True)
      embed.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}", inline = False)
      embed.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embed.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
      #----
      embeds = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embeds.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = False)
      embeds.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}\n{str(member_data.spy)} :detective:", inline = False)
      embeds.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embeds.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)

      #---

      embedsp = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embedsp.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = False)
      embedsp.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.spy)} :detective:", inline = False)
      embedsp.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embedsp.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
      
      #----
     
      embed2 = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      embed2.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = False)
      embed2.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}", inline = False)
      embed2.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embed2.add_field(name="Total HP", value=f"{health1} {hearts}", inline = False)
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")


      base_info = discord.Embed(description="Intel has been successfully sent to your DMs. :white_check_mark:", color=0x567d46)

      await ctx.reply(embed=base_info)

      if member_data.tanks <= 0 and member_data.spy <=0:
        await ctx.author.send(embed=embed2)
      if member_data.tanks > 0 and member_data.spy <= 0:
        await ctx.author.send(embed=embed)
      if member_data.tanks <= 0 and member_data.spy > 0:
        await ctx.author.send(embed=embedsp)
      if member_data.tanks > 0 and member_data.spy > 0:
         await ctx.author.send(embed=embeds)
          

      
         
        

          
     


def setup(client):
    client.add_cog(info(client))   

def load_data():
        if os.path.isfile(data_filename):
            with open(data_filename, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)