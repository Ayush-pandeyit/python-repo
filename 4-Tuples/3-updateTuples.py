# Updating Tuples Using Concatenation Operator
# original tuple
t1 = (10, 20, 30, 40)
# tuple to be concatenated
t2 = ("one", "two", "three", "four")
# Updating the tuple using the concatenation operato
t1 = t1 + t2
print(t1)

# Updating Tuples Using Slicing

# Original tuple
T1 = (37, 14, 95, 40)
# Elements to be added
new_elements = ("green", "blue", "red", "pink")
# Extracting slices of the original tuple
# Elements before index 2
part1 = T1[:2]
# Elements from index 2 onward
part2 = T1[2:]
# Create a new tuple
updated_tuple = part1 + new_elements + part2
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)

# Updating Tuples Using List Comprehension

t1 = (10, 20, 30, 40)
# Converting the tuple to a list
list_t1 = list(t1)
# Using list comprehension
updated_list = [item + 100 for item in list_t1]
# Converting the updated list back to a tuple
updated_tuple = tuple(updated_list)
# print the updated tuple
print("original tuple: ", t1)
print("updated tuple :", updated_tuple)


# Updating Tuples Using append() function

# Original tuple
T1 = (10, 20, 30, 40)
# Convert tuple to list
list_T1 = list(T1)
# Elements to be added
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)
