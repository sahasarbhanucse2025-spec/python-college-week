print("1-add")
print("2-Substraction")
print("3-Multiply")
print("4-Divide")

option=int(input("Choose an operator: "))  

if(option in [1,2,3,4]):
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2            

else:
    print("The number is invalid")

       
print("The result of the operation is {}". format(result))       
       
       