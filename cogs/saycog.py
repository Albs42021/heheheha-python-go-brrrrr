from discord.ext import commands
import discord
from discord import app_commands

class SayCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Makes the bot say something.")
    async def say(self, interaction:discord.Interaction):
        def check(msg: discord.Message):
            return msg.author == interaction.user

        await interaction.response.send_message('What should I say?')

        message = await self.bot.wait_for('message', check = check, timeout = 20)

        if message is None:
            return await interaction.channel.send('Nothing was said.')

        await interaction.channel.send(message.content)

async def setup(bot: commands.Bot):
    await bot.add_cog(SayCog(bot))