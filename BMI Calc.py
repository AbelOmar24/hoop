# BMI Claculator
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height **2

bmi = round(bmi)

if bmi > 1:
  if bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
  elif bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
  elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
  elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
  print("Please try entering you height and weight again.")

