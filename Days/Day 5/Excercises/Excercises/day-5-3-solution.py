# Interactive Coding Exercises
# Exercise 3 - Adding Even Numbers
# https://app.codingrooms.com/management/assignments/364936/overview

# Write your code below this row 👇
# Two ways
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(total2)
