import random

def choose_team():
    """Choosing your team and opponent"""
    blah = True
    while blah:
     team_choice = input("Which NFL team would you like to play with? ").title()
     NFL_teams = ["Jets", "Bills", "Dolphins", "Patriots", "Titans", "Texans", "Colts", "Jaguars", "Broncos", "Chiefs", "Chargers", "Raiders", "Browns", "Steelers", "Ravens", "Bengals", "Giants", "Eagles", "Redskins", "Cowboys", "Vikings", "Packers", "Lions", "Bears", "49ers", "Seahawks", "Rams", "Cardinals", "Saints", "Falcons", "Ravens", "Buccaneers"]
     if team_choice not in NFL_teams:
        print("Please pick an existing NFL team.")
     else:
        blah = False
        print(f"Good choice! The {team_choice} are ready to kick some butt!")
        bruh = True
        while bruh:
         opponent_choice = input("Now, what team would you like to play against? ").title()
         if opponent_choice == team_choice:
             print("You can't play against the same team, silly!")
         elif opponent_choice not in NFL_teams:
             print("Please pick an existing NFL team.")
         else:
             bruh = False
             print(f"{team_choice} vs. {opponent_choice}: What a matchup! Let's get this game started!")

print("Welcome to Pocket Football!")
start = input("Would you like to play? Yes or no answers please. ").lower()
if start == "no":
 print("Well then. I hope your final project bugs out.")
else:
 print("Glad to hear! Let's go!")
 choose_team()

