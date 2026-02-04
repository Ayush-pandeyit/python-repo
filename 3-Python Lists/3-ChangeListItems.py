# Change list items

list1 = [1, 2, 3, 4, 5]
print("Orignal list: ", list1)
list1[3] = 7
print("After change this value index 3:", list1)


# Change consecutive list items

list1 = ["a", "b", "c", "d"]
print("Orignal list:", list1)

list2 = ["x", "y"]
list1[1:3] = list2
print("List after changing with sublist :", list1)

# Change a range of list items

list1 = ["a", "b", "c", "d"]
print("Orignal list :", list1)

list2 = ["X", "y", "z"]
list1[1:3] = list2
print("LIst after changing with subloist:", list1)

# Example
list1 = ["a", "b", "c", "d"]
print("Orignal list : ", list1)
list2 = ["z"]
list1[1:3] = list2
print("List after changing the sublist :", list1)
