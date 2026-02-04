# Python list comprehension

string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)


# List comprehensions and lambda

original_list = [1, 2, 3, 4, 5, 6]
double_list = [(lambda x: x * 2)(x) for x in original_list]
print(double_list)

# Nested loops in python list comprehension

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combLst = [(x, y) for x in list1 for y in list2]
print(combLst)
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# Conditionals in python list comprehension

list1 = [x for x in range(1, 21) if x % 2 == 0]
print(list1)


# List Comprehensions vs For Loop

# Example using for loops
chars = []
for ch in "TutorialsPOINT":
    if ch not in "aeiou":
        chars.append(ch)
print(chars)

# Example using list comprehension

chars = [char for char in "TutorialsPoint" if char not in "aeiou"]
print(chars)
