import os, discord, embed, downloadvideo, gitimport, runserver
import asyncio
import functools
from dotenv import load_dotenv
from multiprocessing import freeze_support
from discord.ext import commands
from discord import app_commands
import discord

os.system("") # Needed for message to have colour in the terminal

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
channel_ids = {
    "youtube-logs": 1391985272589123665
}

# ---------------
# BOT SETUP
# ---------------
intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="yt!", intents=intents)

# ---------------
# ON READY
# ---------------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})\n')

@bot.command()
@commands.has_permissions(administrator=True)
async def sync_tree(ctx):
    synced_list = await ctx.bot.tree.sync()
    await ctx.send(f"Syncing {len(synced_list)} commands to all guilds")

@bot.tree.command(
    name="generatepage",
    description="Download a video and generate a page with the video and its details.",
)
@app_commands.describe(
    link="The link of the video you want to download"
)
@commands.has_permissions(administrator=True)
async def generatepage(interaction: discord.Interaction, link: str):
    await interaction.response.defer(ephemeral=False)

    message = await interaction.followup.send(
        embed=embed.show_download_progress(link)
    )

    # Run the blocking download in a separate thread so it doesn't block the event loop
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, functools.partial(downloadvideo.startvideodownload, link))

    completed_embed = embed.show_download_complete(result)

    await message.edit(embed=completed_embed)

@bot.tree.command(
    name="restart",
    description="Restart the app"
)
@commands.has_permissions(administrator=True)
async def restart(interaction: discord.Interaction):
    await interaction.response.send_message("Restarting...")
    await bot.close()
    gitimport.restart_bot()

def main():
    bot.run(token = TOKEN)

if __name__ ==  "__main__":
    freeze_support()
    main()