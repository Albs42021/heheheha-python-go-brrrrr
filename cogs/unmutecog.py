from discord.ext import commands
import discord
from discord import app_commands

class UnmuteCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Unmutes someone on this discord server.")
    @app_commands.checks.has_permissions(moderate_members = True)
    async def unmute(self, interaction: discord.Interaction, member: discord.Member, reason:str):
        await discord.Member.timeout(member, None, reason=reason)

        Serverembed = discord.Embed(title = f"Unmute:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        Serverembed.add_field(name = "Member:", value = member.mention, inline = False)

        Serverembed.add_field(name = "Reason:", value = reason, inline = False)

        await interaction.response.send_message(embed = Serverembed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UnmuteCog(bot))