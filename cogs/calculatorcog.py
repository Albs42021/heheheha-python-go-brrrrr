from discord.ext import commands
import discord
import math
from discord import app_commands

class CalculatorCog(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    @app_commands.command(description = "Gives you a calculator.")
    async def calculator(self, interaction:discord.Interaction):
        def check(msg: discord.Message):
            return msg.author == interaction.user
        
        embed1 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

        embed1.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

        embed1.add_field(name = "What operation should I preform?", value = "", inline = False)

        await interaction.response.send_message(embed = embed1)

        operationMessage = await self.bot.wait_for('message', check = check, timeout = 20)

        operation = operationMessage.content
        
        if operation == "Mean" or operation == "mean" or operation == "average" or operation == "Average":
            embed2 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed2.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

            embed2.add_field(name = "Operation:", value = "Mean", inline = False)

            embed2.add_field(name = "How many numbers are to be averaged?", value = "", inline = False)

            await operationMessage.reply(embed = embed2)

            amount = await self.bot.wait_for('message', check = check, timeout = 20)

            total:int = 0

            count:int = 0

            average:int = 0

            numbers = []

            numbersList:str = ""
            
            while count < int(amount.content):
                if count == 0:
                    embed3 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                    embed3.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                    embed3.add_field(name = "Operation:", value = "Mean", inline = False)
            
                    embed3.add_field(name = "Amount of numbers being averaged:", value = amount.content, inline = False)
            
                    embed3.add_field(name = "Please enter a number to be averaged.", value = "", inline = False)

                    await amount.reply(embed = embed3)

                    number = await self.bot.wait_for('message', check = check, timeout = 20)

                    numbers.append(number.content)

                    numbersList = ""

                    numbersListCount = 0

                    for n in numbers:
                        numbersListCount += 1

                        if numbersListCount == count + 1:
                            numbersList = numbersList + n

                        else:
                            numbersList = numbersList + n + ", "

                    total += int(number.content)

                    count += 1
                    
                else:
                    embed4 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

                    embed4.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)

                    embed4.add_field(name = "Operation:", value = "Mean", inline = False)
            
                    embed4.add_field(name = "Amount of numbers being averaged:", value = amount.content, inline = False)

                    embed4.add_field(name = "Numbers entered:", value = numbersList, inline = False)
            
                    embed4.add_field(name = "Please enter another number to be averaged.", value = "", inline = False)

                    await number.reply(embed = embed4)
                    
                    number = await self.bot.wait_for('message', check = check, timeout = 20)

                    numbers.append(number.content)

                    numbersList = ""

                    numbersListCount = 0

                    for n in numbers:
                        numbersListCount += 1

                        if numbersListCount == count + 1:
                            numbersList = numbersList + n

                        else:
                            numbersList = numbersList + n + ", "

                    total += int(number.content)

                    count += 1

            average = total / int(amount.content)

            embed5 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed5.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed5.add_field(name = "Operation:", value = "Mean", inline = False)
    
            embed5.add_field(name = "Amount:", value = amount.content, inline = False)
                                    
            embed5.add_field(name = "Numbers entered:", value = numbersList, inline = False)

            embed5.add_field(name = "Sum:", value = total, inline = False)
    
            embed5.add_field(name = "Answer:", value = "The mean is " + str(average), inline = False)

            await number.reply(embed = embed5)
        
        elif operation == "log" or operation == "Log" or operation == "logarithim" or operation == "Logarithim" or operation == "logarithims" or operation == "Logarithims":
            embed6 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed6.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed6.add_field(name = "Operation:", value = "Log", inline = False)
    
            embed6.add_field(name = "Please enter the logbase.", value = "", inline = False)

            await operationMessage.reply(embed = embed6)

            logbase = await self.bot.wait_for('message', check = check, timeout = 20)

            embed7 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed7.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed7.add_field(name = "Operation:", value = "Log", inline = False)

            embed7.add_field(name = "Logbase:", value = logbase.content, inline = False)
    
            embed7.add_field(name = "Please enter the argument.", value = "", inline = False)

            await logbase.reply(embed = embed7)

            number = await self.bot.wait_for('message', check = check, timeout = 20)

            embed8 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed8.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed8.add_field(name = "Operation:", value = "Log", inline = False)

            embed8.add_field(name = "Logbase:", value = logbase.content, inline = False)

            embed8.add_field(name = "Argument:", value = number.content, inline = False)
    
            embed8.add_field(name = "Answer:", value = "Log " + str(logbase.content) + ", " + str(number.content) + " = " + str(math.log(float(int(number.content)), float(int(logbase.content)))), inline = False)

            await interaction.response.send_message(embed = embed8)

        elif operation == "+" or operation == "add" or operation == "Add" or operation == "Addition" or operation == "addition" or operation == "plus" or operation == "Plus":
            embed9 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed9.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed9.add_field(name = "Operation:", value = "Addition", inline = False)
    
            embed9.add_field(name = "Please enter the first addend.", value = "", inline = False)

            await operationMessage.reply(embed = embed9)

            first_addend = await self.bot.wait_for('message', check = check, timeout = 20)

            embed10 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed10.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed10.add_field(name = "Operation:", value = "Addition", inline = False)

            embed10.add_field(name = "First addend:", value = first_addend.content, inline = False)
    
            embed10.add_field(name = "Please enter the second addend.", value = "", inline = False)

            await first_addend.reply(embed = embed10)

            second_addend = await self.bot.wait_for('message', check = check, timeout = 20)

            sum:int = int(first_addend.content) + int(second_addend.content)

            embed11 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed11.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed11.add_field(name = "Operation:", value = "Addition", inline = False)

            embed11.add_field(name = "First addend:", value = first_addend.content, inline = False)

            embed11.add_field(name = "Second addend:", value = second_addend.content, inline = False)

            embed11.add_field(name = "Answer:", value = str(first_addend.content) + " + " + str(second_addend.content) + " = " + str(sum), inline = False)

            await interaction.response.send_message(embed = embed11)

        elif operation == "-" or operation == "–" or operation == "minus" or operation == "Minus" or operation == "Subtraction" or operation == "subtraction" or operation == "subtract" or operation == "Subtract":
            embed12 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed12.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed12.add_field(name = "Operation:", value = "Subtraction", inline = False)
    
            embed12.add_field(name = "Please enter the minuend.", value = "", inline = False)

            await operationMessage.reply(embed = embed12)

            minuend = await self.bot.wait_for('message', check = check, timeout = 20)
            
            embed13 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed13.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed13.add_field(name = "Operation:", value = "Subtraction", inline = False)

            embed13.add_field(name = "Minuend:", value = minuend.content, inline = False)
    
            embed13.add_field(name = "Please enter the subtrahend.", value = "", inline = False)

            await minuend.reply(embed = embed13)

            subtrahend = await self.bot.wait_for('message', check = check, timeout = 20)

            difference:int = int(minuend.content) - int(subtrahend.content)

            embed14 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed14.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed14.add_field(name = "Operation:", value = "Subtraction", inline = False)

            embed14.add_field(name = "Minuend:", value = minuend.content, inline = False)

            embed14.add_field(name = "Subtrahend:", value = subtrahend.content, inline = False)
    
            embed14.add_field(name = "Answer:", value = str(minuend.content) + " - " + str(subtrahend.content) + " = " + str(difference), inline = False)

            await interaction.response.send_message(embed = embed14)

        elif operation == "x" or operation == "X" or operation == "*" or operation == "times" or operation == "Times" or operation == "multiply" or operation == "Multiply" or operation == "multiplication" or operation == "Multiplication" or operation == "×":   
            embed15 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed15.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed15.add_field(name = "Operation:", value = "Multiplication", inline = False)
    
            embed15.add_field(name = "Please enter the first factor.", value = "", inline = False)

            await operationMessage.reply(embed = embed15)

            first_factor = await self.bot.wait_for('message', check = check, timeout = 20)

            embed16 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed16.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed16.add_field(name = "Operation:", value = "Multiplication", inline = False)

            embed16.add_field(name = "First factor:", value = first_factor.content, inline = False)
    
            embed16.add_field(name = "Please enter the second factor.", value = "", inline = False)

            await first_factor.reply(embed = embed16)

            second_factor = await self.bot.wait_for('message', check = check, timeout = 20)

            product:int = int(first_factor.content) * int(second_factor.content)

            embed17 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed17.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed17.add_field(name = "Operation:", value = "Multiplication", inline = False)

            embed17.add_field(name = "First factor:", value = first_factor.content, inline = False)

            embed17.add_field(name = "Second factor:", value = second_factor.content, inline = False)
    
            embed17.add_field(name = "Answer:", value = str(first_factor.content) + " × " + str(second_factor.content) + " = " + str(product), inline = False)

            await interaction.response.send_message(embed = embed17)

        elif operation == "/" or operation == "÷" or operation == "divide" or operation == "Divide" or operation == "division" or operation == "Division":
            embed18 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed18.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed18.add_field(name = "Operation:", value = "Division", inline = False)

            embed18.add_field(name = "Please enter the dividend.", value = "", inline = False)

            await operationMessage.reply(embed = embed18)

            dividend = await self.bot.wait_for('message', check = check, timeout = 20)

            embed19 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed19.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed19.add_field(name = "Operation:", value = "Division", inline = False)

            embed19.add_field(name = "Dividend:", value = dividend.content, inline = False)

            embed19.add_field(name = "Please enter the divisor.", value = "", inline = False)

            await dividend.reply(embed = embed19)

            divisor = await self.bot.wait_for('message', check = check, timeout = 20) 

            quotient:int = int(dividend.content) / int(divisor.content)

            embed20 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed20.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed20.add_field(name = "Operation:", value = "Division", inline = False)

            embed20.add_field(name = "Dividend:", value = dividend.content, inline = False)

            embed20.add_field(name = "Divisor:", value = divisor.content, inline = False)

            embed20.add_field(name = "Answer:", value = str(dividend.content) + " ÷ " + str(divisor.content) + " = " + str(quotient), inline = False)

            await interaction.response.send_message(embed = embed20)

        elif operation == "^" or operation == "exponent" or operation == "Exponent" or operation == "exponents" or operation == "Exponents" or operation == "power" or operation == "Power" or operation == "powers" or operation == "Powers":
            embed21 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed21.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed21.add_field(name = "Operation:", value = "Exponent", inline = False)

            embed21.add_field(name = "Please enter the base.", value = "", inline = False)
            
            await operationMessage.reply(embed = embed21)

            base = await self.bot.wait_for('message', check = check, timeout = 20)

            embed22 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed22.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed22.add_field(name = "Operation:", value = "Exponent", inline = False)

            embed22.add_field(name = "Base:", value = base.content, inline = False)

            embed22.add_field(name = "Please enter the exponent.", value = "", inline = False)

            await base.reply(embed = embed22)

            exponent = await self.bot.wait_for('message', check = check, timeout = 20) 

            power:int = int(base.content) ** int(exponent.content)

            embed23 = discord.Embed(title = f"Calculator:", timestamp = discord.utils.utcnow(), color = 0x0000FF)

            embed23.add_field(name = "Requested by:", value = interaction.user.mention, inline = False)  
                               
            embed23.add_field(name = "Operation:", value = "Exponent", inline = False)

            embed23.add_field(name = "Base:", value = base.content, inline = False)

            embed23.add_field(name = "Exponent:", value = base.content, inline = False)

            embed23.add_field(name = "Answer:", value = str(base.content) + " ^ " + str(exponent.content) + " = " + str(power), inline = False)

            await interaction.response.send_message(embed = embed23)

        else:
            await interaction.response.send_message("Invalid operation.")

async def setup(bot: commands.Bot):
    await bot.add_cog(CalculatorCog(bot))