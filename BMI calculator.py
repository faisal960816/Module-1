print("  BMI   CALCULAR    ")
name=input("Enter your name: ")
weight=float(input("weight in kg: "))
hight=float(input("Enter your height in foot: "))
bmi=(weight/hight)**2
print(bmi)
if bmi<18.5:
    print(name,"You are underweight")
elif bmi>=18.5 and bmi<24.9:
    print(name,"You are normal weight")
elif bmi>=25:
    print(name,"You are overweight")
else:
    print(name,"You are obese")            
