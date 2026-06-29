# Day2...........................

word = "Python"
print("==== Slicing ====")
print(f"word= {word}")
print(f"word[0] = {word[0]}")
print(f"word[-1] = {word[-1]}")
print(f"word[0:3] = {word[0:3]}")
print(f"word[2:] = {word[2:]}")
print(f"word[::-1] = {word[::-1]}")
print(f"len(word) = {len(word)}")

print("\n==== string methodes ====")
sentence = " the quick brown fox "

print(f"original : '{sentence}'")
print(f".strip() : '{sentence.strip()}'")
print(f"upper() : '{sentence.strip().upper()}'")
print(f"lower() : '{sentence.strip().lower()}'")
print(f"replace() : '{sentence.strip().replace('fox', 'coder')}'")
print(f".count('o') : {sentence.strip().count('o')}")
print(f".startswith() : {sentence .strip().startswith('the')}")


# --- SECTION 3: f-string Formatting ---

print ("\n==== f-string Formatting ====")
name = "kavi"
score = 487.5
label = "Score"

print(f"{'Name':<10} {'Score':>10}")
print(f"{name:<10} {score:>10.2f}")
print(f"\npi = {3.14159265:.4f}")
print(f"big = {1_000_000:,}")

# --- SECTION 4: Type Conversion ---

print("\n=== Type Conversion ===")
num_str = "2005"
num_int = int(num_str)
print(f"str : {num_str!r} type={type(num_str)}")
print(f"int :{num_int} type={type(num_int)}")
print(f"year + 1 = {num_int + 1}")

tricky = "3.99"
print(f"\nConverting '3.99' to int via float: {int(float(tricky))}")

# --- SECTION 5: Mad Libs Generator ---

print("\n=== Mad Libs Generator ===\n")
print("Fill in the blanks to build your storyh!\n")

# Collect inputes
person =input("A person's name : ").strip().title()
place = input("A place : ").strip().title()
animal = input("An animal(past tense) :").strip().lower()
verb_past = input("A verb(past tense) :").strip().lower()
adjective = input("An adjective :").strip().lower()
number = input("A number :").strip()
food = input("A type of food :").strip().lower()

try:
    number = int(number)
except ValueError:
    number = 42

story = f"""

One sunny morninng, {person} decided to travel to {place}.
They had alwways dreamed of seeing a wild {animal} in person.

After {verb_past} for exactly {number} hours sstraight, 
{person} finally arrived — only to find the {animal}
sitting on a {adjective} rock, eating a giant plate of {food}.

The {animal} looked up and said: "I've been expecting you,
{person}. There are only {number} portions of {food} left.
Choose wisely."

{person} gulped. It was going to be a long day in {place}.

                        ~ THE END ~
"""
print(story)
