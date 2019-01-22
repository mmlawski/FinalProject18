import random

play_game = True
location = 0
kick_return = 0
team_choice = 0
opponent_choice = 0
down = 1
game_continue = 0

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
    """Takes input and determines the yard gain on the kickoff"""
    kickoff_choice = input(f"The {opponent_choice} are kicking off to your end zone. Do you want to return the kickoff? ").lower()
    global kick_return
    global location
    if kickoff_choice == "yes":
        if random.random() < 0.08:
            if random.random() < 0.7:
                kick_return = random.randint(1, 9)
            else:
                kick_return = random.randint(70, 100)
        elif random.random() > 0.08 and random.random() < 0.25:
            if random.random() < 0.8:
                kick_return = random.randint(10, 19)
            else:
                kick_return = random.randint(50, 69)
        elif random.random() > 0.25 and random.random() < 0.33:
            kick_return = random.randint(40, 49)
        else:
            kick_return = random.randint(20, 39)
        print(f"Your kick returner just returned the ball {kick_return} yards! Ball starts at the {kick_return} yard-line. ")
        print("First and 10")
    else:
        kick_return = 25
        print("You didn't say yes, so it's a touckback. Ball starts at the 25 yard-line.")
        print("First and 10")
    location = kick_return

def run_func():
    """Determines yard gain on running play"""
    global gain
    if random.random() < 0.75:
      gain = random.randint(1, 9)
    elif random.random() > 0.75 and random.random() < 0.95:
      if random.random() < 0.6:
        gain = random.randint(10, 29)
      else:
        gain = random.randint(-5, 0)
    elif random.random() > 0.95 and random.random() < 0.99:
      gain = random.randint(30, 49)
    else:
      gain = random.randint(50, 99)


def pass_func():
    """Determines yard gain on passing play"""
    global gain
    if random.random() < 0.37:
      gain = 0
      print("The pass is incomplete.")
    elif random.random() > 0.37 and random.random() < 0.44:
      gain = random.randint(-5, 0)
    elif random.random() > 0.44 and random.random() < 0.85:
      gain = random.randint(1, 15)
    elif random.random() > 0.85 and random.random() < 0.93:
      gain = random.randint(16, 25)
    elif random.random() > 0.93 and random.random() < 0.98:
      gain = random.randint(26, 40)
    else:
      gain = random.randint(41, 99)


def drive():
    global location
    global gain
    global yards_to_go
    """Player can choose to run or pass the ball"""
    game_continue = True
    while game_continue == True:
     play = input("Do you want to run or pass the ball? ").lower()
     if play not in ["run", "pass", "philly special"]:
        print("Please select a valid play choice.")
     else:
      if play == "run":
        if random.random() < .06:
          game_continue = False
          print("FUMBLE! Your team lost the ball! You lose!")
          break
        else:
          run_func()
      elif play == "pass":
        if random.random() < .06:
          game_continue = False
          print("INTERCEPTION! You lose!")
          break
        else:
          pass_func()
      else:
        game_continue = False
        print(f"NO ONE SAW THAT COMING! TOUCHDOWN {team_choice}! YOU WIN!")
        break
      location += gain
      if location >= 100:
        game_continue = False
        location = 100
        print(f"TO THE HOUSE! TOUCHDOWN {team_choice}! You win!")
        break
      else:
        print(f"Your team gained {gain} yards!")
        print(f"The ball is at the {location} yard-line.")
        yards_to_go = 10 - gain
        global down
        if yards_to_go <= 0:
          print("First down!")
          down = 1
          print("First and 10")
        else:
          down += 1
          if down == 2:
            print(f"Second down and {yards_to_go}")
          elif down == 3:
            print(f"Third down and {yards_to_go}")
          elif down == 4:
            print(f"Fourth down and {yards_to_go}")
          else:
            game_continue = False
            print("You did not get the first down. You lose!")
            break



start_game()
choose_team()
kickoff()
drive()


