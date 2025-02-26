from discord.ext import commands
import discord
from discord import app_commands
import typing
import html
import random

class TriviaCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.typeList = ["Any", "General Knowledge", "Books", "Movies", "Music", "Musicals & Theater", "TV", "Video Games", "Board Games", "Science & Nature", "Computers", "Math", "Mythology", "Sports", "Geogrphy", "History", "Politics", "Art", "Celebreties", "Animals", "Vehicles", "Comics", "Gadgets", "Anime & Manga", "Cartoons & Animations"]

    @app_commands.command(description = "Gives you a trivia question.")
    async def trivia(self, interaction: discord.Interaction, difficulty:typing.Literal["Any", "Easy", "Medium", "Hard"], type:typing.Literal["Any", "Multiple Choice", "True / False"], category:typing.Literal["Any", "General Knowledge", "Books", "Movies", "Music", "Musicals & Theater", "TV", "Video Games", "Board Games", "Science & Nature", "Computers", "Math", "Mythology", "Sports", "Geogrphy", "History", "Politics", "Art", "Celebreties", "Animals", "Vehicles", "Comics", "Gadgets", "Anime & Manga", "Cartoons & Animations"]):
        categoryInt:int = self.typeList.index(category) + 8

        difficultyStr:str = difficulty.lower()

        typeStr1:str = type.lower()

        typeStr2 = None

        if typeStr1 == "multiple choice":
            typeStr2 = "multiple"

        elif typeStr1 == "true / false":
            typeStr2 = "boolean"

        else:
            typeStr2 = "any"

        if categoryInt == 8:
            if difficultyStr == "any":
                if typeStr2 == "any":
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1")

                else:
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&type={typeStr2}")
            
            else:
                if typeStr2 == "any":
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyStr}")

                else:
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyStr}&type={typeStr2}")

        else:
            if difficultyStr == "any":
                if typeStr2 == "any":
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&category={str(categoryInt)}")

                else:
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&category={str(categoryInt)}&type={typeStr2}")
            
            else:
                if typeStr2 == "any":
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&category={str(categoryInt)}&difficulty={difficultyStr}")

                else:
                    url = await self.bot.session.get(f"https://opentdb.com/api.php?amount=1&category={str(categoryInt)}&difficulty={difficultyStr}&type={typeStr2}")

        json = await url.json()

        results = json.get("results")

        question = results[0].get("question")

        questionType = results[0].get("type")

        questionTypeStr = None

        if questionType == "boolean":
            questionTypeStr = "True / False"

        else:
            questionTypeStr = "Multiple Choice"


        questionCategory = results[0].get("category")

        questionDifficulty = results[0].get("difficulty")

        answers = []

        wrongAnswers = results[0].get("incorrect_answers")

        answers += wrongAnswers

        rightAnswer = results[0].get("correct_answer")

        answers.append(rightAnswer)

        triviaEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        triviaEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

        triviaEmbed.add_field(name = "Category:", value = questionCategory.capitalize(), inline = False)

        triviaEmbed.add_field(name = "Difficulty:", value = questionDifficulty.capitalize(), inline = False)

        triviaEmbed.add_field(name = "Type:", value = questionType.capitalize(), inline = False)

        triviaEmbed.add_field(name = "Question:", value = html.unescape(question), inline = False)

        if questionType == "multiple":
            random.shuffle(answers)

        else:
            for answer in answers:
                if answer == "True":
                    answerIndex = answers.index(answer)
                    answers.pop(answerIndex)
                    answers.insert(0, answer)

        if questionType == "multiple":
            class buttons(discord.ui.View):
                @discord.ui.button(label=html.unescape(answers[0]), style=discord.ButtonStyle.primary)
                async def button_callback1(self, interaction:discord.Interaction, button):
                    if answers[0] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

                @discord.ui.button(label=html.unescape(answers[1]), style=discord.ButtonStyle.primary)
                async def button_callback2(self, interaction:discord.Interaction, button):
                    if answers[1] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

                @discord.ui.button(label=html.unescape(answers[2]), style=discord.ButtonStyle.primary)
                async def button_callback3(self, interaction:discord.Interaction, button):
                    if answers[2] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

                @discord.ui.button(label=html.unescape(answers[3]), style=discord.ButtonStyle.primary)
                async def button_callback4(self, interaction:discord.Interaction, button):
                    if answers[3] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

        else:
            class buttons(discord.ui.View):
                @discord.ui.button(label=html.unescape(answers[0]), style=discord.ButtonStyle.primary)
                async def button_callback1(self, interaction:discord.Interaction, button):
                    if answers[0] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

                @discord.ui.button(label=html.unescape(answers[1]), style=discord.ButtonStyle.primary)
                async def button_callback2(self, interaction:discord.Interaction, button):
                    if answers[1] == rightAnswer:
                        correctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        correctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        correctEmbed.add_field(name = "You are:", value = "Correct.", inline = False)

                        await interaction.response.send_message(embed = correctEmbed)

                    else:
                        incorerctEmbed = discord.Embed(title = "Trivia:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                        incorerctEmbed.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                        incorerctEmbed.add_field(name = "You are:", value = "Incorrect.", inline = False)

                        await interaction.response.send_message(embed = incorerctEmbed)

        buttons = buttons()
        
        await interaction.response.send_message(embed = triviaEmbed)

        await interaction.channel.send(view = buttons)

        trivia = commands.Cog.get_app_commands('trivia')

        await trivia()


async def setup(bot: commands.Bot):
    await bot.add_cog(TriviaCog(bot))