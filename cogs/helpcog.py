from discord.ext import commands
import discord
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gives you all the bots commands.")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title = f"Help:", timestamp = discord.utils.utcnow(), color = 0xFFFF00)

        embed.add_field(name = "/ban:", value = "Bans someone from this discord server.", inline = False)

        embed.add_field(name = "/calculator:", value = "Gives you a calculator.", inline = False)

        embed.add_field(name = "/define:", value = "Defines a word.", inline = False)

        embed.add_field(name = "/dm:", value = "DM's someone on this server.", inline = False)

        embed.add_field(name = "/generate_invite:", value = "Generates an invite link to this discord server.", inline = False)

        embed.add_field(name = "/id:", value = "Gets the id of a member of this discord server.", inline = False)

        embed.add_field(name = "/joke:", value = "Gives you a joke.", inline = False)

        embed.add_field(name = "/kick:", value = "Kicks someone from this discord server.", inline = False)

        embed.add_field(name = "/meme:", value = "Gives you a meme.", inline = False)

        embed.add_field(name = "/mute:", value = "Mutes someone on this discord server.", inline = False)

        embed.add_field(name = "/ping:", value = "Gives you the bot's ping.", inline = False)

        embed.add_field(name = "/roast:", value = "Gives you a roast.", inline = False)

        embed.add_field(name = "/roast_dm:", value = "Roasts someone in their DMs.", inline = False)

        embed.add_field(name = "/say:", value = "Makes the bot say something.", inline = False)

        embed.add_field(name = "/snipe_delete:", value = "Gives you the last deleted message.", inline = False)

        embed.add_field(name = "/snipe_edit:", value = "Gives you the last edited message.", inline = False)

        embed.add_field(name = "/spam:", value = "Spams this channel.", inline = False)

        embed.add_field(name = "/spam_dm:", value = "Spams the DM's of someone in this server.", inline = False)

        embed.add_field(name = "/spam_ping:", value = "Spam pings someone on this channel.", inline = False)

        embed.add_field(name = "/spam_ping_dm:", value = "Spam pings the DM's of someone in this server.", inline = False)

        embed.add_field(name = "/trivia:", value = "Gives you a trivia question.", inline = False)

        embed.add_field(name = "/unban:", value = "Unbans someone from this discord server.", inline = False)
        
        embed.add_field(name = "/unmute:", value = "Unmutes someone on this discord server.", inline = False)

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))