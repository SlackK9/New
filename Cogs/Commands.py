import discord
from discord.ext import commands
from discord import app_commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="ping",
        description="Check the bot's latency",
    )
    async def ping(self, ctx: commands.Context):
        latency = str(round(self.bot.latency * 1000, 2))

        if int(latency.split(".")[0]) > 150:
            colour = discord.Color.red()
        else:
            colour = discord.Color.green()

        embed = discord.Embed(
            title="Pong!",
            description=f"Bot is online and responding with a latency of {latency}ms",
            color=colour
        )

        await ctx.reply(embed=embed)

    @commands.hybrid_command(
        name="ssutest",
        description="Start the server up",
    )
    async def ssutest(self, ctx: commands.Context):
        embed = discord.Embed(
            title="NCRP Server Start Up:",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/1119847222394237041/d03d6c6ed2a897ec897218afd8071a51.png?size=256"
        )
        embed.add_field(name="The server is starting up!", value="<@&1120824611752378481>", inline=False)
        embed.add_field(name="Join Code", value="WakeNC is our server join code!", inline=False)
        embed.add_field(
            name="Info:",
            value="You have 10 minutes to join if you reacted or you may be moderated! Hope to see you in game!",
            inline=False
        )

        embed.set_footer(
            text="WakeNCRP Helper Bot v0.5 Alpha.",
        )

        channel = await self.bot.fetch_channel(1119910979703144478)  # Use self.bot here
        await channel.send(embed=embed)
        # await channel.send(f'<@&1120824611752378481>')

        await ctx.reply(embed=embed)  # Removed the extra parenthesis

    @commands.hybrid_command(
        name="staffneeded",
        description="Start the server up",
    )
    async def staffneeded(self, ctx: commands.Context):
        embed = discord.Embed(
            title="NCRP Staff Assistance Needed!",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/1119847222394237041/d03d6c6ed2a897ec897218afd8071a51.png?size=256"
        )
        embed.add_field(name="Assist your fellow staff!", value="{UserCalling} is requesting staff join up in the game server!", inline=False)

        embed.set_footer(
            text="WakeNCRP Helper Bot v0.5 Alpha.",
        )

        channel = await self.bot.fetch_channel(1119910979703144478)  # Use self.bot here
        await channel.send(embed=embed)
        # await channel.send(f'<@&1120824611752378481>')

        await ctx.reply(embed=embed)  # Removed the extra parenthesis

    @commands.hybrid_command(
        name="fafopager",
        description="Start the server up",
    )
    async def fafopager(self, ctx: commands.Context):


        channel = await self.bot.fetch_channel(1326306040743989349)  # Use self.bot here

        for i in range(5):
            await channel.send(f'<@&1325685769129693214>')




async def setup(bot):
    await bot.add_cog(Commands(bot))