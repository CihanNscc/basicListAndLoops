# Examples with a list of strings
print("Examples with a list of strings")

# Creating  a list
animals = ["cat", "dog", "bat", "tiger", "snake", "crocodile"]

# Printing the list
print("Original List:\n", animals)

# Accessing values in the list
print("2nd item in the list:", animals[1])  # Prints 2nd item in the list
print("1 to 3rd items in the list:", animals[0:3])  # Prints 1 to 3rd items in the list
print("Last item in the list:", animals[-1])  # Prints the last item in the list

# Simple operations with strings
print("An example to concatenation:", animals[2] + animals[4])  # Prints the concatenation of 3rd and 5th items
print("An example to repetition:", animals[4] * 4)  # Prints the repetition (4 reps) of 3rd item

# Updating List
animals[2] = "dolphin"  # Updates the 3rd item ("bat") in the list to "dolphin"

animals.append("eagle")  # Adds an item to the end of the list

animals.insert(2, "snake")  # Inserts an item to the 3rd spot on the list

del animals[6]  # Deletes the 5th item ("crocodile") in the list

# Printing the list
print("\nUpdated List:\n", animals)

# Some common list functions
print("Count of the 'snake' in the list:", animals.count("snake"))
print("Number of the items in the list:", len(animals))
animals.reverse()
print("Reversed List:", animals)

# Examples with a list of numbers
print("\nExamples with a list of numbers")

# Creating  a list of numbers
listOfNumbers = [6, 17, 12, 4, 22, 7]

# Printing the list
print("Original List:\n", listOfNumbers)

# Simple functions
print("\nSum of all numbers in the list:", sum(listOfNumbers))  # Prints sum of all items in the list
print("Highest number in the list:", max(listOfNumbers))  # Prints the item with the max value in the list
print("Lowest number in the list:", min(listOfNumbers))  # Prints the item with the min value in the list