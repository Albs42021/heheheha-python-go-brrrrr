from discord.ext import commands
import discord
from discord import app_commands

class SnipeEditCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        
        bot.last_edited_message_before = None
        bot.last_edited_message_after = None

    @app_commands.command(description = "Gives you the last edited message.")
    async def snipe_edit(self, interaction:discord.Interaction):
        server = interaction.guild

        if self.bot.last_edited_message_before == None or self.bot.last_edited_message_after == None:
            return await interaction.response.send_message("There is no edited message to snipe.")
                
        embed = discord.Embed(title = f"Snipe edit:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Author:", value = self.bot.last_edited_message_before.author.mention, inline = False)

        embed.add_field(name = "Before:", value = self.bot.last_edited_message_before.content, inline = False)

        embed.add_field(name = "After:", value = self.bot.last_edited_message_after.content, inline = False)
        
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(SnipeEditCog(bot))