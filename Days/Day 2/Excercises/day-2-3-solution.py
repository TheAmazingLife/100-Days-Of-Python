# Interactive Coding Exercises
# Exercise 3 - Life in Weeks
# https://app.codingrooms.com/management/assignments/364911/overview

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_remaining = 90 - int(age)
age_months = 12 * age_remaining
age_weeks = 52 * age_remaining
age_days = 365 * age_remaining

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")
