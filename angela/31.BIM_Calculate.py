#BIM = weight / height ** 2
weight = int(input("your weight:"))
height = float(input ("your height:"))
BMI = weight / height ** 2
print(BMI)
BMI_as_int = int(BMI)
print(BMI_as_int)
if BMI <18.5:
    print("you are underweight")
elif BMI <25:
    print("you are normalweight")
elif BMI < 30:
    print("you are overweight")
elif BMI < 35:
    print("you are obse")
else:
    print("you are clinically obse")