# append
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
# Important: Adds only ONE item, even if it's a list


# extend()
fruits = ["apple", "banana"]
fruits.extend(["cherry", "mango"])
print(fruits)


# insert()
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # Insert at index 1
print(fruits)

# Using negative index:
numbers = [1, 2, 3, 4, 5]
numbers.insert(-1, 99)  # Insert before last item
print(numbers)  # [1, 2, 3, 4, 99, 5]


# remove()
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)


# Pop() - Remove and Return Item
fruits = ["apple", "banana", "cherry"]

removed = fruits.pop()  # Remove last item
print(removed)  # 'cherry'
print(fruits)  # ['apple', 'banana']

# Negative index
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(-2)  # Remove second-to-last
print(removed)  # 'banana'


# Clear() - Remove All Items
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)


# index() - Find Position of Item
fruits = ["apple", "banana", "cherry", "banana"]
position = fruits.index("banana")
print(position)

# With start and end:
fruits = ["apple", "banana", "cherry", "banana"]
position = fruits.index("banana", 2)  # Search from index 2
print(position)  # 3

# Error if not found:
fruits = ["apple", "banana"]
fruits.index("mango")  # ValueError: 'mango' is not in list


# count() - Count Occurrences
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)

# With strings:
fruits = ["apple", "banana", "apple", "cherry"]
print(fruits.count("apple"))  # 2
print(fruits.count("mango"))  # 0 (doesn't give error!)
