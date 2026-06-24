# Day 1.......................................
name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)

print(f"\nHello, {name}! You are {age} years old.")
print(f"In 10 years you will be {age + 10}.")
print(f"Type of 'name': {type(name)}")
print(f"type of 'age': {type(age)}")

# ------FUNCTION CALCULATOR ---
print("\n------FUNCTION CALCULATOR-----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division ="Undefined (can not divide by zero)"

print(f"\n{num1} + {num2} = {addition}")
print(f"\n{num1} - {num2} = {substraction}")
print(f"\n{num1} * {num2} = {multiplication}")
print(f"\n{num1} / {num2} = {division}")

