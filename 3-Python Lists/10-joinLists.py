# Join Lists Using Concatenation Operator

# Two lists to be joined
l1 = [10, 20, 30, 40]
l2 = ["one", "two", "three", "four"]
# Joining the lists
joined_list = l1 + l2
# printing the joined list
print("Joined List : ", joined_list)


# Join Lists Using List Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]

joined = [item for list in [list1, list2] for item in list]
print("joined list :", joined)


# Join lists using append function
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# Example
# List to which elements will be appended
list1 = ["Fruit", "Number", "Animal"]
# List from which elements will be appended
list2 = ["Apple", 5, "Dog"]
# Joining the lists using the append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List:", list1)


# Join Lists Using extend() Function

list1 = [10, 20, 30]
list2 = [15, 25, 35]
list1.extend(list2)
print("Extended list :", list1)
