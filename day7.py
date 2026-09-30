# sum of digits in a long number

n= int(input("Enter the number: "))
total = 0
remain = n
while remain>0:
    total += remain % 10 # by dividing by 10 and getting the remainder, it should be added to the total
    remain //= 10 # by doing  the integer division to  the number, we can chop off the last digit ( "/" means float division, and "//" means integer division)
print(f"The sum of every digit of the number is {total}")


# printing reversed spelling of a word

s = input("Enter the word")
rev=""
for ch in s: # here ch is the 1st to last character in a word
    rev = ch + rev
print(f"The reversed word is {rev}")

# printing the number of vowels in a word

w = input("Enter a word")
v= "aeiouAEIOU"
count = 0
for ch in w:
    if ch in v:
        count += 1
print(f"The number of vowels in the word you entered are {count}")

# prime number check
n =  int(input("Enter the number: "))
prime = True
if  n < 2:
    prime = False
else:
    for i in range(2, int(n**0.5)+1): # we dont have to check until the whole number count, checking until the square root(int(n**0.5) is enough)
        if n % i == 0:
            prime = False
            break # break inside for loop is necessary here because if it is divisible by a number we don't have to check further more
print(f"{n} is a prime number: {prime}")

# printing a right triangle of stars
n= int(input("Enter the number of rows: "))
for i in range (1 ,n+1):
    print("*" * i)

# palindrome checker, palindrome is like madom reversed madom

s = input("Enter a string")
cleaned_word = s.replace(" " , "").lower() # if the sentence is Nurses Run, it is a palindrome only if it could be written as nursesrun, so it have to remove space and make it lower case
print(f"Palindrome: {cleaned_word == cleaned_word[::-1]}") # here the output will be palindrome: True/False, because the comparison itself is already a boolean answer

#factorial using for loop
n =int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"The factorial of the number is {fact}")

#factorial using while loop
n=int(input("Enter the number: "))
fact = 1
count = 1
while count <= n:
    fact *= count
    count += 1
print(f"The factorial of the number is {fact}")

# skipping the multiples of 3
for i in range(1,31):
    if i % 3 == 0:
        continue
    print(i)
    




















