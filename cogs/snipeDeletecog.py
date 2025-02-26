from discord.ext import commands
import discord
from discord import app_commands

class SnipeDeleteCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        bot.last_deleted_message = None

    @app_commands.command(description = "Gives you the last deleted message.")
    async def snipe_delete(self, interaction:discord.Interaction):
        server = interaction.guild

        if self.bot.last_deleted_message == None:
            return await interaction.response.send_message("There is no deleted message to snipe.")
        
        embed = discord.Embed(title = f"Snipe:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Author:", value = self.bot.last_deleted_message.author.mention, inline = False)

        embed.add_field(name = "Message:", value = self.bot.last_deleted_message.content, inline = False)
        
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(SnipeDeleteCog(bot))