rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game_images = [rock, paper, scissors]

choice = int(
    input(
        "What do you choose..\nType 0 for rock\t 1 for paper\t 2 for scissors\n"
    ))

computer_choice = random.randint(0, 2)
print("Your choice: \n", game_images[choice])
print("\nComputor choice: \n", game_images[computer_choice])

#combos
#01 10 12 21 02 20
if choice == computer_choice:
    print("Match draws")
if choice >= 3:
    print("Invalid input..")
#rock & paper -> paper
if choice == 0 and computer_choice == 1:
    print("Computer wins")
elif choice == 0 and computer_choice == 1:
    print("you Win!!")
#rock & scissors -> rock
elif choice == 0 and computer_choice == 2:
    print("You Win!!")
elif choice == 2 and computer_choice == 0:
    print("Computer wins")
#paper & scissors -> scissors
elif choice == 1 and computer_choice == 2:
    print("Computer wins")
elif choice == 2 and computer_choice == 1:
    print("You Win!!")
