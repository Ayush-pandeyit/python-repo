# FOR THROUGH LIST ITEMS WITH FOR LOOPS

lst = [25, 23, 68, 98, 76, 65]
for num in lst:
    print(num, end=" ")


# LOOP THROUGH LIST ITEMS WITH WHILE LOOP
my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1


# Loop Through List Items with Index

lst = [25, 34, 45, -21, 10, 100]
indices = range(len(lst))
for i in indices:
    print("lst[{}]:".format(i), lst[i])


# Iterate using List Comprehension

number = [1, 2, 3, 4, 5]
squared_number = [num**2 for num in number]
print(squared_number)


# Iterate using the enumerate function

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
