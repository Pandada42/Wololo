import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

bot = commands.Bot(command_prefix="jud ")

print("Lecture en Cours de la Bible Judigniste")

meter = ["m", "mètre", "meter"]


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        break


@bot.command(name="convert", help="")
async def convert_command(ctx: discord.ext.commands.context.Context, to_convert: float, unit_from: str, unit_to: str):
    if meter.__contains__(unit_from.lower()) and unit_to.lower() == "idil":
        result: float = to_convert / 1.6
        string = "%s mètre(s) = %s Idil(s)"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "idil" and meter.__contains__(unit_to.lower()):
        result: float = to_convert * 1.6
        string = "%s Idil(s) = %s mètre(s)"
        await ctx.send(content=string % (to_convert, result))


@bot.command(name="fbi", help="")
async def fbi_command(ctx: discord.ext.commands.context.Context):
    await ctx.send(content="***___FBI OPEN UP!!___***")


bot.run(TOKEN)
