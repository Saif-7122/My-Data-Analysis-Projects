# This program calculates Body Mass Index (BMI)
weight = float(input("Enter your weight in kilograms (kg): "))

height = float(input("Enter your height in meters (m): "))

bmi = weight / height**2

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
  print("You are underweight.")
elif bmi < 25:
  print("You are normal weight.")
elif bmi < 30:
  print("You are overweight.")
else:
  print("You are obese.")
