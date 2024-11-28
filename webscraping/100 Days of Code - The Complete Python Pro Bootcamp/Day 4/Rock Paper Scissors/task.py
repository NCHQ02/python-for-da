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
fruits_list = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
print("your choice")
print(fruits_list[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer choice:")
print(fruits_list[computer_choice])