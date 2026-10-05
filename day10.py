# week 3 day 3 sets tuples strings

# sets (unique and unordered)

nums = {1, 2, 3, 3, 4, 4}
print(nums)  # {1, 2, 3, 4} will be printed

empty = set()  # creates a set called empty, = {} creates a dictionary
empty.add("x")  # .add adds an element to the set, if print in this stage "x" printed
empty.remove("x")  # .remove removes an element from the set, if print in this stage set() printed, KeyError if missing
empty.discard("x")  # it removes and print set() when printed but no error if missing
print(empty)

print(len(set(["a", "b", "a"])))  # 2
print("a" in {"a", "b"})  # True (fast membership check)
# no indexing here because sets have no order

# set operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # union: everything in either -> {1, 2, 3, 4}
print(a & b)  # intersection: in both -> {2, 3}
print(a - b)  # difference: in a, not b ->  {1}
# also written as a.union(b), a.interaction(b), a.diffrence(b)

# Tuples (immutable)
point = (3, 4)
print(point[0])  # 3 (indexing works)
x, y = point  # unpacking
print(x, y)  # 3 4
#point[0] = 9  # TypeError : cant't change
single = (5,)  # one-item tuple needs the trailing comma
# one can read a tuple but never modify it

# strip()
text = "  hello, world!   "
print(text.strip()) #"hello, world!" (removes white space at both ends)
print("xxxxxxxhixxxx".strip("x")) # "hi" (removes given characters from the end)
# only the ends. It never touches the middel

# replace()
s = "hello world"
print(s.replace("l","L")) # heLLo worLd
print(s) # hello world (unchanged)
s = s.replace("l","L") # reassign to keep the result
# string are immutable, so string methods return a new string. They never change the original

# split()
print("the cat  sat".split()) # ['the', 'cat', 'sat'](any whitespace, extras ignored)
print("a,b,c".split(",")) # ['a', 'b', 'c'] (custom separator)
print("".split()) # []

# join()

words = ["the", "cat", "sat"]
print("".join(words)) # the cat sat
print("-".join(words)) # the-cat-sat

# chain summary
sentence = " The cat. The hat!  "
clean = sentence.strip().lower().replace(".", "").replace("!", "")
print(clean) # the cat the hat
words = clean.split()
print(words) # ['the', 'cat', 'the', 'hat']
print(len(set(words))) # 3
print(" ".join(words)) # the cat the hat

# word_counter.py

sentence = input("Write a sentance: ")
clean = sentence.strip().lower().replace(".","").replace(",","").replace("!","").replace("?","")
#for mark in [".", ",", "!", "?"]:
#    sentence = sentence.replace(mark, "")
words = clean.split() # split creates a list here, so we can use len for counting the words in the list
if len(words) == 0:
    print("No words")
else:
    counts = {} # this creates a dictionary here
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # this store the counts in the dictionary counts.
        # index_counts[word] = counts.get(word, 0) (counts.get(word) look up for the word, by giving like (word, 0) it give a default index of 0 for each new word)
        # counts[word] = index_counts[word] + 1

    for word, count in sorted(counts.items()):
        print(word, count)

    print("Unique words: ", len(set(words)))
























