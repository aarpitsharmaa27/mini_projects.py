# ⚙️ Mini Projects Hub

Welcome to my **Mini Projects Repository**!  
This repo contains a growing collection of beginner-friendly and fun coding projects.  
These mini tools are built to sharpen my skills and solve practical problems.

---

## 📌 Project

###  🧮 Python CLI Calculator

A cool command-line calculator in Python — with a touch of personality 😎  
Handles basic arithmetic and even roasts you for dividing by zero!

**🧠 How It Works:**

```python
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
