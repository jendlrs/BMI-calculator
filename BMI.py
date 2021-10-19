name=input("Enter your name:")
height_m=float(input("Enter your height in meter:"))
weight_kg=float(input("Enter your weight in kilogram:"))

bmi=weight_kg / (height_m*height_m)

print("Your BMI is:",bmi)
print(name,' ', end= "is")

if bmi < 18.5:
    print(' ',"underweight.")
elif bmi >= 18.5 and bmi <25:
    print(' ', "In normal weight")
elif bmi >=25 and bmi <30:
    print(' ', "overweight")
elif bmi >30:
    print(' ', "obese")