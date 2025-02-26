from discord.ext import commands
import discord
from discord import app_commands
class JokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description = "Gives you a joke.")
    async def joke(self, interaction: discord.Interaction):
        r = await self.bot.session.get("https://v2.jokeapi.dev/joke/Any?format=txt")

        joke = await r.text()

        embed = discord.Embed(title = "Joke:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        embed.add_field(name = "Joke:", value = joke, inline = False)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(JokeCog(bot))