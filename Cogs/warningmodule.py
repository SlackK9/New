import discord
from discord.ext import commands

from utils.util import Pag


class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        @commands.guild_only()
        @commands.has_role(1120059332864782376)
        async def warn(self, ctx, member: discord.Member, *, reason ):
            if member.id in [ctx.author.id, self.bot.user.id]:
                return await ctx.send("You can't warn yourself or my bot!")

