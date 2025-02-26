from discord.ext import commands
import discord
from discord import app_commands

class DefineCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description = "Defines a word.")
    async def define(self, interaction:discord.Interaction, word:str):
        req = await self.bot.session.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        json = await req.json()

        try:
            if json.get("title"):
                return await interaction.response.send_message(f"Invalid word received: {word}")
        except:
            await interaction.response.send_message("Definition found.")

        definitions = json[0]["meanings"]

        embed = discord.Embed(title = f"Definition(s) of {word}", timestamp = discord.utils.utcnow(), color = 0x0000FF)
        
        for pack in definitions:
            d = ""
            for definition in pack["definitions"]:
                d += f"Definition: {definition['definition']}\n"
            
            embed.add_field(name = pack["partOfSpeech"], value = d, inline = False)

        await interaction.channel.send(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(DefineCog(bot))