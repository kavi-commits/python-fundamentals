# Week 4 Day 17 Error Handling


#  1 try/exept/else/finally

try:
    n = int(input("Number: "))   #risky code
except ValueError:
    print("Please enter an integer") # runs only if ValueError happened
else:
    print(f"You entered: {n}") # runs only if NO error Happened
finally:
    print("done")   # runs  always, error or not

# try: code that might fail
# except: what to do if it fails
# else: success only code. Keep it separate so except only guards the risky line
# finally: cleanup that must always run (closing files, releasing resources)


# 2. Catch specific errors
try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File missing. ")
except PermissionError:
    print("No access.")

# _____ERRORS______
# ValueError --> int("abc") raises ValueError
# FileNotFoundError --> open("Missing.txt") raises FileNotFoundError
# ZeroDivisionError --> 10/0 raises ZeroDivisionError
# Always name the error. Bare except: or except Exception: hides real bugs, including typos in your own code.
# One try can have several except blocks. Python uses the first matches
# Catch several in one block: except (ValueError, TypeError):
# Get the message: except ValueErrors e: then print(e)

# 3. Raise your own Errors
    def set_age(age):
        if age < 0:
            raise ValueError("Age cannot be Negative.")
        return age


    try:
        set_age(-5)
    except ValueError as e:
        print(e)  # Age cannot be Negative

# ! raise stops the function immediately and sends the error to the caller.
# use it when input is valid and your function cannot continue safely.

# 4. Build: validators.py
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Must be greater then 0.")
        except ValueError as e:
            if "Must be greater" in str(e):
                print(e)
            else:
                print("Invalid input. Enter a number like 5 or 2.5")
        else:
            return value



if __name__ == "__main__":
    x = get_positive_number("Enter amount: ")
    print(f"Got {x}")
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number like 5 or 2.5")
            continue
        if value <= 0:
            print("Must be greater than 0.")
            continue
        return value














