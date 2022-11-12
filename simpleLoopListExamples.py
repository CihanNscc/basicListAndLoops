# Creating  a list of months
months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Printing months with a for loop
for i in months:
    print(i)

print("\n")
# Printing the numbers of months in the list
for i in range(0, len(months)):  # Using len() function to get the number of items in the list
    print(i + 1)  # Adding +1 since the index starts from 0

print("\n")
# Using parallel lists
# Adding the second list of expenses
expenses = [822, 736, 455, 890, 1221, 965, 2134, 1765, 567, 435, 768, 1532]

# Printing expenses of each month
for i in range(0, len(months)):  # Since number of items in both lists are same we can either use length either months or expenses
    print(months[i], ":::", expenses[i])

print("\n")
# Printing expenses of every 3rd month
for i in range(2, len(months), 3):
    print(months[i], ":::", expenses[i])

print("\n")
# This loop will compare each item in the list with the value of and stop if there is a match.
targetObject = "Phone"
allObjects = ["Desk", "Bed", "Chair", "Bucket", "Phone", "Pan", "Television"]
for i in range(0, len(allObjects)):
    if allObjects[i] == targetObject:
        print(allObjects[i], "is a", targetObject)
        break  # This will stop the loop
    else:
        print(allObjects[i], "is not a", targetObject)

# Creating a new list, excluding the "cat" items
pets = ["cat", "dog", "pig", "parrot", "cat", "cat", "dog", "turtle", "goat", "dog", "cat", "turtle"]
print("\nAll pets:\n", pets)
petsAllowed = []

for i in pets:
    if i != "cat":
        petsAllowed.append(i)

print("\nPets allowed:\n", petsAllowed)

# Adding 3 new pets to the list
for x in range(3):
    inputedAnimal = input("Enter pet #{0}: ".format(x))
    petsAllowed.append(inputedAnimal)
print("\nNew list with added pets:\n", petsAllowed)
