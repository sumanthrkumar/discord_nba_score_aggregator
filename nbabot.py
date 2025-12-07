import discord
from discord.ext import commands
from discord.ui import Button, View
from nba_api.stats.static import teams
from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv2
from nba_api.live.nba.endpoints import scoreboard
from datetime import datetime, timedelta

import asyncio

#DISCORD CONFIGURATION
TOKEN = 'ENTER_TOKEN_HERE'

# --- SETUP ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# Fetch today's NBA games
def getTodaysGames():
    try:
        board = scoreboard.ScoreBoard()
        gamesData = board.get_dict()
        gameList = []
        
        # Loop through the list of games in the JSON structure
        for game in gamesData['scoreboard']['games']:
            gameId = game['gameId']
            homeTeam = game['homeTeam']
            awayTeam = game['awayTeam']
            
            # Get abbreviations and Scores
            homeName = homeTeam['teamTricode']
            awayName = awayTeam['teamTricode']
            homeScore = homeTeam['score']
            awayScore = awayTeam['score']
            
            status = game['gameStatusText']
            
            matchupStr = f"{awayName} vs {homeName}"
            scoreStr = f"{awayScore} - {homeScore}"
            
            gameList.append({
                'id': gameId,
                'matchup': matchupStr,
                'score': scoreStr,
                'status': status
            })
            
        return gameList

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
class GameButton(Button):
    def __init__(self, gameInfo):
        # Create a button with the matchup label
        label = f"{gameInfo['matchup']} ({gameInfo['status']})"
        
        # custom_id stores the gameId so we know what to fetch when clicked
        super().__init__(style=discord.ButtonStyle.primary, label=label[:80], custom_id=str(gameInfo['id']))
        self.gameInfo = gameInfo

    async def callback(self, interaction: discord.Interaction):
        # This triggers when the button is clicked
        await interaction.response.defer(ephemeral=True)
        
        # Placeholder: For now, we just confirm the click. 
        # (We will add the full box score stats logic here later)
        await interaction.followup.send(f"Fetching stats for {self.gameInfo['matchup']}... (Feature coming soon)", ephemeral=True)

class ScoreboardView(View):
    def __init__(self, gameList):
        super().__init__(timeout=None) # Buttons never expire
        for game in gameList:
            self.add_item(GameButton(game))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def games(ctx):
    # 1. Fetch data first 
    gameList = getTodaysGames()
    
    if not gameList:
        await ctx.send("No games found today.")
        return

    # 2. Create the "Header" message in the main channel
    # This acts as the anchor for the thread.
    todayDate = datetime.now().strftime('%Y-%m-%d')
    headerMsg = await ctx.send(f"🏀 **NBA Games for {todayDate}**\nClick the thread below for live scores and stats! ⬇️")

    # 3. Create a public thread on that message
    # auto_archive_duration=1440 means it closes after 24 hours of inactivity
    thread = await headerMsg.create_thread(name=f"NBA Games - {todayDate}", auto_archive_duration=1440)

    # 4. Prepare the Embed and View (same as before)
    view = ScoreboardView(gameList)
    embed = discord.Embed(title=f"Scoreboard - {todayDate}", color=discord.Color.red())
    
    summaryText = ""
    for game in gameList:
        summaryText += f"**{game['matchup']}**: {game['score']} ({game['status']})\n"
    
    embed.add_field(name="Summary", value=summaryText)
    embed.set_footer(text="Click a button below to expand the Box Score")

    # 5. Send the heavy content INSIDE the thread
    await thread.send(embed=embed, view=view)


if __name__ == "__main__":
    bot.run(TOKEN)