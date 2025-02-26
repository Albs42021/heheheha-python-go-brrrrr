from discord.ext import commands
import discord
from discord import app_commands

class UnbanCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Unbans someone from this discord server.")
    @app_commands.checks.has_permissions(moderate_members = True)
    async def unban(self, interaction: discord.Interaction, user:discord.User, reason:str): 
        await interaction.guild.unban(user, reason=reason)

        Serverembed = discord.Embed(title = f"Unban:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        Serverembed.add_field(name = "Member:", value = user.mention, inline = False)

        Serverembed.add_field(name = "Reason:", value = reason, inline = False)

        await interaction.response.send_message(embed = Serverembed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UnbanCog(bot))