#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """

  ________                                ________                       
 /  _____/ __ __   ____   ______ ______  /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/ /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \  \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >  \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/          \/     \/      \/     \/ 

"""

print(logo)

import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LAVEL_ATTEMPTS = 5

def set_difficulty(level):
  if level.lower() == "easy":
    return 10
  else:
    return 5

def check_ans(ans, guess, turns):
  if guess > ans:
    print(f"You answer {guess} is too high")
    return turns - 1
  elif guess < ans:
    print(f"You answer {guess} is too low")
    return turns - 1
  else:
    print("you got the right answer !! Booo")

def guess_game():
  ans = random.randint(1, 100)
  print(f"just a part of cheating.. {ans}")
  turns = 0
  level = input("Pick the difficalty level - easy or hard")
  turns = set_difficulty(level)
  print(f"You have picked the level : {level} and you have {turns} attempts to guess the number")
  guess = 0
  while guess != ans:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number "))
    turns = check_ans(ans, guess, turns)
    if turns == 0:
      print("You lost, get the hell out of this game")
      return 
    elif guess != ans:
      print("Guess again.")


guess_game()
