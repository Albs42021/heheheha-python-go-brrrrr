from discord.ext import commands
import discord
from discord import app_commands

class PingCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready():
        print("cogs.pingcog has been loaded.")

    @app_commands.command(description = "Gives you the bot's ping.")
    async def ping(self, interaction:discord.Interaction):
        embed = discord.Embed(title = f"Ping:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Ping:", value = f"**{round(self.bot.latency * 1000)}**ms", inline = False)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(PingCog(bot))