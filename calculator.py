# Just Simple Calculator Project

print("Welcome to your Brother Calculator")

num1 = float(input("What's your First Number :"))
num2 = float(input("What's Your Second Number :"))
operation = input("Choose Your Operation (+ , - , * , /):")

if operation == "+" :
    result = num1 + num2
    print(f"Result : {num1} + {num2} = {result}")

elif operation == "-" :
    result = num1 - num2
    print(f"Result : {num1} - {num2} = {result}")

elif operation == "*" :
    result = num1 * num2
    print(f"Result : {num1} * {num2} = {result}")

elif operation == "/" :
    if num2 != 0  :
        result = num1 / num2
        print(f"Result : {num1} / {num2} = {result}")
    else :
        print("Are You Mad ??")
print("I HOPE YOU GOT YOUR ANSWER . THANK YOU FOR USING !")