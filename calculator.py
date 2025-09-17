num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number2: "))

operation = int(input("Enter 1 for addition or 2 for subtraction or 3 for multiplication or 4 for division: "))

if(operation == 1):
    print("Result: ",num1 + num2)

elif(operation == 2):
    print("Result: ",num1 - num2)
elif operation==3:
    print("Result: ",num1*num2)
elif operation==4:
    print("Result: ",num1/num2)