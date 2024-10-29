def claculator():
    print("welcome to the simple calculator!")
    num1=float(input("Enter the First Number:"))
    operation=input("Choose operation(+,-,*,/):")
    num2=float(input("Enter the Second Number:"))

    if operation=='+':
        result=num1+num2
    elif operation=='-':
        result=num1-num2
    elif operation=='*':
        result=num1*num2
    elif operation=='/':
        if num2==0:
            return "Cannot divide by zero!"
        result= num1/num2
    else:
        return "Invalid Operation"
    
    print("Ther result is ",result)

claculator()

