import random

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

#Write your code below this line 👇

#Statement
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")

#If Else statement for user_choice
if user_choice == "0":
  print(rock)
elif user_choice == "1":
  print(paper)
elif user_choice == "2":
  print(scissors)
else:
  print("Try again")

#Random Rock,Paper,Scissors generator
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

#Conditions for Rock
if computer_choice == 0:
  print(rock)
  if user_choice == 0:
    print("Tie")
  elif user_choice == 1:
    print("You win") 
  else:
    print("You Lose")

#Conditions for Paper
if computer_choice == 1:
  print(paper)
  if user_choice == 0:
    print("You Lose")
  elif user_choice == 1:
    print("Tie") 
  else:
    print("You Win")

#Conditions for Scissors
if computer_choice == 2:
  print(scissors)
  if user_choice == 0:
    print("You win")
  elif user_choice == 1:
    print("You Lose") 
  else:
    print("You tie")
 