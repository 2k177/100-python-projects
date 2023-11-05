from day14.game_data import data
from art import logo,vs
import random


def display_options(a, b):
  print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")

def pick_random_option():
  random_idx = random.randint(0, len(data)-1)
  return random_idx

def intial_display():
  random_idx = pick_random_option()
  print(logo)
  display_options(data[random_idx], data[random_idx+1])
  return data[random_idx], data[random_idx+1]

def check_answer(user_choice, a , b):
  if a == b:
    print("Looks like A and B is same option, let roll the dice...")
    random_idx = pick_random_option()
    a = data[random_idx]
  if user_choice == "A" and a['follower_count'] > b['follower_count']:
    print(f"You're right! {a['name']} has more followers.")
    b = a
    a = data[random.randint(0, len(data)-1)]
    result = True
  elif user_choice == "B" and b['follower_count'] > a['follower_count']:
    print(f"You're right! {b['name']} has more followers.")
    a = data[random.randint(0, len(data)-1)]
    result = True
  else:
    print(f"Sorry, {a['name']} has {a['follower_count']} followers. and {b['name']} has {b['follower_count']} followers.")
    result = False
  print("\n", "-" * 50, "\n")
  return a, b, result


def higher_lower():
  a, b = intial_display()
  result = True
  while result:
    display_options(a,b)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    a, b, result = check_answer(user_choice, a, b)

higher_lower()
