# Basic Tuples

# tup1 = ("Rohan", "Physics", 21, 69.75)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = ("a", "b", "c", "d")
# tup4 = (25.50, True, -55, 1+2j)


# Accessing Values in Tuples

tup1 = ("Ayush", "Shivam", "Physics", "Chemistry", 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 67, 7, 90)
print("tup1[0]:", tup1[0])
print("tup2:", tup2)
print("tup2[1:4]", tup2[1:4])


# Updating Tuples
tup1 = (12, 34.56)
tup2 = ("abc", "xyz")
# Following action is not valid for tuples
# tup1[0] = 100;
# so let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)


# Delete Tuple Elements
tup1 = ("physics", "chemistry", 1997, 20.45)
print(tup1)
del tup1
print("after deleting tup : ")
print(tup)
# after del tup tuple does not exist any more −

# compares tuple
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
result = cmp(tuple1, tuple2)  # Returns -1, 0, or 1
