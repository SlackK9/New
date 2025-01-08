import discord
from discord.ext import commands
from discord import app_commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="ssutest",
        description="Start the server up",
    )
    async def ssutest(self, ctx: commands.Context):


        if int(latency.split(".")[0]) > 150:
            colour = discord.Color.red()
        else:
            colour = discord.Color.green()

        embed = discord.Embed(
            title="NCRP Server Start Up:",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/guilds/1119847222394237041/users/1075189440890286213/avatars/743e6153d7e1197d8cd3ee14b28f5da9.png?size=496")
        embed.add_field(name="The server is starting up!", value="<@&1120824611752378481>", inline=False)
        embed.add_field(name="Join Code", value="WakeNC is our server join code!", inline=False)
        embed.add_field(name="Info:",
                        value="You have 10 minutes to join if you reacted or you may be moderated! Hope to see you in game!",
                        inline=False)

        embed.set_footer(
            text="WakeNCRP Helper Bot v0.5 Alpha.",
            icon_url="https://cdn.discordapp.com/avatars/978662093408591912/4b6cf7884fc5487b53f0c118e9f9598c.png?size=512"
        )

        channel = await _bot.fetch_channel(1119910979703144478)
        await channel.send(embed=embed)
        await channel.send(f'<@&1120824611752378481>')

        await ctx.reply(embed=embed)








async def setup(bot):
    await bot.add_cog(Commands(bot))