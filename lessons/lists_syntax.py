"""Demonstrate basic list syntax."""

#initialize an empty list
grocery_list: list[str] = list() # <-list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

#add items to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#indexing
print("Print first element of string")
print(grocery_list[0])

#modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

#measuring length
print(len(grocery_list))

#remove an item by idx
grocery_list.pop(2)
print("After removing bread:")
print(grocery_list)

# function name: display
# parameter: list[str]
# return nothing
# print out the list
def display(word: list[str]) -> None:
    print(word)
display(grocery_list)

# create a list
# name: create
# parameters: str and str
# RV: list[str]
# put both parameters into a list
def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list
print(create("Hello", "World"))