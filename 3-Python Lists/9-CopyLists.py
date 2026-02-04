# SHALLOW COPY
list1 = [1, 2, 3]
list2 = list1.copy()  # Creates a NEW list

list2.append(4)
print(list1)  # [1, 2, 3] - Original unchanged
print(list2)  # [1, 2, 3, 4] - Only copy changed


# Example
import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a shallow copy
shallow_copied_list = copy.copy(original_list)
# Modifying an element in the shallow copied list
shallow_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)


# Deep copy

import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2].append(5)

print(original)  # [1, 2, [3, 4]] - Unchanged!
print(deep)  # [1, 2, [3, 4, 5]] - Only deep copy changed


# Copying List Using Slice Notation

# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using slice notation
copied_list = original_list[1:4]
# Modifying the copied list
copied_list[0] = 100
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)


# Copying List Using the list() Function

original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)
print("Original_list : ", original_list)
print("copied list :", copied_list)


# Copying List Using the copy() Function
import copy

original_list = [1, 2, 3, 4, 5]
copied_list = copy.copy(original_list)
print("Copied list :", copied_list)
