from discord.ext import commands
import discord
from discord import app_commands

class SpamPingDMCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Spam pings the DM's of someone in this server.")
    async def spam_ping_dm(self, interaction:discord.Interaction, recipients: str, count:int, message:str):
        sender = interaction.user

        # Convert user mentions into Member objects
        recipients_list = []
        for mention in recipients.split():
            member_id = mention.strip("<@!>")
            if member_id.isdigit():
                member = interaction.guild.get_member(int(member_id))
                if member:
                    recipients_list.append(member)

        embed = discord.Embed(title = f"Spam pinging DM's:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name="Recipients:", value=", ".join([r.mention for r in recipients_list]), inline=False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = f"{", ".join([r.mention for r in recipients_list])} {message}", inline = False)

        await interaction.response.send_message(embed = embed)

        embed = discord.Embed(title = f"Your DM's are getting spam pinged:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed.add_field(name = "Server:", value = interaction.guild.name, inline = False)

        embed.add_field(name = "Requested by:", value = sender.mention, inline = False)

        embed.add_field(name = "Count:", value = str(count), inline = False)

        embed.add_field(name = "Message:", value = f"{", ".join([r.mention for r in recipients_list])} {message}", inline = False)
        
        # Spam each recipient
        for recipient in recipients_list:
            countAt:int = 0

            try:
                await recipient.send(f"{sender.mention} is spam pinging your DMs.")

                while countAt < count:
                    countAt += 1
                    await recipient.send(recipient.mention + " " + message)

            except discord.Forbidden:
                await interaction.response.send_message(f"Could not DM {recipient.mention}. They may have DMs disabled.", ephemeral=True)
                return

async def setup(bot: commands.Bot):
    await bot.add_cog(SpamPingDMCog(bot))