# Removing list item using removed method

list1 = ["Ayush", "Pree", "Sam", 5, 9]
print("Orignal list : ", list1)
list1.remove("Sam")
print("After removing index :", list1)


# Removing list item using pop method

list2 = [22.50, "ayu", 9, "Vishal"]
print("Orignal list : ", list2)
list2.pop(2)
print("List after popping: ", list2)


# Removing list item using clear mrthod

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("Cleared list:", my_list)


# Removing list using del keyword

list1 = ["a", "b", "c", "d"]
print("orignal lists :", list1)
del list1[2]
print("List after deleting: ", list1)

# Example
list2 = ["a", "b", "c", 86, 90, 00]
print("Origanl list : ", list2)
del list2[3:6]
print("After deleting :", list2)
