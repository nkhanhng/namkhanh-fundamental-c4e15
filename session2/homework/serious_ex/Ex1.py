h = int(input("Your height?(cm) "))
w = int(input("Your weight?(kg) "))

m = h * 0.01
bmi = w / (m * m)

print("Your BMI =", bmi)

if bmi < 16:
    print("Severely underweight")
elif 16 <= bmi < 18.5:
    print("Underweight")
elif 18 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
