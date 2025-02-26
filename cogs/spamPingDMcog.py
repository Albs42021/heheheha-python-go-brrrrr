from discord.ext import commands
import discord
from discord import app_commands

class SpamPingDMCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Spam pings the DM's of someone in this server.")
    async def spam_ping_dm(self, interaction:discord.Interaction, recipient: discord.Member, count:int, message:str):
        sender = interaction.user

        embed = discord.Embed(title = f"Spam pinging DM's:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Recipient:", value = recipient.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = f"{recipient.mention} {message}", inline = False)

        await interaction.response.send_message(embed = embed)

        embed = discord.Embed(title = f"Your DM's are getting spam pinged:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Server:", value = interaction.guild.name, inline = False)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = f"{recipient.mention} {message}", inline = False)

        await recipient.send(f"{sender.mention} is spam pinging your DMs.")
    
        countAt:int = 0
        
        while countAt < count:
            countAt += 1
            await recipient.send(recipient.mention + message)

async def setup(bot: commands.Bot):
    await bot.add_cog(SpamPingDMCog(bot))