# Accessing List Items with Indexing

list1 = ["Rohan", "Ayush", "Shivam", 92, 90]
list2 = [1, 2, 3, 4, 5]
print("Item at 0th index in list: ", list1[0])
print("Item at index 2 in list2: ", list2[2])

# Access List Items with Negative Indexing

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -65, 1 + 2j]
print("Item at 0th index in list1:", (list1[-1]))
print("Item at index 2 in list2: ", list2[-3])


# Access List Items with Slice Operator
# start is the starting index (inclusive).
# stop is the ending index (exclusive)

list1 = ["a", "b", "c", "d"]
list2 = [25.98, 98, -55, 90, 80]
list3 = ["Rohan", "Ayush", 21, 50, 80.96]

print("Items from index 1 to last in list1:", list1[1:])
print("Items from index 0 to 1 in list2:", list2[:2])
print("Items from index 0 to index last in list3", list3[:])


# Access Sub List from a List

list1 = ["a", "b", "c", "d"]
list2 = [25.90, True, -55, 1 + 2j]
print("Items from index 1 to 2 in list1: ", list1[1:3])
print("Items from index 0 to 1 in list2: ", list2[0:2])
