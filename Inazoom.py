import discord
from discord import app_commands
from discord.ext import commands
from discord import ui, Embed, Interaction
from discord.app_commands import Choice
from typing import Optional

import csv

data = []

TOKEN = "Example"

def load_csv():
    global data
    with open("players.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

positions = set()
elements = set()
playstyles = set()

def build_categories():
    global positions, elements, playstyles
    positions = set()
    elements = set()
    playstyles = set()

    for row in data:
        if row["position"]:
            positions.add(row["position"])
        if row["element"]:
            elements.add(row["element"])
        if row["playstyle"]:
            playstyles.add(row["playstyle"])


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

async def autocomplete_position(interaction, current: str):
    current = current.lower()
    return [
        Choice(name=p, value=p)
        for p in sorted(positions)
        if current in p.lower()
    ][:25]

async def autocomplete_element(interaction, current: str):
    current = current.lower()
    return [
        Choice(name=e, value=e)
        for e in sorted(elements)
        if current in e.lower()
    ][:25]

async def autocomplete_playstyle(interaction, current: str):
    current = current.lower()
    return [
        Choice(name=s, value=s)
        for s in sorted(playstyles)
        if current in s.lower()
    ][:25]

async def player_name_autocomplete(interaction: discord.Interaction, current: str):
    current = current.lower()

    results = []
    for row in data:
        if (
            current in row["kanjiname"].lower() or
            current in row["hiragananame"].lower() or
            current in row["romajiname"].lower() or
            current in row["localisedname"].lower() or
            current in row["nickname"].lower()
        ):
            results.append(
                Choice(
                    name=f"{row['localisedname']} ({row['romajiname']})",
                    value=row["localisedname"]
                )
            )

        if len(results) >= 25:
            break

    return results

sort_options = [
    "bst",
    "kick",
    "control",
    "technique",
    "pressure",
    "physical",
    "agility",
    "intelligence"
]

async def autocomplete_sort(interaction, current: str):
    current = current.lower()
    return [
        Choice(name=opt.capitalize(), value=opt)
        for opt in sort_options
        if current in opt.lower()
    ][:25]


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    load_csv()
    build_categories()
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
@app_commands.autocomplete(name=player_name_autocomplete)
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
    embed.set_footer(text="Credit to @Xion for dataset: https://docs.google.com/spreadsheets/d/1N4h7z27Rxq3bvYuR9VyeQv3Ze-zwo-1XZQTd9rZa-Zs/edit?usp=sharing \nCreated by @Anna, DM me if you have any issues or suggestions!")
    
    await interaction.response.send_message(embed=embed, view=paginator)


@bot.tree.command(
    name="translate",
    description="Translate a player name (Kanji, Hiragana, Romaji, Localised, Nickname)."
)
@app_commands.autocomplete(name=player_name_autocomplete)
async def translate(interaction: discord.Interaction, name: str):
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
        await interaction.response.send_message("No player found with that name.")
        return

    row = matches[0]

    embed = discord.Embed(
        title=f"Translations for {row['localisedname']} ({row['romajiname']})",
        description=(
            f"**Kanji:** {row['kanjiname']}\n"
            f"**Hiragana:** {row['hiragananame']}\n"
            f"**Romaji:** {row['romajiname']}\n"
            f"**Localised:** {row['localisedname']}\n"
            f"**Nickname:** {row['nickname']}\n"
        ),
        color=0x00AEEF
    )

    if row.get("image"):
        embed.set_thumbnail(url=row["image"])

    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name="filter",
    description="Filter players using position, element, playstyle, and optional sorting."
)
@app_commands.describe(
    position="Player position (FW, MF, DF, GK)",
    element="Player element",
    playstyle="Player's playstyle",
    sort_by="Stat to sort results by (BST, Kick, Control, etc.)",
    order="Sort order: Ascending or Descending"
)
@app_commands.autocomplete(
    position=autocomplete_position,
    element=autocomplete_element,
    playstyle=autocomplete_playstyle,
    sort_by=autocomplete_sort
)
async def filter(
    interaction: discord.Interaction,
    position: str | None = None,
    element: str | None = None,
    playstyle: str | None = None,
    sort_by: str | None = None,
    order: str | None = "desc"
):

    matches = [
        row for row in data
        if (position is None or row["position"] == position)
        and (element is None or row["element"] == element)
        and (playstyle is None or row["playstyle"] == playstyle)
    ]

    if not matches:
        await interaction.response.send_message("No players found matching these filters.")
        return

    if sort_by is not None:
        reverse = (order.lower() != "asc")
        try:
            matches.sort(key=lambda r: int(r[sort_by]), reverse=reverse)
        except Exception:
            await interaction.response.send_message(
                f"Could not sort by `{sort_by}`. Make sure it is a numeric stat."
            )
            return

    paginator = PlayerPaginator(matches)
    embed = paginator.create_embed()

    embed.set_footer(text="Credit to @Xion for dataset: https://docs.google.com/spreadsheets/d/1N4h7z27Rxq3bvYuR9VyeQv3Ze-zwo-1XZQTd9rZa-Zs/edit?usp=sharing \nCreated by @Anna, DM me if you have any issues or suggestions!")
    await interaction.response.send_message(embed=embed, view=paginator)





bot.run(TOKEN)
