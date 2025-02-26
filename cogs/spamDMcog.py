from discord.ext import commands
import discord
from discord import app_commands

class SpamDMCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Spams the DM's of someone in this server.")
    async def spam_dm(self, interaction:discord.Interaction, recipient: discord.Member, count:int, message:str):
        sender = interaction.user

        embed = discord.Embed(title = f"Spamming DM's:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Recipient:", value = recipient.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = message, inline = False)

        await interaction.response.send_message(embed = embed)

        embed = discord.Embed(title = f"Your DM's are getting spammed:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Server:", value = interaction.guild.name, inline = False)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = message, inline = False)

        await recipient.send(embed = embed)
    
        countAt:int = 0
        
        while countAt < count:
            countAt += 1
            await recipient.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(SpamDMCog(bot))