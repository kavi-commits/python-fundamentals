#Never ending loop continues inside the condition
count = 0
while count < 5:
    print(count)
    count += 1

#using break inside while loop

while True:
    answer = input("want to quit?")
    if answer == "yes":
        break

#using  continue inside while loop

n = 0
while n< 10:
    n += 1
    if n%2 == 0:
        continue
    print(n)

#Number guessing game
import random

target = random.randint(1,100)
attempts =0

while True:
    guess = int(input("Guess a number (1-100)"))
    attempts += 1
    if guess < target:
        print("GO HIGHER")
    elif guess > target:
        print("GO LOWER")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break
