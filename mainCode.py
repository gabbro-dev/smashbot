import urllib.request, urllib.parse
import ssl, re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Utility var
rows = 20

# Smash roster tuple
ssbuRoster = ("Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox", "Pikachu", "Luigi", 
              "Ness", "Captain Falcon", "Jigglypuff", "Peach", "Daisy", "Bowser", "Ice Climbers", "Sheik", "Zelda",
              "Dr Mario", "Pichu", "Falco'", "Marth", "Lucina", "Young Link", "Ganondorf", "Mewtwo", "Roy", "Chrom",
              "Mr Game And Watch", "Meta Knight", "Pit", "Dark Pit", "Zero Suit Samus", "Wario", "Snake", "Ike",
              "Pokemon Trainer", "Diddy Kong", "Lucas", "Sonic", "King Dedede", "Olimar", "Lucario", "Rob", 
              "Toon Link", "Wolf", "Villager", "Mega Man", "Wii Fit Trainer", "Rosalina And Luma", "Little Mac",
              "Greninja", "Mii Swordfighter", "Mii Brawler", "Mii Gunner", "Palutena", "Pac Man", "Robin", "Shulk",
              "Bowser Jr", "Duck Hunt", "Ryu", "Ken", "Cloud", "Corrin", "Bayonetta", "Inkling", "Ridley", 
              "Simon", "Richter", "King K Rool", "Isabelle", "Incineroar", "Piranha Plant", "Joker", "Hero", 
              "Banjo-Kazooie", "Terry", "Byleth", "Min Min", "Steve", "Sephiroth", "Pyra Mythra", 
              "Kazuya", "Sora", "Random")

# Class for players profiles
class Players:       # Main Atr             # For Discord Profile
    def __init__(self, name, pos, mains, code, winrate, tournNames, tournRank, tournMaxRank, ownerId):
        # Main Atributes
        self.name = name
        self.pos = pos
        self.mains = mains
        self.code = code
        # For Discord Profile
        self.winrate = winrate
        self.tournNames = tournNames
        self.tournRank = tournRank
        self.tournMaxRank = tournMaxRank
        self.ownerId = ownerId

    playerProfilesList = []
    
    # Constructor
    @classmethod
    def createPlayerProfile(cls, name, pos, mains, code, winrate, tournNames, tournRank, tournMaxRank):
        playerProfile = cls(name, pos, mains, code, winrate, tournNames, tournRank, tournMaxRank, "N/A")
        Players.playerProfilesList.append(playerProfile)
        print("✅ Created profile:", playerProfile.name)
    
    # Search player by name
    def searchPlayer(search):
        # If string provided, searches by name (i.name)
        if type(search) == str:
            print("💬 Searching by name")
            for player in Players.playerProfilesList:
                # To make the search less tedious
                if search.isalpha():
                    test = re.findall(search.upper(), player.name.upper())
                else:
                    test = re.findall(search, player.name)
                
                if len(test) > 0:
                    # Returns the player object
                    return player
            # If name is not found
            print("❌ Name not found:", search)
            return "NOTFOUND"
        else:
            print("🔢 Searching by top")
            # Int was providad, searches by top (i.pos)
            for player in Players.playerProfilesList:
                if player.pos == search:
                    return player
            # If top was not found
            print(f"❌ Top out of range (Max {rows}):", search)
            return "NOTFOUND"
                
# Function to retrieve all profiles
def getArgRankProfiles():

    """ Part 1: Getting main atributes """

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Arg Rank Website URL
    urlArgRanking = "https://braacket.com/league/ArgRank2024/ranking?rows=" + str(rows) # Amount of players
    htmlArgRanking = urlopen(urlArgRanking, context=ctx).read()
    soupArgRanking = BeautifulSoup(htmlArgRanking, "html.parser") # Not used

    # Retrieve all players names (in order)
    names = re.findall("/league/ArgRank2024/player/.*'>(.+)</a>", htmlArgRanking.decode())
    # Retrieve all players codes (in order)
    playerCodes = re.findall("'/league/ArgRank2024/player/(.*)\\'>\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t<a href=\\'/league/ArgRank2024/player/.*\\'>", htmlArgRanking.decode())
    # Retrieve all players mains
    rawMains = re.findall("\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t&nbsp(.*)\\t\\t\\t\\t\\t\\t\\t\\t\\t</td>", htmlArgRanking.decode())
    
    print("=" * 100)
    print("✅ PART 1 complete")
    print("=" * 100)

    """ Part 2: Getting Discord Profile atributes """

    # List to then use in the constructor of instances
    winrateList = []
    tournNamesList = []
    tournRankList = []
    tournMaxRankList = []
    # Number for debugging in process of appending profiles
    n = 0

    # Get all Discord Profile atributes for player
    for code in playerCodes:
        # For debugging
        n += 1
        loading = (n * 100) // rows
        # Get HTML from URL
        url = "https://braacket.com/league/ArgRank2024/player/" + str(code)
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser") # Not used

        # Get Tournament Names
        tournamentNames = re.findall("'>(.*)</a>\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t</td>\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t<td", html.decode())
        # Get Winrate
        wr = re.findall("<div class=\\'my-dashboard-values-main\\'>\\n\\t\\t\\t\\t\\t(.*) \\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tWin rate\\n\\t\\t\\t\\t</div>", html.decode())
        # Get player rank per tournament
        rank = re.findall("\\'text-bold\\'>\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t(.+)\\n", html.decode())
        # Get total rank per tournament
        totalRanks = re.findall("class=\\'player_stats_tournament_rank_total\\'>(.+)</span>", html.decode())

        # Limiting to 12 tournaments per profile

        maxTournies = 12
        tournamentNames = tournamentNames[:maxTournies]
        rank = rank[:maxTournies]
        totalRanks = totalRanks[:maxTournies]

        # Append them to the list
        winrateList.append(wr[0])
        tournNamesList.append(tournamentNames)
        tournRankList.append(rank)
        tournMaxRankList.append(totalRanks)

        # Debugging
        print("✅", n, "profile appended |", loading, "%")

    print("=" * 100)
    print("✅ PART 2 complete")
    print("=" * 100)

    """ Part 3: Creating instances """

    # Creating instances for each player
    for i in range(len(names)):
        # Necessary list (since mains are a weird code at the beginning)
        playerMain = []
        main = rawMains[i]
        # Cleaning the weird main code
        for pj in ssbuRoster:
            if pj in main:
                playerMain.append(pj)
        # Create the instance for the player
        Players.createPlayerProfile(names[i], i + 1, playerMain, playerCodes[i], winrateList[i], tournNamesList[i],
                                    tournRankList[i], tournMaxRankList[i])
        
    print("=" * 100)
    print("✅ PART 3 complete")
    print("=" * 100)

""" Testing Area """