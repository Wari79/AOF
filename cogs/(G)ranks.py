import discord
from discord.ext import commands
import os
import pickle
import random
import asyncio
import json
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

class ranks(commands.Cog):
    def __init__(self, client): 
        self.client = client


    
    @commands.command(alianses = ["REDEEM_PVT", "Redeem_pvt"])
    @commands.has_role(941007783506092042)
    async def redeem_pvt(self, ctx):
      with open("Ranks/(W)pvt.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __PVT__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(W)pvt.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)

        member_data.strikes += 3
        member_data.spy += 1
        member_data.resources += 100
        member_data.soldiers += 100
        save_member_data(ctx.author.id, member_data)
        reward_pvt = discord.Embed(description=f"**Redemption successful**, __PVT__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n1 :detective:\n100 {res}\n100 {sold}", color=green)
        await ctx.reply(embed=reward_pvt)



  
    @commands.command(alianses = ["REDEEEM_PV2", "Redeem_pv2", "Redeem_Pv2"])
    @commands.has_role(941007926020169818)
    async def redeem_pv2(self, ctx):
      with open("Ranks/(A)pv2.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __PV2__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(A)pv2.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 150
        save_member_data(ctx.author.id, member_data)
        reward_pv2 = discord.Embed(description=f"**Redemption successful**, __PV2__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n150 {res}", color=green)
        await ctx.reply(embed=reward_pv2)

    @commands.command(alianses = ["REDEEEM_PFC", "Redeem_pfc", "Redeem_Pfc"])
    @commands.has_role(941008015996387348)
    async def redeem_pfc(self, ctx):
      with open("Ranks/(B)pfc.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __PFC__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(B)pfc.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 200
        member_data.tanks += 1
        save_member_data(ctx.author.id, member_data)
        reward_pfc = discord.Embed(description=f"**Redemption successful**, __PFC__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n200 {res}\n1 {tank}", color=green)
        await ctx.reply(embed=reward_pfc)

    @commands.command(alianses = ["REDEEEM_SPC", "Redeem_spc", "Redeem_Spc"])
    @commands.has_role(941008333404532767)
    async def redeem_spc(self, ctx):
      with open("Ranks/(C)spc.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __SPC__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(C)spc.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 250
        member_data.tanks += 1
        member_data.spy += 1
        save_member_data(ctx.author.id, member_data)
        reward_spc = discord.Embed(description=f"**Redemption successful**, __SPC__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n250 {res}\n1 {tank}\n1 :detective:", color=green)
        await ctx.reply(embed=reward_spc)

    @commands.command(alianses = ["REDEEEM_CPL", "Redeem_cpl", "Redeem_Cpl"])
    @commands.has_role(941008438090166353)
    async def redeem_cpl(self, ctx):
      with open("Ranks/(D)cpl.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CPL__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(D)cpl.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 300
        member_data.tanks += 1
        member_data.spy += 1
        member_data.soldiers += 300
        save_member_data(ctx.author.id, member_data)
        reward_cpl = discord.Embed(description=f"**Redemption successful**, __CPL__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n300 {res}\n1 {tank}\n1 :detective:\n300 {sold}", color=green)
        await ctx.reply(embed=reward_cpl)

    @commands.command(alianses = ["REDEEEM_SGT", "Redeem_sgt", "Redeem_Sgt"])
    @commands.has_role(941008550245830667)
    async def redeem_sgt(self, ctx):
      with open("Ranks/(E)sgt.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __SGT__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(E)sgt.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 350
        member_data.tanks += 2
        member_data.spy += 1
        member_data.soldiers += 350
        save_member_data(ctx.author.id, member_data)
        reward_sgt = discord.Embed(description=f"**Redemption successful**, __SGT__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n350 {res}\n2 {tank}\n1 :detective:\n350 {sold}", color=green)
        await ctx.reply(embed=reward_sgt)

    @commands.command(alianses = ["REDEEEM_SSG", "Redeem_ssg", "Redeem_Ssg"])
    @commands.has_role(941008677287104529)
    async def redeem_ssg(self, ctx):
      with open("Ranks/(F)ssg.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __SSG__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(F)ssg.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 400
        member_data.tanks += 2
        member_data.spy += 2
        member_data.soldiers += 400
        save_member_data(ctx.author.id, member_data)
        reward_ssg = discord.Embed(description=f"**Redemption successful**, __SSG__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n400 {res}\n2 {tank}\n2 :detective:\n400 {sold}", color=green)
        await ctx.reply(embed=reward_ssg)

    @commands.command(alianses = ["REDEEEM_SFC", "Redeem_sfc", "Redeem_Sfc"])
    @commands.has_role(941008861479972914)
    async def redeem_sfc(self, ctx):
      with open("Ranks/(G)sfc.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __SFC__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(G)sfc.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 450
        member_data.tanks += 3
        member_data.spy += 2
        member_data.soldiers += 450
        member_data.wall += 1
        save_member_data(ctx.author.id, member_data)
        reward_sfc = discord.Embed(description=f"**Redemption successful**, __SFC__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n450 {res}\n3 {tank}\n2 :detective:\n450 {sold}\n1 {wall}", color=green)
        await ctx.reply(embed=reward_sfc)

    @commands.command(alianses = ["REDEEEM_MSG", "Redeem_msg", "Redeem_Msg"])
    @commands.has_role(941010196761833582)
    async def redeem_msg(self, ctx):
      with open("Ranks/(H)msg.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __MSG__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(H)msg.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 500
        member_data.tanks += 3
        member_data.spy += 3
        member_data.soldiers += 500
        member_data.wall += 1
        save_member_data(ctx.author.id, member_data)
        reward_msg = discord.Embed(description=f"**Redemption successful**, __MSG__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n500 {res}\n3 {tank}\n3 :detective:\n500 {sold}\n1 {wall}", color=green)
        await ctx.reply(embed=reward_msg)

    @commands.command(alianses = ["REDEEEM_1SG", "Redeem_1sg", "Redeem_1sg"])
    @commands.has_role(941010203866980372)
    async def redeem_1sg(self, ctx):
      with open("Ranks/(I)1sg.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __1SG__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(I)1sg.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 550
        member_data.tanks += 5
        member_data.spy += 3
        member_data.soldiers += 550
        member_data.wall += 1
        save_member_data(ctx.author.id, member_data)
        reward_1sg = discord.Embed(description=f"**Redemption successful**, __1SG__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n550 {res}\n5 {tank}\n3 :detective:\n550 {sold}\n1 {wall}", color=green)
        await ctx.reply(embed=reward_1sg)

    @commands.command(alianses = ["REDEEEM_SMG", "Redeem_smg", "Redeem_Smg"])
    @commands.has_role(941010208816250910)
    async def redeem_smg(self, ctx):
      with open("Ranks/(J)smg.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __SMG__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(J)smg.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 600
        member_data.tanks += 5
        member_data.spy += 4
        member_data.soldiers += 600
        member_data.wall += 1
        save_member_data(ctx.author.id, member_data)
        reward_smg = discord.Embed(description=f"**Redemption successful**, __SMG__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n600 {res}\n5 {tank}\n4 :detective:\n600 {sold}\n1 {wall}", color=green)
        await ctx.reply(embed=reward_smg)

    @commands.command(alianses = ["REDEEEM_CSM", "Redeem_csm", "Redeem_Csm"])
    @commands.has_role(941010211378974791)
    async def redeem_csm(self, ctx):
      with open("Ranks/(K)csm.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CSM__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(K)csm.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 650
        member_data.tanks += 5
        member_data.spy += 5
        member_data.soldiers += 650
        member_data.wall += 1
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CSM__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n650 {res}\n5 {tank}\n5 :detective:\n650 {sold}\n1 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_WO1", "Redeem_wo1", "Redeem_Wo1"])
    @commands.has_role(941010213857787946)
    async def redeem_wo1(self, ctx):
      with open("Ranks/(L)wo1.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __WO1__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(L)wo1.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 700
        member_data.tanks += 5
        member_data.spy += 5
        member_data.soldiers += 700
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __WO1__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n700 {res}\n5 {tank}\n5 :detective:\n700 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_CW2", "Redeem_cw2", "Redeem_Cw2"])
    @commands.has_role(941010216579891290)
    async def redeem_cw2(self, ctx):
      with open("Ranks/(M)cw2.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CW2__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(M)cw2.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 750
        member_data.tanks += 6
        member_data.spy += 6
        member_data.soldiers += 750
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CW2__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n750 {res}\n6 {tank}\n6 :detective:\n750 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_CW3", "Redeem_cw3", "Redeem_Cw3"])
    @commands.has_role(941010219155218442)
    async def redeem_cw3(self, ctx):
      with open("Ranks/(N)cw3.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CW3__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(N)cw3.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 800
        member_data.tanks += 7
        member_data.spy += 7
        member_data.soldiers += 800
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CW3__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n800 {res}\n7 {tank}\n7 :detective:\n800 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_CW4", "Redeem_cw4", "Redeem_Cw4"])
    @commands.has_role(941010222233841686)
    async def redeem_cw4(self, ctx):
      with open("Ranks/(O)cw4.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CW4__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(O)cw4.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 850
        member_data.tanks += 9
        member_data.spy += 9
        member_data.soldiers += 850
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CW4__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n850 {res}\n9 {tank}\n9 :detective:\n850 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_CW5", "Redeem_cw5", "Redeem_Cw5"])
    @commands.has_role(941010225316655164)
    async def redeem_cw5(self, ctx):
      with open("Ranks/(P)cw5.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CW5__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(P)cw5.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 900
        member_data.tanks += 10
        member_data.spy += 10
        member_data.soldiers += 900
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CW5__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n900 {res}\n10 {tank}\n10 :detective:\n900 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_2Lt", "Redeem_2lt"])
    @commands.has_role(941010228693053492)
    async def redeem_2lt(self, ctx):
      with open("Ranks/(Q)2lt.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __2LT__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(Q)2lt.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 950
        member_data.tanks += 10
        member_data.spy += 10
        member_data.soldiers += 950
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __2LT__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n950 {res}\n10 {tank}\n10 :detective:\n950 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_1Lt", "Redeem_1lt"])
    @commands.has_role(941010235882098738)
    async def redeem_1lt(self, ctx):
      with open("Ranks/(R)1lt.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __1LT__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(R)1lt.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 1100
        member_data.tanks += 12
        member_data.spy += 12
        member_data.soldiers += 1100
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __1LT__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n1100 {res}\n12 {tank}\n12 :detective:\n1100 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_CPT", "Redeem_cpt", "Redeem_Cpt"])
    @commands.has_role(941010238419648583)
    async def redeem_cpt(self, ctx):
      with open("Ranks/(S)cpt.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __CPT__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(S)cpt.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 3
        member_data.resources += 1500
        member_data.tanks += 16
        member_data.spy += 16
        member_data.soldiers += 1500
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __CPT__ rewards have been successfully redeemed.\n-\n**Rewards:**\n3 {strike}\n1500 {res}\n16 {tank}\n16 :detective:\n1500 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_MAJ", "Redeem_maj", "Redeem_Maj"])
    @commands.has_role(941010240709726258)
    async def redeem_maj(self, ctx):
      with open("Ranks/(T)maj.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __MAJ__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(T)maj.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 4
        member_data.resources += 1800
        member_data.tanks += 20
        member_data.spy += 20
        member_data.soldiers += 1800
        member_data.wall += 2
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __MAJ__ rewards have been successfully redeemed.\n-\n**Rewards:**\n4 {strike}\n1800 {res}\n20 {tank}\n20 :detective:\n1800 {sold}\n2 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_LTC", "Redeem_ltc", "Redeem_Ltc"])
    @commands.has_role(941010243746406510)
    async def redeem_ltc(self, ctx):
      with open("Ranks/(U)ltc.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __LTC__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(U)ltc.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 7
        member_data.resources += 2500
        member_data.tanks += 25
        member_data.spy += 25
        member_data.soldiers += 2500
        member_data.wall += 4
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __LTC__ rewards have been successfully redeemed.\n-\n**Rewards:**\n7 {strike}\n2500 {res}\n25 {tank}\n25 :detective:\n2500 {sold}\n4 {wall}", color=green)
        await ctx.reply(embed=reward)

    @commands.command(alianses = ["REDEEEM_COL", "Redeem_col", "Redeem_Col"])
    @commands.has_role(941010253196185681)
    async def redeem_col(self, ctx):
      with open("Ranks/(V)col.json") as json_file:
          data = json.load(json_file)
      try:
        if data["members"][str(ctx.author.id)]:
          fail = discord.Embed(description="**Redemption failed**, you have already redeemed __COL__ rewards.", color=red)
          await ctx.reply(embed=fail)
      except KeyError:
        imports = {
            "member": ctx.author.id, 
            "name": ctx.author.name,
            "checkability": "redeemed"
        }
        data["members"][ctx.author.id] = imports
        with open("Ranks/(V)col.json", "w") as j:
          json.dump(data, j, indent=4)
        member_data = load_member_data(ctx.author.id)
        member_data.strikes += 15
        member_data.resources += 3500
        member_data.tanks += 40
        member_data.spy += 40
        member_data.soldiers += 3500
        member_data.wall += 10
        save_member_data(ctx.author.id, member_data)
        reward = discord.Embed(description=f"**Redemption successful**, __COL__ rewards have been successfully redeemed.\n-\n**Rewards:**\n15 {strike}\n3500 {res}\n40 {tank}\n40 :detective:\n3500 {sold}\n10 {wall}", color=green)
        await ctx.reply(embed=reward)











def setup(client):
    client.add_cog(ranks(client))   

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