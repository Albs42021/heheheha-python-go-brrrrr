from discord.ext import commands
import discord
from discord import app_commands

class IDCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gets the id of a member of this discord server.")
    async def id(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user
        await interaction.response.send_message(member.id)

async def setup(bot: commands.Bot):
    await bot.add_cog(IDCog(bot))