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
ca = "<:ca:1036338258629632020>"
crate = "<:crate:1036330635238842478>"
medal = "🏅"
spy = "🕵️"
scrap = "⚙️"



air = "https://media.discordapp.net/attachments/814828851724943361/1038888979686244362/ezgif.com-gif-maker_4.gif"
spies = "https://media.discordapp.net/attachments/814828851724943361/1038885671697403984/ezgif.com-gif-maker_3.gif"
base = "https://media.discordapp.net/attachments/814828851724943361/1038878064521777212/ezgif.com-gif-maker.gif"
walls = "https://media.discordapp.net/attachments/814828851724943361/1038878256922906634/ezgif.com-gif-maker_1.gif"
tank3 = "https://media.discordapp.net/attachments/814828851724943361/1038881920978792499/ezgif.com-gif-maker_2.gif"
aof = "https://media.discordapp.net/attachments/941054208327696395/1003781301494632579/unknown.png"
trade = "https://media.discordapp.net/attachments/814828851724943361/1038891016306049145/ezgif.com-gif-maker_5.gif"
war = "https://media.discordapp.net/attachments/814828851724943361/1038891231633215488/ezgif.com-gif-maker_6.gif"
sell = "https://media.discordapp.net/attachments/814828851724943361/1038892781181091961/ezgif.com-gif-maker_7.gif"
end = "https://media.discordapp.net/attachments/814828851724943361/1038897468886237254/ezgif.com-gif-maker_8.gif"





col = 0x89CFF0

tree = "https://images-ext-1.discordapp.net/external/aryLl3-37PrQXeZqPsAPkkSm4ak0RjefVDc7KNISTPg/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/569970865744248837/a_645b82a88c8aab8f9048e38c5e2ec6ce.gif?width=434&height=434"



data_filename = "currency files/data.pickle"
data_filename4 = "currency files/specials"
data_filename5 = "currency files/medals"
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700
class Data:
      def __init__(self, resources, soldiers, tanks, spy, wall, strikes, crate, ca, scrap, medals):
        self.resources = resources
        self.soldiers = soldiers
        self.tanks = tanks
        self.spy = spy
        self.wall = wall
        self.strikes = strikes
        self.crate = crate
        self.ca = ca
        self.scrap = scrap
        self.medals = medals
        


