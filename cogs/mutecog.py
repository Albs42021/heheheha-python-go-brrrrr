from discord.ext import commands
import discord
import datetime
from discord import app_commands

class MuteCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Mutes someone on this discord server.")
    @app_commands.checks.has_permissions(moderate_members = True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member, days:int, hours:int, minutes:int, reason:str): 
        time = datetime.timedelta(days = days, hours = hours, minutes = minutes)

        timeValue:str = str(days) + " days, " + str(hours) + " hours, and " + str(minutes) + " minutes."

        await discord.Member.timeout(member, time, reason=reason)

        Serverembed = discord.Embed(title = f"Mute:", timestamp = discord.utils.utcnow(), color = 0xFF0000)

        Serverembed.add_field(name = "Member:", value = member.mention, inline = False)

        Serverembed.add_field(name = "Time:", value = timeValue, inline = False)

        Serverembed.add_field(name = "Reason:", value = reason, inline = False)

        await interaction.response.send_message(embed = Serverembed)

async def setup(bot: commands.Bot):
    await bot.add_cog(MuteCog(bot))