

# Rock Paper Scissors ASCII Art

# Rock
import random


Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choose == 0 :
    print(Rock)
elif choose == 1 :
    print(Paper)
elif choose == 2 :
    print(Scissors)

print("Computer Choose")

com_Choose = random.randint(0,2)

if com_Choose == 0 :
    print(Rock)
elif com_Choose == 1 :
    print(Paper)
elif com_Choose == 2 :
    print(Scissors)

if choose == 0 and com_Choose == 1 :
    print("You Lose")
elif choose == 1 and com_Choose == 2:
     print("You Lose")
elif choose == 2 and com_Choose == 0 :
     print("You Lose")
elif choose == com_Choose :
    print("Both have choosen same option and turn is a draw")
else :
     print("You Win")