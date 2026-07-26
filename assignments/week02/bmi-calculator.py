weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi <= 24.9:
    print("BMI Category: Normal weight")
elif bmi <= 29.9:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")