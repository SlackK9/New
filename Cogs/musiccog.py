""" user_id = 1075189440890286213 # ID of the user to send the DM to
message_content = "top.gg verification 1075189440890286213"  # Message content
user = bot.get_user(user_id)
    if user is None:
user = await bot.fetch_user(user_id)

    try:
    await user.send(message_content)
    await ctx.send(f"Successfully sent a DM to {user}.")
    except discord.Forbidden:
    await ctx.send("I couldn't send the DM. The user might have DMs disabled.")
    except discord.HTTPException as e:
    await ctx.send(f"Failed to send the DM due to an HTTP error: {str(e)}")

import discord
from discord.ext import commands

# Replace with your bot token
TOKEN = 'YOUR_BOT_TOKEN'

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, user: discord.User, *, message):

    try:
        await user.send(message)
        await ctx.send(f"DM sent to {user.name}!")
    except discord.Forbidden:
        await ctx.send("Could not send DM to the user. They might have DMs disabled.")

bot.run(TOKEN)
"""