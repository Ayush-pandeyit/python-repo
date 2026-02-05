# Accessing Tuple Items with Indexing

tuple1 = ("shivam", ",ayush", 32, 89.43)
tuple2 = (1, 2, 3, 4, 5)
print("Item at 0th index in tuple1 : ", tuple1[0])
print("Item at 3th index in tuple2 : ", tuple2[3])


# Accessing Tuple Items with Negative Indexing

tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1 + 3j)
print("item at -1 index in tuples : ", tuple1[-1])
print("item at index 1 in tuple2 : ", tuple2[1])


# Accessing Range of Tuple Items with Negative Indexing
tup1 = ("a", "b", "c", "d")
tup2 = (1, 2, 3, 4, 5)
print("Items from index 1 to last in tup1: ", tup1[1:])
print("items from index 2 tast in tup2: ", tup2[2:-1])  # (3, 4)


# Access Tuple Items with Slice Operator

tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1 + 2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)

print("Items from index 1 to last in tuple1: ", tuple1[1:])
print("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print("Items from index 0 to index last in tuple3", tuple3[:])


# Accessing Sub Tuple from a Tuple
tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1 + 2j)

print("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print("Items from index 0 to 1 in tuple2: ", tuple2[0:2])
