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


@bot.command(name="convert", help="jud convert *value* *base unit* *wanted unit* --> *converted value* *wanted unit*")
async def convert_command(ctx: discord.ext.commands.context.Context, to_convert: float, unit_from: str, unit_to: str):
    if meter.__contains__(unit_from.lower()) and unit_to.lower() == "idil":
        result: float = to_convert / 1.6
        string = "%s mètre(s) = %s Idil(s)"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "idil" and meter.__contains__(unit_to.lower()):
        result: float = to_convert * 1.6
        string = "%s Idil(s) = %s mètre(s)"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "w" and unit_to.lower() == "robert":
        result: float = to_convert / 700
        string = "%s W = %s Robert"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "w" and unit_from.lower() == "robert":
        result: float = to_convert * 700
        string = "%s Robert = %s W"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "kg" and unit_to.lower() == "robert":
        result: float = to_convert / 120
        string = "%s kg = %s Robert"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "kg" and unit_from.lower() == "robert":
        result: float = to_convert * 120
        string = "%s Robert = %s kg"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "kwh" and unit_to.lower() == "juif":
        result: float = to_convert
        string = "%s kWh = %s Juif"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "kwh" and unit_from.lower() == "juif":
        result: float = to_convert
        string = "%s Juif = %s kWh"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "iq" and unit_to.lower() == "bougrine":
        result: float = to_convert / 200
        string = "%s IQ = %s Bougrine"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "iq" and unit_from.lower() == "bougrine":
        result: float = to_convert * 200
        string = "%s Bougrine = %s IQ"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "iq" and unit_to.lower() == "matthieu":
        result: float = (to_convert * 0.9) / 200
        string = "%s IQ = %s Matthieu"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "iq" and unit_from.lower() == "matthieu":
        result: float = (to_convert * 200) / 0.9
        string = "%s Matthieu = %s IQ"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "h" and unit_to.lower() == "juif":
        result: float = to_convert
        string = "%s h = %s Juif"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "h" and unit_from.lower() == "juif":
        result: float = to_convert
        string = "%s Juif = %s h"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "km/h" and unit_to.lower() == "fastaf":
        result: float = to_convert / 69
        string = "%s km/h = %s Fast AF"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "km/h" and unit_from.lower() == "fastaf":
        result: float = to_convert * 69
        string = "%s Fast AF = %s km/h"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "km/h" and unit_to.lower() == "fast_af":
        result: float = to_convert / 69
        string = "%s km/h = %s Fast AF"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "km/h" and unit_from.lower() == "fast_af":
        result: float = to_convert * 69
        string = "%s Fast AF = %s km/h"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "c" and unit_to.lower() == "jenifer_aniston":
        result: float = to_convert / 63
        string = "%s °C = %s Jenifer Aniston"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "c" and unit_from.lower() == "jenifer_aniston":
        result: float = to_convert * 63
        string = "%s Jenifer Aniston = %s °C"
        await ctx.send(content=string % (to_convert, result))

    if unit_from.lower() == "c" and unit_to.lower() == "juif":
        result: float = to_convert / 121
        string = "%s °C = %s Juif"
        await ctx.send(content=string % (to_convert, result))

    if unit_to.lower() == "c" and unit_from.lower() == "juif":
        result: float = to_convert * 121
        string = "%s Juif = %s °C"
        await ctx.send(content=string % (to_convert, result))


@bot.command(name="fbi", help="Dites bonjour au FBI ! ")
async def fbi_command(ctx: discord.ext.commands.context.Context):
    await ctx.send(content="***___FBI OPEN UP!!___***")

@bot.command(name="inculte", help="Arrête de jouer et va lire !")
async def inculte_command(ctx: discord.ext.commands.context.Context):
    await ctx.send(content="***__INCUUULTEE !!__***")

bot.run(TOKEN)
