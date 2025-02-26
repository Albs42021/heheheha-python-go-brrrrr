from discord.ext import commands
import discord
from discord import app_commands

class SpamCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Spams this channel.")
    async def spam(self, interaction:discord.Interaction, count:int, message:str):
        embed = discord.Embed(title = f"Spamming this channel:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = message, inline = False)

        await interaction.response.send_message(embed = embed)
    
        countAt:int = 0
        
        while countAt < count:
            countAt += 1
            await interaction.channel.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(SpamCog(bot))