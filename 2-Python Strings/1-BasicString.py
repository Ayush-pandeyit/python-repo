# Creating python strings in various type

"Welcome To TutorialsPoint"
"Welcome To TutorialsPoint"
"Welcome To TutorialsPoint"
"Welcome To TutorialsPoint"
"""Welcome To TutorialsPoint"""
"Welcome To TutorialsPoint"
"""Welcome To TutorialsPoint"""
"Welcome To TutorialsPoint"

# Accessing Values in Strings
var1 = "Hello World!"
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])


# Updating Strings
var1 = "Hello World!"
print("Updated String :- ", var1[:6] + "Python")

# Python Multiline Strings
var = """
Welcome To
Python Tutorial
from TutorialsPoint
"""
print("var:", var)

# Getting Type of Python Strings

var = "Welcome To TutorialsPoint"
print(type(var))  # str
var = 12345
print(type(var))  # integer
var = 123.678
print(type(var))  # float
