# Python Airthmetic Operators

a = 21
b = 10
c = 0
c = a + b
print("a: {} b: {} a+b: {}".format(a, b, c))

c = a - b
print("a: {} b: {} a-b: {}".format(a, b, c))

c = a * b
print("a: {} b: {} a*b: {}".format(a, b, c))

c = a / b
print("a: {} b: {} a/b: {}".format(a, b, c))

c = a % b
print("a: {} b: {} a%b: {}".format(a, b, c))


# Python Comparison operators

a = 21
b = 10
if a == b:
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")


if a > b:
    print("Line 4 - a is greater than b")
else:
    print("Line 4 - a is not greater than b")


# Python Assignment Operators

a = 21
b = 10
c = 0
print("a: {} b: {} c : {}".format(a, b, c))
c = a + b
print("a: {}  c = a + b: {}".format(a, c))

c *= a  # (c=c*a)
print("a: {} c *= a: {}".format(a, c))


# Python Bitwise Operators

a = 20
b = 10

print("a=", a, ":", bin(a), "b=", b, ":", bin(b))
c = 0

c = a & b
print("result of AND is ", c, ":", bin(c))
