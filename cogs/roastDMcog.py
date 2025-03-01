from discord.ext import commands
import discord
from discord import app_commands
class RoastDMCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gives you a roast.")
    async def roast_dm(self, interaction: discord.Interaction, recipiant: discord.Member):
        sender = interaction.user

        url = await self.bot.session.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

        json = await url.json()

        roast = json.get("insult")

        dmEmbed = discord.Embed(title = "Roast DM:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        dmEmbed.add_field(name = "Sent By:", value = sender.mention, inline = False)

        dmEmbed.add_field(name = "Recipiant", value = recipiant.mention, inline = False)

        dmEmbed.add_field(name = "Roast:", value = roast, inline = False)

        await recipiant.send(embed = dmEmbed)

        serverEmbed = discord.Embed(title = "Roast DM:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        serverEmbed.add_field(name = "Sent By:", value = sender.mention, inline = False)

        serverEmbed.add_field(name = "Recipiant", value = recipiant.mention, inline = False)

        await interaction.response.send_message(embed = serverEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(RoastDMCog(bot))