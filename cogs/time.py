import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

class time(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('time command loaded!')

    @app_commands.command(name="time", description="Outputs Mito's current time")
    async def time(self, interaction: discord.Interaction):
        mito = discord.Color.from_rgb(77, 104, 158)
        currentDateAndTime = datetime.now() # this grabs whatever the current local time is on the computer
        time = currentDateAndTime.strftime("%I:%M:%S %p")
        embed=discord.Embed(description=str(currentDateAndTime.month) + '/' + str(currentDateAndTime.day) + '/' + str(currentDateAndTime.year) + ' ' + time, color=mito)
        embed.set_author(name="Current time for Mito:") # you may change this obviously
        embed.set_footer(text="Eastern Standard Time (UTC-5)") # you may change this obviously
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(time(bot), guilds=[discord.Object(id=850466170829013044)])