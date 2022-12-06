# Interactive Coding Exercises
# Exercise 5 - Love Calculator
# https://app.codingrooms.com/management/assignments/364926/overview

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# Letter T
letter_T = lower_name1.count("t")
letter_T += lower_name2.count("t")
# Letter R
letter_R = lower_name1.count("r")
letter_R += lower_name2.count("r")
# Letter U
letter_U = lower_name1.count("u")
letter_U += lower_name2.count("u")
# Letter E
letter_E = lower_name1.count("e")
letter_E += lower_name2.count("e")

TRUE = letter_T + letter_R + letter_U + letter_E

# Letter L
letter_L = lower_name1.count("l")
letter_L += lower_name2.count("l")
# Letter O
letter_O = lower_name1.count("o")
letter_O += lower_name2.count("o")
# Letter V
letter_V = lower_name1.count("v")
letter_V += lower_name2.count("v")
# Letter E
letter_E = lower_name1.count("e")
letter_E += lower_name2.count("e")

LOVE = letter_L + letter_O + letter_V + letter_E

total = TRUE*10+LOVE
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
