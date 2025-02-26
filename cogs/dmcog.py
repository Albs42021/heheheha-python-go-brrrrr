from discord.ext import commands
import discord
from discord import app_commands

class DMCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "DM's someone on this server.")
    async def dm(self, interaction: discord.Interaction, recipient:discord.Member, message:str):
        sender = interaction.user

        DMembed = discord.Embed(title = f"You have been sent a DM:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        DMembed.add_field(name = "Author:", value = sender.mention, inline = False)

        DMembed.add_field(name = "Message:", value = message, inline = False)

        await recipient.send(embed = DMembed)

        Serverembed = discord.Embed(title = f"DM:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        Serverembed.add_field(name = "Recipient:", value = recipient.mention, inline = False)

        Serverembed.add_field(name = "Author:", value = sender.mention, inline = False)

        await interaction.response.send_message(embed = Serverembed)

async def setup(bot: commands.Bot):
    await bot.add_cog(DMCog(bot))