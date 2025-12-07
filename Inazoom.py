import discord
from discord import app_commands
from discord.ext import commands
from discord import ui, Embed, Interaction

import csv

data = []

def load_csv():
    global data
    with open("players.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

class PlayerPaginator(ui.View):
    def __init__(self, matches):
        super().__init__(timeout=180)
        self.matches = matches
        self.index = 0

    def create_embed(self):
        row = self.matches[self.index]
        embed = Embed(
            title=f"{row['localisedname']} ({row['romajiname']})",
            description=(
                f"**Kanji:** {row['kanjiname']}\n"
                f"**Hiragana:** {row['hiragananame']}\n"
                f"**Nickname:** {row['nickname']}\n\n"
                f"**Position:** {row['position']}\n"
                f"**Element:** {row['element']}\n"
                f"**Playstyle:** {row['playstyle']}\n\n"
                f"**Stats:**\n"
                f"Kick: {row['kick']}\n"
                f"Control: {row['control']}\n"
                f"Technique: {row['technique']}\n"
                f"Pressure: {row['pressure']}\n"
                f"Physical: {row['physical']}\n"
                f"Agility: {row['agility']}\n"
                f"Intelligence: {row['intelligence']}\n"
                f"**BST:** {row['bst']}\n\n"
                f"*Player {self.index + 1} of {len(self.matches)}*"
            ),
            color=0x00AEEF
        )
        if row.get("image"):
            embed.set_image(url=row["image"])
        return embed

    @ui.button(emoji="⬅️", style=discord.ButtonStyle.secondary)
    async def previous(self, interaction: Interaction, button: ui.Button):
        self.index = (self.index - 1) % len(self.matches)
        await interaction.response.edit_message(embed=self.create_embed(), view=self)

    @ui.button(emoji="➡️", style=discord.ButtonStyle.secondary)
    async def next(self, interaction: Interaction, button: ui.Button):
        self.index = (self.index + 1) % len(self.matches)
        await interaction.response.edit_message(embed=self.create_embed(), view=self)


TOKEN = "EXAMPLETOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    load_csv()
    print("CSV Loaded!")
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.tree.command(
    name="player",
    description="Search for a player by name (kanji, romaji, nickname, etc.)"
)
async def player(interaction: discord.Interaction, name: str):
    name = name.lower().strip()

    matches = [
        row for row in data
        if (
            name in row["kanjiname"].lower() or
            name in row["hiragananame"].lower() or
            name in row["romajiname"].lower() or
            name in row["localisedname"].lower() or
            name in row["nickname"].lower()
        )
    ]

    if not matches:
        await interaction.response.send_message("Player not found.")
        return

    paginator = PlayerPaginator(matches)
    embed = paginator.create_embed()
    embed.set_footer(text="Credit to @Xion for dataset: https://docs.google.com/spreadsheets/d/1N4h7z27Rxq3bvYuR9VyeQv3Ze-zwo-1XZQTd9rZa-Zs/edit?usp=sharing")
    
    await interaction.response.send_message(embed=embed, view=paginator)

bot.run(TOKEN)
