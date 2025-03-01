from discord.ext import commands
import discord
from discord import app_commands
class RoastCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gives you a roast.")
    async def roast(self, interaction: discord.Interaction):
        url = await self.bot.session.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

        json = await url.json()

        roast = json.get("insult")

        embed = discord.Embed(title = "Roast:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        embed.add_field(name = "Roast:", value = roast, inline = False)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(RoastCog(bot))