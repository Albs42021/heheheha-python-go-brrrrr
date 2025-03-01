from discord.ext import commands
import discord
from discord import app_commands
import datetime

class DMCog(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @app_commands.command(description="DMs one or more people on this server.")
    @app_commands.describe(recipients="Mention the users to DM")
    async def dm(self, interaction: discord.Interaction, message: str, recipients: str):
        sender = interaction.user

        # Convert user mentions into Member objects
        recipients_list = []
        for mention in recipients.split():
            member_id = mention.strip("<@!>")
            if member_id.isdigit():
                member = interaction.guild.get_member(int(member_id))
                if member:
                    recipients_list.append(member)

        if not recipients_list:
            await interaction.response.send_message("No valid recipients found. Please mention the users.", ephemeral=True)
            return

        # Create the DM embed
        DMembed = discord.Embed(
            title="You have been sent a DM:",
            timestamp=datetime.datetime.utcnow(),
            color=0x0000FF
        )
        DMembed.add_field(name="Author:", value=sender.mention, inline=False)
        DMembed.add_field(name="Message:", value=message, inline=False)

        # Send DM to each recipient
        for recipient in recipients_list:
            try:
                await recipient.send(embed=DMembed)
            except discord.Forbidden:
                await interaction.response.send_message(f"Could not DM {recipient.mention}. They may have DMs disabled.", ephemeral=True)
                return

        # Create the confirmation embed
        Serverembed = discord.Embed(
            title="DM Sent:",
            timestamp=datetime.datetime.utcnow(),
            color=0x0000FF
        )
        Serverembed.add_field(name="Recipients:", value=", ".join([r.mention for r in recipients_list]), inline=False)
        Serverembed.add_field(name="Author:", value=sender.mention, inline=False)

        await interaction.response.send_message(embed=Serverembed)

async def setup(bot: commands.bot):
    await bot.add_cog(DMCog(bot))