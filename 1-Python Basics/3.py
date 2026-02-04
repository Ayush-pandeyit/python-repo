# Numeric Data Tyhpe

Var1 = 1
Var2 = True
Var3 = 10.303
Var4 = 10 + 2j
print(type(Var1))
print(type(Var2))
print(type(Var3))
print(type(Var4))


# Example of Numeric Data type
# integer variable
a = 100
print("the type of variable having value", a, "is", type(a))


# Example of String Data Type

str = "Hello world!"
print(str)
print(str[0])
print(str[2:5])
print(str[2:5])
print(str * 2)


# Python List Data Type
type([2023, "Ayush", 3.11, 5 + 6j, 1.23e-4])
<class 'list'>


# Python Tuple Data Type
type((2023, "python", 3.11, 5+6j, 1.23E-4))
<class <'tuple'>


# Range Data Type
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)


# Python set type
type({2023, "Ayush", 3.22, 5+6j, 1.2E-4})
<class 'set'>


# Example of Set
set1 = {123, 452, 5, 6}
set2 = {"Java", "Python", "JavaScript"}

print(set1)
print(set2)

# Getting Data Type

# Getting type of values
print(type(123))
print(type(9.99))

# Getting type of variables
a = 10
b = 2.12
c = "Hello"
d = (10, 20, 30)
e = [10, 20, 30]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# Python Data Type Conversion

# print("Conversion to integer data type")
a = int(1)  # a will be 1
b = int(2.2)  # b will be 2
c = int("3.3")  # c will be 3

print(a)
print(b)
print(c)

# print("Conversion to floating point number")
a = float(1)  # a will be 1.0
b = float(2.2)  # b will be 2.2
c = float("3.3")  # c will be 3.3

print(a)
print(b)
print(c)

# print("Conversion to string")
a = str(1)  # a will be "1"
b = str(2.2)  # b will be "2.2"
c = str("3.3")  # c will be "3.3"

print(a)
print(b)
print(c)
