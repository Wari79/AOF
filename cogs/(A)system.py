import discord
from discord.ext import commands
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
import time
green = 0x567d46
red = 0xFF0000
yellow = 0xFFD700


class system(commands.Cog):
    def __init__(self, client):
        self.client = client

    def better_time(self, cd:int):
        time = f"{cd}s"
        if cd > 60:
            minutes = cd - (cd % 60)
            seconds = cd - minutes
            minutes = int(minutes/ 60)
            time = f"{minutes}m {seconds}s"
            if minutes > 60:
                hoursglad = minutes -(minutes % 60)
                hours = int(hoursglad/ 60)
                minutes = minutes - (hours*60)
                time = f"{hours}h {minutes}m {seconds}s"
        return time


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        owner = self.client.get_user(798280308071596063)
        if isinstance(error, commands.NotOwner):
          own = discord.Embed(description="Access failed, user's identity hasn't been recognized.", color=red)
          await ctx.reply(embed=own)
        elif isinstance(error, MissingPermissions):
          per = discord.Embed(description=f"**Action failed**, you need ``{error.missing_perms}`` permission to access.", color=red)
          await ctx.reply(embed=per)
          ctx.command.reset_cooldown(ctx)
        elif isinstance(error, MissingRequiredArgument):
          args = discord.Embed(description=f"Commander {ctx.author.name}, you have missed an argument while trying to perform this action, you are required to mention `{error.param.name}` for the action to be executed.", color=red)
          await ctx.reply(embed=args)
          ctx.command.reset_cooldown(ctx)
        elif isinstance(error, CommandNotFound):
          comm = discord.Embed(description="**Action failed**, this command hasn't been found in the database.", color=red)
          await ctx.reply(embed=comm)
        elif isinstance(error, MissingRole):
          roler = discord.Embed(description=f"Commander, you are missing <@&{error.missing_role}> role", color=red)
          await ctx.reply(embed=roler)
          ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.NoPrivateMessage):
          dm = discord.Embed(description=f"Commander, you cannot use this command here. Head to the server and execute the command at either <#939982436492791838> or <#939982482097442816>", color=red)
          await ctx.reply(embed=dm)
          ctx.command.reset_cooldown(ctx)
        elif isinstance(error, discord.Forbidden):
            emergency = discord.Embed(
                title="",
                description="I am not high enough to perform this command please try moving my role up the role list like in the images :white_check_mark:",
                color=0xFF0000,
            )
            emergency.set_image(url="https://discord.com/channels/960189413349019688/960189414477295632/964544873812357160")
            emergency.set_image(      url="https://discord.com/channels/960189413349019688/960189414477295632/964544997355556874")
            await ctx.reply(embed=emergency)
        elif isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
            if cd == 0:
              cd = 1
            # cool = discord.Embed(description='**Action failed**, this action can’t be done at the moment, it’s estimated that this action can be done <t:{}:R>.'.format(int(time.time() + error.retry_after)), color=red)
            em = discord.Embed(description=f"**Action failed**, this action can’t be done at the moment, it’s estimated that this action can be done in ` {self.better_time(cd)} `", color=red)
            await ctx.reply(embed=em)
        else:
            em = discord.Embed(
                title=f"Error!",
                description=f"If this error keeps occuring, please contact {owner} regarding the issue! thank you!",
                color=0x0000,
            )
            em.add_field(
                name="Terminal error :arrow_heading_down:",
                value=f"`{str(error)}`",
                inline=True,
            )
            await ctx.reply(embed=em)
            await ctx.message.add_reaction("❌")
            ctx.command.reset_cooldown(ctx)
            raise error

def setup(client):
    client.add_cog(system(client))      