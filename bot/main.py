import discord
from discord.ext import commands

server_id = "1180915117773299784"
bot_token = "MTE4MTg1MDI0MTQxMTA2MzgyOA.Gsm5e4.OR7PRjSt-4Uvu8jtiO7AW3caJQBaxD5X5QxZKU"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def create_custom_invite(ctx, vanity_code="tQp4pSE"):
    
    """
    Creates a custom invite link for the server with the provided vanity code.

    Args:
        vanity_code: The desired name for the custom invite link.
    """
    print("Creating custom invite link...")
    # Check if server is boosted
    if not ctx.guild.premium_tier:
        await ctx.send("Your server needs to be boosted to create a custom invite link.")
        return

    # Fetch server object
    server = bot.get_guild(server_id)

    # Update the server's vanity code
    try:
        await server.edit(vanity_code=vanity_code)
        await ctx.send(f"Custom invite link created successfully! Link: https://discord.gg/{vanity_code}")
    except Exception as e:
        await ctx.send(f"Error creating custom invite link: {e}")

bot.run(bot_token)