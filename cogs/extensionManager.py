from discord.ext import commands
from discord import app_commands
import discord

class ExtensionManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description = "Reloads an extention of the bot.")
    @commands.guild_only()
    @commands.is_owner()
    async def reload_extension(self, interaction: discord.Interaction, extension: str):
        try:
            await self.bot.reload_extension(extension)
            await interaction.response.send_message(f"{extension} has been reloaded.")
        except:
            await interaction.response.send_message(f"Something went wrong.")

async def setup(bot):
    await bot.add_cog(ExtensionManager(bot))