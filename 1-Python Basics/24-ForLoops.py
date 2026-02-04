# # Python for Loop with Strings
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""
for char in zen:
    if char not in "aeiou":
        print(char, end="")

# Python for Loop with Tuples

numbers = (54, 36, 88, 97, 43, 8, 28, 99)
total = 0
for num in numbers:
    total += num

print("Total =", total)

# Python for Loop with Lists
number = [20, 54, 87, 4, 90, 28, 45]
total = 0
for num in number:
    if num % 2 == 0:
        print(num)

# Python for Loop with Range Objects
for num in range(5):
    print(num, end=" ")
print()
for num in range(10, 20):
    print(num, end=" ")
print()
for num in range(1, 10, 2):
    print(num, end=" ")
