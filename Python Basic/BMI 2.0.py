height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg : "))

BMI = round((weight/(height**2)), 2)

if BMI <= 18.5:
    print("your BMI is {} Kg/sq.m, you are underwight " .format(BMI))

elif BMI <25:
    print("your BMI is {} Kg/sq.m, you hav a normal weight " .format(BMI))

elif BMI < 30 :
    print("your BMI is {} Kg/sq.m, you are overwight " .format(BMI))

elif BMI <35:
    print("your BMI is {} Kg/sq.m, you are obese " .format(BMI))

else:
    print("your BMI is {} Kg/sq.m, you are clinically obese " .format(BMI))

# print("BMI is " + str(BMI) + " Kg/sq.m")
