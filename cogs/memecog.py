from discord.ext import commands
import discord
from discord import app_commands
class MemeCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gives you a meme.")
    async def meme(self, interaction: discord.Interaction, subreddit:str = "memes"):
        url = await self.bot.session.get(f"https://meme-api.com/gimme/{subreddit}/1")

        json = await url.json()

        memes = json.get("memes")

        link = memes[0].get("postLink")

        title = memes[0].get("title")

        meme = memes[0].get("url")

        author = memes[0].get("author")

        embed = discord.Embed(title = "Meme:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        embed.add_field(name = "Title:", value = title, inline = False)

        embed.add_field(name = "Meme:", value = meme, inline = False)

        embed.add_field(name = "Author:", value = author, inline = False)

        embed.add_field(name = "Link:", value = link, inline = False)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(MemeCog(bot))