class info(commands.Cog):
    def __init__(self, client): 
        self.client = client

    def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
        return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)






    @commands.command()
    @commands.guild_only()
    async def help(self, ctx): 
      intro = discord.Embed(title="**Freedom Bot’s Helping guide**",description=f"Welcome, Commander {ctx.author.name} to Freedom Bot’s Helping guide.\n-\nThis guide will explain Freedom Bot, its basics, and the elements it contains.\n-\nNavigate the guide using the reactions below.", color=0x567d46)
      intro.set_thumbnail(url=aof)

      confirmation = discord.Embed(title="Important Note!", description="In the following embeds of the guide you will be observing alot of commands that require member mentioning, however you may use [ids](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-#:~:text=In%20the%20right%2Dclick%20menu,ID%20copied%20to%20your%20clipboard.) that are accessible from [Developer tools](https://www.youtube.com/watch?v=e_UoIwmS8Xk). Ids make it less suspicious and more secretive to accomplish your commands without disturbances to others.", color=yellow)

      

      #Page 1: Consits of introuction to AOF
      p1 = discord.Embed(description="**Freedom Bot**\nFreedom Bot is an interactive role play custom bot made specially for Army Of Freedom, it is a war simulation game that contains simple yet fun gameplay.\n-\nYour mission is to become the greatest commander out there, and Freedom Bot is here to assist you in completing this ambitious mission.", color = col) 


      
      #Page 2: Base
      p2 = discord.Embed(title="Your base, your root", description="> The base is the core of your adventure; everything you gain in the game will have an affect on your journey and your base, either positively or negatively. Your base contains  important sections;\n1) **Protection**\n2) **Army**\n3) **Specials**\n4) **Wealth**\n-\n> You may check your base using ` aof base `", color = col) 

      p2.set_image(url=base)

      
      #Page 3: Protection
      p3 = discord.Embed(title="Proection", description="> Protection comes first, and by that we mean shields and walls\n-\n> **Wall** is an obtainable item that may be constructed with ` aof construct `, and its sole purpose is to guard you from an approaching attack.\n-\n> **Stike** is an available construction that may be built with ` aof construct `, and its main purpose is to function as a sort of ticket to an attack, but they do not cause any harm to enemy's base or troops. __**You need a strike to perform an attack**__", color = col)

      p3.set_image(url=walls)
      
      
      #Page 4: Army 1
      p4 = discord.Embed(title="Army P1/2", description=f"> Army in aof mainly focus on two great factors; **Soldiers {sold}** and **tanks {tank}**. A **soldier** is worth `1 hp` while a **tank** is worth `10 hp`.\n-\nYou can recruit **soldiers** using ` aof recruit ` and you can construct a **tank** using ` aof construct `",color = col)

      p4.set_image(url=tank3)

      
      #Page 5: Army 2
      p5 = discord.Embed(title="Army P2/2", description = f"> **Spies {spy}** observe other commanders' bases primarily. They fully tell you of what the other commander have acquired in their base. You can construct a spy using ` aof construct`\n-\n> You may spy another commander using ` aof spy @member/id `", color = 0x89CFF0)
      p5.set_image(url=spies)
      
      

      p6 = discord.Embed(title="Specials", description=f"> Special weapons and gadgets are available to make you more powerful.\n-\n> **Combat Aircraft {ca}**, combat aircraft is a very strong weapon that provides air strikes that deal a total of ` 1000 hp ` damage to enemy's base, they can be constructed using ` aof construct ` for scraps.\n-\n> **Scrap {scrap}** are materials that are used to construct combat aircrafts, scraps can be constructed by ` aof construct `.\n-\n> **Crates {crate}** are loot-like boxes that contain sets of goods, they can be crafted with war medals.\n-\n> **War medals {medal}** can be obtained to commanders after every successful war they initiate. they are also visible in your base.\n-\nTo use air strikes on a member, use ` aof strike @member/id `\nTo open a crate use ` aof open crate `", color=col)
      p6.set_image(url=air)

      
      

      p7 = discord.Embed(title="Wealth", description=f"> **Resources {res}** are the most important factor in this game, they are the 'currency' of the game, they can be obtained by ` aof expedition ` and are used in constructions. You can gain resources by invading other commanders as well on completing quests", color = col)

      p8 = discord.Embed(title="Attacking", description="> To declare an **attack** and start war, use ` aof attack ` and mention the commander you want to attack, but you have to play it smart and choose the right moment to strike a blow.", color=col)
      p8.set_image(url=war)

      

      p9= discord.Embed(title="Extra P1/2", description = "> **Trading**\n-\nThis command allows you to trade a certain amount of item for another user's item. This can be used via ` aof trade @member/id {trader item amount} {trader item name} {user item amount} {user item name} `\n-\n>**Quests**\nQuests are weekly missions that all commanders can complete in order to gain a big amount of goodies, they last for a short time, but there rewards will benefit you for awhile, use ` aof view quests ` to view all the quests available at that time, your progress and the rewards you get for completing each one of them.",  color = col)
      p9.set_image(url=trade)

      

      p92 = discord.Embed(title="Extra P2/2", description = "> **Selling**\n-\nYou can sell items/weapons that you don't need anymore using ` aof sell {amount} {item name} ` but you will only gain half it's original price", color = col)
      p92.set_image(url=sell)

      p10 = discord.Embed(description = "**Brigadier General Application**\nIf you would like to help us and become a general to improve Army Of Freedom’s experience, use ` aof apply ` and follow the applying process.", color = col)
      p10.set_thumbnail(url=aof)

      end = discord.Embed(title="You're ready to go!", description="> **That's it commander, that's the end of the guide. You now know the basics of the bot and the bot's purpose and visio, good luck!", color=green)
      end.set_image(url=end)

      

      

      lists = [intro, confirmation, p2, p3, p4, p5, p6, p7, p8, p9, p92, p10, end]
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
              if i < 12:
                  i += 1
                  await message.edit(embed=lists[i])
          elif str(reaction) == "⏭":
              i = 12
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
      member_data4 = load_member_data4(ctx.author.id)
      member_data5 = load_member_data5(ctx.author.id)
      health1 = member_data.soldiers * 1
      health2 = member_data.soldiers * 1 + member_data.tanks * 10

      if member_data.strikes < 0:
        member_data.strikes = 0
      if member_data.resources < 0:
        member_data.resources = 0
    
      embed = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embed.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = True)
      embed.add_field(name="War Medals", value=f"{member_data5.medals} {medal}", inline=True)
      embed.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}", inline = False)
      embed.add_field(name="Specials", value=f"{member_data4.ca} {ca}\n{member_data4.crate} {crate}\n{member_data4.scrap} {scrap}", inline = False)
      embed.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embed.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")
      #----
      embeds = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embeds.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = True)
      embeds.add_field(name="War Medals", value=f"{member_data5.medals} {medal}", inline=True)
      embeds.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.tanks)} {tank}\n{str(member_data.spy)} :detective:", inline = False)
      embeds.add_field(name="Specials", value=f"{member_data4.ca} {ca}\n{member_data4.crate} {crate}\n{member_data4.scrap} {scrap}", inline = False)
      embeds.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embeds.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
      embeds.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")

      #---

      embedsp = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      
      embedsp.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = True)
      embedsp.add_field(name="War Medals", value=f"{member_data5.medals} {medal}", inline=True)
      embedsp.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}\n{str(member_data.spy)} :detective:", inline = False)
      embedsp.add_field(name="Specials", value=f"{member_data4.ca} {ca}\n{member_data4.crate} {crate}\n{member_data4.scrap} {scrap}", inline = False)
      embedsp.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embedsp.add_field(name="Total HP", value=f"{health2} {hearts}", inline = False)
      embedsp.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")
      
      #----
     
      embed2 = discord.Embed(title=f"{ctx.author.display_name}'s Base", color=0xfbc28d)
      embed2.add_field(name="Protection", value=f"{str(member_data.wall)} {wall}", inline = True)
      embed2.add_field(name="War Medals", value=f"{member_data5.medals} {medal}", inline=True)
      embed2.add_field(name="Army", value=f"{member_data.strikes} {strike}\n{str(member_data.soldiers)} {sold}", inline = False)
      embed2.add_field(name="Specials", value=f"{member_data4.ca} {ca}\n{member_data4.crate} {crate}\n{member_data4.scrap} {scrap}", inline = False)
      embed2.add_field(name="Wealth", value=f"{str(member_data.resources)} {res}", inline = False)
      embed2.add_field(name="Total HP", value=f"{health1} {hearts}", inline = False)
      embed2.set_thumbnail(url="https://media.discordapp.net/attachments/814828851724943361/995035645053513829/ezgif.com-gif-maker.jpg")


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
        return Data(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
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