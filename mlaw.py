import random
import time

play_game = True
location = 0
kick_return = 0
team_choice = 0
opponent_choice = 0
down = 1
game_continue = True

def start_game():
    """Start for code"""
    print("Welcome to Pocket Football!\n")
    global game_continue
    while game_continue == True:
      start = input("Would you like to play? Yes or no answers please. \n").lower()
      if start == "no":
       game_continue = False
       print("Well then. I hope your final project bugs out.")
       time.sleep(600000) #Game will pretty much stop
      elif start == "yes":
       print("Glad to hear! Let's go!\n")
       return #Will go to next function
      else:
       print("Please pick either yes or no.")

def choose_team():
    """Choosing your team and opponent"""
    blah = True
    global team_choice
    global opponent_choice
    while blah:
     team_choice = input("Which NFL team would you like to play with? \n").title()
     NFL_teams = ["Jets", "Bills", "Dolphins", "Patriots", "Titans", "Texans", "Colts", "Jaguars", "Broncos", "Chiefs", "Chargers", "Raiders", "Browns", "Steelers", "Ravens", "Bengals", "Giants", "Eagles", "Redskins", "Cowboys", "Vikings", "Packers", "Lions", "Bears", "49Ers", "Seahawks", "Rams", "Cardinals", "Saints", "Falcons", "Ravens", "Buccaneers"]
     if team_choice not in NFL_teams:
        print("Please pick an existing NFL team.")
     else:
        blah = False
        print(f"Good choice! The {team_choice} are ready to kick some butt!\n")
        bruh = True
        while bruh:
         opponent_choice = input("Now, what team would you like to play against? \n").title()
         if opponent_choice == team_choice:
             print("You can't play against the same team, silly!")
         elif opponent_choice not in NFL_teams:
             print("Please pick an existing NFL team.")
         else:
             bruh = False
             print(f"{team_choice} vs. {opponent_choice}: What a matchup! Let's get this game started!\n")
    return #Will use team and opponent later on so this returns all the inputs from the function

def kickoff():
    """Player decides whether they want to return the kickoff, associated gain on kickoff depending on input"""
    kickoff_choice = input(f"The {opponent_choice} are kicking off to your end zone. Do you want to return the kickoff? \n").lower()
    global kick_return
    global location
    if kickoff_choice == "yes":
        if random.random() < 0.1:
            if random.random() < 0.7:
                kick_return = random.randint(5, 9)
            else:
                kick_return = random.randint(70, 200) #200 is here so that there is a better chance of scoring a touchdown on the kickoff
        elif random.random() > 0.1 and random.random() < 0.25:
            if random.random() < 0.8:
                kick_return = random.randint(10, 19)
            else:
                kick_return = random.randint(50, 69)
        elif random.random() > 0.25 and random.random() < 0.33:
            kick_return = random.randint(34, 49) #For example, you have an 8% chance of returning the kickoff between 40 and 49 yards
        else:
            kick_return = random.randint(20, 33)
        location = kick_return
        if location >= 100:
            print("YOU JUST TOOK THE KICKOFF FOR A TOUCHDOWN! YOU WIN!")
            time.sleep(600000) #Game will pretty much stop
        else:
            print(f"Your kick returner just returned the ball {kick_return} yards! Ball starts at the {kick_return} yard-line. \n")
            print("First and 10\n")
    else:
        kick_return = 25
        print("You didn't say yes, so it's a touchback. Ball starts at the 25 yard-line.\n")
        print("First and 10\n")

def run_func():
    """Determines yard gain on running play"""
    global gain
    if random.random() < 0.8:
      if random.random() < .7:
        gain = random.randint(1, 6) #For example, you have an 80% chance of gaining between 1 and 9 yards on a run play, and you have about a 56% chance to gain between 1 and 6 yards
      else:
        gain = random.randint(7, 9)
    elif random.random() > 0.8 and random.random() < 0.95:
      if random.random() < 0.5:
        gain = random.randint(10, 20)
      else:
        gain = random.randint(-5, 0)
    elif random.random() > 0.95 and random.random() < 0.99:
      gain = random.randint(21, 30)
    else:
      if random.random() < .8:
        gain = random.randint(31, 45)
      else:
        gain = random.randint(46, 99)


def pass_func():
    """Determines yard gain on passing play"""
    global gain
    if random.random() < 0.35:
      gain = 0 #You don't gain yardage if the pass is incomplete
      print("The pass is incomplete.\n")
    elif random.random() > 0.35 and random.random() < 0.43:
      if random.random() < .7:
        gain = random.randint(1, 5)
      else:
        gain = random.randint(-5, 0)
    elif random.random() > 0.43 and random.random() < 0.65:
      gain = random.randint(6, 10) #For example, you have a 22% chance of gaining between 6 and 10 yards on a pass play
    elif random.random() > 0.65 and random.random() < 0.84:
      gain = random.randint(11, 15)
    elif random.random() > 0.84 and random.random() < 0.93:
      gain = random.randint(16, 25)
    elif random.random() > 0.93 and random.random() < 0.99:
      gain = random.randint(26, 40)
    else:
      if random.random() < .7:
        gain = random.randint(41, 50)
      else:
        if random.random() < .7:
          gain = random.randint(51, 60)
        else:
          gain = random.randint(61, 99)


def drive():
    global location
    global gain
    global yards_to_go
    """Player chooses play option and will gain or lose yards, can result in first down, turnover, or score"""
    yards_to_go = 10
    game_continue = True
    while game_continue == True:
     play = input("Do you want to run or pass the ball? \n").lower()
     if play not in ["run", "pass", "philly special"]:
        print("Please select a valid play choice.")
     else:
      if play == "run":
        if random.random() < .05:
          game_continue = False
          print("FUMBLE! Your team lost the ball! You lose!")
          break
        else:
          run_func()
      elif play == "pass":
        if random.random() < .05:
          game_continue = False
          print("INTERCEPTION! You lose!")
          break
        else:
          pass_func()
      else: #If you select philly special
        game_continue = False
        print(f"NO ONE SAW THAT COMING! TOUCHDOWN {team_choice}! YOU WIN!")
        break
      location += gain
      if location >= 100: #If you reach the endzone
        game_continue = False
        location = 100
        print(f"TO THE HOUSE! TOUCHDOWN {team_choice}! You win!")
        break
      else:
        print(f"Your team gained {gain} yards!\n")
        print(f"The ball is at the {location} yard-line.\n")
        global down
        yards_to_go -= gain #Yards needed to get first down changes
        if yards_to_go <= 0: #If you reach the first down marker
          print(f"First down!\n")
          down = 1 #Resets to first down
          if location > 90: # If it becomes first and goal to go situation
              yards_to_go = 100 - location
              print(f"First and {yards_to_go}\n")
          else:
              print("First and 10\n")
              yards_to_go = 10 #Resets back to 10 yards needed to get the first down
        else:
          down += 1 #Down is added if you do not get the first down
          if down == 2:
            print(f"Second down and {yards_to_go}\n") #Will tell you what down it is and how many yards you need to get the first down
          elif down == 3:
            print(f"Third down and {yards_to_go}\n")
          elif down == 4:
            print(f"Fourth down and {yards_to_go}\n")
          else: #If you don't get the first down in four tries
            game_continue = False
            print("You did not get the first down. You lose!")
            break



start_game()
choose_team()
kickoff()
drive()


