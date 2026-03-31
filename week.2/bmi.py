weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
                                                                              
# BMI formula
bmi = weight / (height * height)
                                     
print("Your BMI is:", round(bmi, 2))
                                           
# BMI Classification
if bmi < 18.5:
    print("Category: Underweight")

elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")

elif 25 <= bmi <= 29.9:
    print("Category: Overweight")

else:
    print("Category: Obesity")

    
