# Python program to find unique numbers in a given list

L1 = [1, 9, 1, 4, 3, 6, 7, 8, 5, 7, 9, 4, 6, 7]
L2 = []
for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)


# Python program to find sum of all numbers in a list.

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Sum:", total)  # Output: Sum: 15


# Python program to create a list of 5 random integers.

import random

l1 = []
for i in range(5):
    x = random.randint(0, 100)
    l1.append(x)
print(l1)
