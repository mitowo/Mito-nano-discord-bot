import discord
from discord import app_commands
from discord.ext import commands
import random
import os

class nano(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('nano command loaded!')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(fmt)} commands.')

    @app_commands.command(name="nano", description="Sends a random image of Nano")
    async def nano(self, interaction: discord.Interaction):
        print('sending requested nano image!')
        path = random.choice(os.listdir('./images/'))
        await interaction.response.send_message(file=discord.File("./images/"+path))

async def setup(bot):
    await bot.add_cog(nano(bot), guilds=[discord.Object(id=850466170829013044)])