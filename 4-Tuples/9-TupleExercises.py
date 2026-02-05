# FIND UNIQUE NUMBER IN GIVEN TUPLE

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 4, 5, 7, 8, 9, 5, 3)
t2 = ()
for x in t1:
    if x not in t2:
        t2 += (x,)
print("Original tuple : ", t1)
print("Unique numbers : ", t2)


# FIND SUM OF ALL NUMBERS IN TUPLE

t1 = (1, 9, 1, 3, 4)
t2 = 0
for x in t1:
    t2 += x
print("Sum of all number using loop : ", t2)
t2 = sum(t1)

print("Sum of all numbers sum() function: ", t2)


# CREATE TUPLE OF 5 RANDOM INTEGERS

import random

t1 = ()
for i in range(5):
    x = random.randint(0, 100)
    t1 += (x,)
print(t1)
