import discord
from discord.ext import commands
import sqlite3

# Database setup
conn = sqlite3.connect("xp.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, xp INTEGER)")

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # XP update
    cursor.execute("SELECT xp FROM users WHERE id=?", (message.author.id,))
    row = cursor.fetchone()
    if row:
        xp = row[0] + 10  # 10 XP per message
        cursor.execute("UPDATE users SET xp=? WHERE id=?", (xp, message.author.id))
    else:
        xp = 10
        cursor.execute("INSERT INTO users (id, xp) VALUES (?, ?)", (message.author.id, xp))
    conn.commit()

    await bot.process_commands(message)

@bot.command()
async def rank(ctx):
    cursor.execute("SELECT xp FROM users WHERE id=?", (ctx.author.id,))
    row = cursor.fetchone()
    xp = row[0] if row else 0

    embed = discord.Embed(
        title="📊 Rank Info",
        description=f"{ctx.author.mention}, your XP is:",
        color=discord.Color.blue()
    )
    embed.add_field(name="XP", value=f"**{xp}**", inline=False)
    embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)

    await ctx.send(embed=embed)

@bot.command()
async def leaderboard(ctx):
    cursor.execute("SELECT id, xp FROM users ORDER BY xp DESC LIMIT 5")
    rows = cursor.fetchall()

    embed = discord.Embed(
        title="🏆 Rialo Leaderboard",
        description="Top 5 Active Members",
        color=discord.Color.gold()
    )

    if rows:
        for i, row in enumerate(rows):
            user = await bot.fetch_user(row[0])
            embed.add_field(
                name=f"{i+1}. {user.name}",
                value=f"XP: **{row[1]}**",
                inline=False
            )
    else:
        embed.description = "No data yet 😢"

    embed.set_footer(text="Keep chatting to earn XP!")
    await ctx.send(embed=embed)

bot.run("your bot token")
