name=input("\nEnter your name: ")
height_in_m=float(input("\nEnter your height in meter: "))
weight_in_kg=float(input("\nEnter your weight in kilogram: "))
#formula
bmi=weight_in_kg / height_in_m**2

print(f"\nYour BMI is: {bmi:.2f}")
print(name,' ', end= "is")

if bmi < 18.5:
    print(' ',"underweight.")
elif bmi >= 18.5 and bmi <25:
    print(' ', "In normal weight")
elif bmi >=25 and bmi <30:
    print(' ', "overweight")
elif bmi >30:
    print(' ', "obese")