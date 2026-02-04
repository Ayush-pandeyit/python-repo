# Augmented Addition Operator (+=)
a = 10.50
b = 5 + 6j
print("Augmented addition of float and complex")
a += b  # equivalent to a=a+b
print("a=", a, "type(a):", type(a))

# a= (15.5+6j) type(a): <class 'complex'>


# Augmented Subtraction Operator (-=)
a = 10.50
b = 5 + 6j
print("Augmented subtraction of float and complex")
a -= b  # equivalent to a=a-b
print("a=", a, "type(a):", type(a))

# a= (5.5-6j) type(a): <class 'complex'>

# Augmented Multiplication Operator (*=)


a = 10
b = 5.5
print("Augmented multiplication of int and float")
a *= b  # equivalent to a=a*b
print("a=", a, "type(a):", type(a))

# a= 55.0 type(a): <class 'float'>

a = 6 + 4j
b = 3 + 2j
print("Augmented multiplication of complex and complex")
a *= b  # equivalent to a=a*b
print("a=", a, "type(a):", type(a))

# a *= b-> a =(6+4j) * (3+2j)
# a= (10+24j) type(a): <class 'complex'>


# Augmented Floor division Operator (//=)
a = 10
b = 5
print("Augmented floor division operator with int and int")
a //= b  # equivalent to a=a//b
print("a=", a, "type(a):", type(a))

# 2 type(a): <class 'int'>
# //= pahle divide karta hai phir, decimal hatata hai , phir answer
# ko a me store karta hai
