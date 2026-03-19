import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def تقديم(ctx):
    await ctx.send("اسمك؟")
    def check(m): return m.author == ctx.author
    name = await bot.wait_for('message', check=check)

    await ctx.send("عمرك؟")
    age = await bot.wait_for('message', check=check)

    await ctx.send("خبراتك؟")
    exp = await bot.wait_for('message', check=check)

    await ctx.send("هل لديك خبرات سابقة؟")
    prev = await bot.wait_for('message', check=check)

    await ctx.send(f"""
تم استلام تقديمك ✅

الاسم: {name.content}
العمر: {age.content}
الخبرات: {exp.content}
خبرات سابقة: {prev.content}
""")

bot.run(os.getenv("TOKEN"))
