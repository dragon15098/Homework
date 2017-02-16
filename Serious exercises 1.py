height = int(input("heght=?"))/100
weight = int(input("weight=?"))
BMI=weight/(height*height)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI <30:
    print("Overweight")
else:
    print("Obese")
