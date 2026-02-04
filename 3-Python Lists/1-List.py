# Example of python List

list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1 + 2j]


# Accessing Values in Lists
list1 = ["Physics", "chemistry", 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]:", list2[1:5])


# Updating Lists
list = ["Physics", "Math", "Chemistry", 1989]
print("value available at index 2 :")
print(list[2])
list[2] = 2001
print("new value available at index 2 :")
print(list[2])


list = ["ayush", "shivam", 91, 993]
print("value of index 2 :", list[2])
# print(list[2])
list[2] = 1990
print("New index is :")
print(list[2])


# Delete List Element
list1 = ["physics", "chemistry", 1997, 1880]
print(list1)
del list1[2]
print("After dleting value of index 2 :")
print(list1)
