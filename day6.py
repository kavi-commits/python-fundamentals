# making a split operation calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Error: division by zero"
    return a/b

#Making manu driven calculator

def calculator():
    while True:
        print("\n1. add\n2. sub\n3. mul\n4. div\n5. Exit")
        choice = input("Choose an operation: ")

        if choice == "5":
            print("Good bye")
            break

        if choice in("1","2","3","4"):
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:, add(a,b)")
            elif choice == "2":
                print("Result:, sub(a,b)")
            elif choice == "3":
                print("Result:, mul(a,b)")
            elif choice == "4":
                print("Result:, div(a,b)")
        else:
            print("Entered invalid choice")

calculator()

