# Unpack Tuple Items

# t1 = (x,y)
# t1 = x,y
# type (t1)
# class  'tuple'


# tup1 = (10,20,30)
# x, y, z = tup1
# print ("x: ", x, "y: ", y, "z: ",z)


# ValueError While Unpacking a Tuple

tup1 = (10, 20, 30)
x, y = tup1
x, y, p, q = tup1
# ValueError: not enough values to unpack (expected 4, got 3)

# Unpack Tuple Items Using Asterisk (*)
tup1 = (10, 20, 30, 40, 67)
x, *y = tup1
print("x: ", x, "y: ", y)

# Output = x: 10, y: [20,30,40,67]


# example 2

tup1 = (10, 20, 30, 40, 50, 60)
x, *y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)

# output  =  x: 10 y: [20, 30, 40, 50] z: 60

# Example 3
# What if we add "*" to the first variable?

tup1 = (10, 20, 30, 40, 50, 60)
*x, y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)

# output = x: [10, 20, 30, 40] y: 50 z: 60
