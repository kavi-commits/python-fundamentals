#week 3 day 4 File read/write

#open() and modes
open("demo.txt", "w") # write: creates files, erases if it exists
open("demo.txt", "a") # append: creates if missing, adds to the end
open("demo.txt", "r") # read (default): file must exist
# open() returns a file object. You use that object to read or write

# the with statement
with open("demo.txt", "w") as f:
    f.write("line one\n")
    # file is automatically closed here
# with closes the file when the block ends, even if an error occurs. Always use it. Plain open() leaves the closing to you, and forgetting can lose data.

# write()
with open("demo.txt", "w") as f:
    f.write("line one\n")
    f.write("line two\n")
# write() takes a string only. f.write(5) is a TypeError, so use f.write(str(5))
# ith adds no new line without \n, everything lands on one line

# append mode
with open("demo.txt", "a") as f:
    f.write("line three\n")
# run the "w" block again and file resets to its new content. Run the "a" block again and it grows each time

# read()
with open("demo.txt", "r") as f:
    text = f.read()
print(text)
# returns the whole file as one string, including the \n characters

# readlines()
with open("demo.txt", "r") as f:
    lines = f.readlines()
print(lines) # ['line one\n', 'line two\n', 'line three\n']
# returns a list with one string per line, each string still ends with \n

# loop line by line

with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip()) # strip removes the trailing \n

with open("demo.txt", "r") as f:
    for i, line in enumerate(f,1):
        print(i, line.strip())
# looping the file object directly reads one line at a time. use this for large files

# Missing file

try:
    with open("demo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
# "r" on a missing file raises FileNotFoundError, "w" and "a" create the file, so they never raise it.

# where the file lives
# Relative names like "demo.txt" are created in the folder you ran python from. run python notes.py from the folder that holds the script.

# Milestone 2, notes.py

while True:
    print("\n1. Add note\n2. View notes\n3. Quit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        note = input("Enter your note: ").strip()
        if note == "":
            print("Empty note")
        else:
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
                print("Added note")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as f:
                lines = f.readlines()
                if len(lines) == 0:
                    print("No notes yet")
                else:
                    for i, line in enumerate(f,1):
                        print(i, line.strip())
           #with open("notes.txt", "r") as f:
               #count = 0
               #for i, line in enumerate(f,1):
                   #print(i, line.strip())
                   #count = i
               #if count == 0:
                   #print("no notes yet")
        except FileNotFoundError:
            print("No notes yet")

    elif choice == "3":
        break

    else:
        print("Invalid choice")























