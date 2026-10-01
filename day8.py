# week 2 day 1, lists

# creating a list of items
items = ["chicken", "eggs", "milk", "salt", "sugar"]
# indexing the items in the list
print(items[0], items[2], items[-1]) #print will be like: chicken milk sugar
#extracting items by slicing
print(items[1:3]) #print will be like ['eggs', 'milk']
# adding an item in the end of the list
items.append("rice")
#removing an item by its name
items.remove("sugar")# if wrong item is given, ValueError: list.remove(x): x not in list
# removing last item, store it in a variable, and changing the list
last = items.pop()
# removing and storing 1st element of a list in a variable, and shifting list by 1 left
first = items.pop(0)
#shorting in alphabetical order
items.sort()
#printing the count of a list
print(len(items))
# loop
for item in items:
    print(item)
# loop with numbering
for i, item in enumerate(items, 1):
    print(i, item)

shopping = []
while True: # this while always return us for 1/2/3/4 choice section
    print("1. Add\n2. Remove\n3. View\n4. Quiet") # ask user to choose 1/2/3/4
    choice = input("Enter your choice: ").strip() # user will type his choice, strip will filter front/back space

    if choice == "1":
        item = input("Enter the item name: ").strip().lower()
        shopping.append(item)

    elif choice == "2":
        item = input("Enter the item to remove: ").strip().lower()
        if item in shopping: # when removing we have to check whether the item inside the list or not
            shopping.remove(item)
        else:
            print("The item not in list")

    elif choice == "3":
        if len(shopping) == 0: # if there is no items in the list choice 3 print nothing, so..
            print("The list is empty")
        else:
            for i, item in enumerate(sorted(shopping), 1):# number and item will be printed, sorted(shopping) sort list in alphabetical order
                print(i, item)

    elif choice == "4": # if user want to quit , we have to use break to come out of while loop
        break

    else:
        print("Invalid choice")









