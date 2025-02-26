from discord.ext import commands
import discord
from discord import app_commands

class SpamPingCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Spam pings someone on this channel.")
    async def spam_ping(self, interaction:discord.Interaction, recipient:discord.Member, count:int, message:str):
        sender = interaction.user

        embed = discord.Embed(title = f"Spam pinging this channel:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Recipient:", value = recipient.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = message, inline = False)

        await interaction.response.send_message(embed = embed)

        countAt:int = 0

        while countAt < count:
            countAt += 1
            await interaction.channel.send(f"{str(recipient.mention)} {message}")

async def setup(bot: commands.Bot):
    await bot.add_cog(SpamPingCog(bot))