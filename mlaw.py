import random

play_game = True
location = 0
kick_return = 0
team_choice = 0
opponent_choice = 0
gain = 0

def start_game():
    """Start for code"""
    print("Welcome to Pocket Football!")
    game = 0

    global play_game

    while game == 0:
     start = input("Would you like to play? Yes or no answers please. ").lower()
     if start == "no":
      print("Well then. I hope your final project bugs out.")
      play_game = False
      game = 1
     elif start == "yes":
      print("Glad to hear! Let's go!")
      game = 1
     else:
      print("Please pick either yes or no.")

def choose_team():
    """Choosing your team and opponent"""
    blah = True

    global play_game
    global team_choice
    global opponent_choice

    while blah and play_game:
     team_choice = input("Which NFL team would you like to play with? ").title()
     NFL_teams = ["Jets", "Bills", "Dolphins", "Patriots", "Titans", "Texans", "Colts", "Jaguars", "Broncos", "Chiefs", "Chargers", "Raiders", "Browns", "Steelers", "Ravens", "Bengals", "Giants", "Eagles", "Redskins", "Cowboys", "Vikings", "Packers", "Lions", "Bears", "49Ers", "Seahawks", "Rams", "Cardinals", "Saints", "Falcons", "Ravens", "Buccaneers"]
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
    return

def kickoff():
    """First play of game"""
    kickoff_choice = input(f"The {opponent_choice} are kicking off to your end zone. Do you want to return the kickoff? ").lower()

    global kick_return
    global location

    if kickoff_choice == "yes":
        if random.random() < 0.1:
            if random.random() < 0.5:
                kick_return = random.randint(1, 9)
            else:
                kick_return = random.randint(70, 100)
        elif random.random() > 0.1 and random.random() < 0.25:
            if random.random() < 0.5:
                kick_return = random.randint(10, 19)
            else:
                kick_return = random.randint(50, 69)
        elif random.random() > 0.25 and random.random() < .4:
            kick_return = random.randint(40, 49)
        else:
            kick_return = random.randint(20, 39)
        print(f"Your kick returner just returned the ball {kick_return} yards! Ball starts at the {kick_return} yard-line. ")
    else:
        kick_return = 25
        print("You didn't say yes, so it's a touckback. Ball starts at the 25 yard-line.")
    location = kick_return

def yards_to_go():
    """Will let player know what down it is"""


def play_selection():
    """Player can choose to run or pass the ball"""
    play = input("Do you want to run or pass the ball? ").lower()
    game_continue = True
    while game_continue == True:
     global gain
     if play not in ["run", "pass", "philly special"]:
        print("Please select a valid play choice.")
     else:
      if play == "run":
        if random.random() < 0.6:
          gain = random.randint(1, 9)
        elif random.random() > 0.6 and random.random() < 0.85:
          if random.random() < 0.5:
            gain = random.randint(10, 29)
          else:
            gain = random.randint(-5, 0)
        elif random.random() > 0.85 and random.random() < 0.95 :
            gain = random.randint(30, 49)
        else:
            gain = random.randint(50, 99)
      elif play == "pass":
        if random.random() < 0.3:
            gain = 0
            print("The pass is incomplete.")
        elif random.random() > 0.3 and random.random() < 0.35:
            gain = random.randint(-5, 0)
        elif random.random() > 0.35 and random.random() < 0.7:
            gain = random.randint(1, 15)
        elif random.random() > 0.7 and random.random() < 0.9:
            gain = random.randint(16, 25)
        elif random.random() > 0.9 and random.random() < 0.97:
            gain = random.randint(26, 40)
        else:
            gain = random.randint(41, 99)
      else:
        game_continue = False
        print(f"NO ONE SAW THAT COMING! TOUCHDOWN {team_choice}! YOU WIN!")
        break
      global location
      location += gain
      if location >= 100:
        game_continue = False
        location = 100
        print(f"TOUCHDOWN {team_choice}! You win!")
        break
      else:
        print(f"Your team gained {gain} yards!")
        print(f"The ball is at the {location} yard-line.")
     play = input("Do you want to run or pass the ball? ").lower()


start_game()
choose_team()
kickoff()
play_selection()


