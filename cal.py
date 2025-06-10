# Simple_Calculator

def calculator ():
    print("Simple calculator")
    num1 = float(input("Enter First number :"))
    num2 = float(input("Enter second number :"))
    num3 = float(input("Enter third number :"))
    operation = input("Choose Operation  (+ , - , *, /): ")

    if operation == '+':
        result = num1 + num2
    
    elif operation == '-':
        result = num1 - num2

    elif operation == '*' :
        result == num1 * num2

    elif operation == '/' :
        if num2 != 0 :
            result == num1 / num2
        else :
            return "Errror : division by zero !"
    else :
         return " Invalid Operation "

    return f"result ; {result}"
    
    print(calculator())