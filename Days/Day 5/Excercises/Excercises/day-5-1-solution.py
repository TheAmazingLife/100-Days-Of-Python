# Interactive Coding Exercises
# Exercise 1 - Average Height
# https://app.codingrooms.com/management/assignments/364933/overview

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

# total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height

# number_of_students = len(student_heights)
number_of_students = 0
for student in student_heights:
    number_of_students += 1

avarage_height = round(total_height / number_of_students)
print(avarage_height)
