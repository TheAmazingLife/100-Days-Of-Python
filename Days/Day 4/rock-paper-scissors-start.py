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

# Write your code below this line 👇
ascii_art = [rock, paper, scissors]

choose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choose >= 3 or choose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(ascii_art[choose])
    choose_pc = random.randint(0, 2)

    print("Computer chose:\n"+ascii_art[choose_pc])

    if choose == 0 and choose_pc == 2:
        print("You Win")
    elif choose_pc == 0 and choose == 2:
        print("You lose")
    elif choose > choose_pc:
        print("You win")
    elif choose_pc > choose:
        print("You lose")
    elif choose == choose_pc:
        print("Its a Draw")
