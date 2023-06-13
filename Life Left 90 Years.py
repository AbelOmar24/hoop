#How long left to 90 Years
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = 90 * 365 - int(age) * 365 
years = 90 - int(age)
weeks = years * 52
months = years * 12

print (f"You have {days} days, {weeks} weeks, and {months} months left.")

