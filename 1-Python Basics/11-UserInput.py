# User Input Functions
name = "Ayush"
city = "Uttar pardesh"

print("Hello My name is", name)
print("I am from", city)


# The input() Function
name = input("Enter your name :")
city = input("Enter Where are you from :")

print("Hello My name is", name)
print("I am from ", city)


# #Taking Numeric Input in Python
# width = input("Enter width : ")
# height = input("Enter height : ")

# area = width*height
# print ("Area of rectangle = ", area)

# You get a TypeError because:

# "20" and "30" are strings, not numbers.
# Multiplying two strings is not allowed in Python./


width = int(input("Enter width : "))
height = int(input("Enter height : "))

area = width * height
print("Area of rectangle = ", area)


# float() function converts a string into a float object

amount = float(input("Enter Amount : "))
rate = float(input("Enter rate of interest : "))

interest = amount * rate / 100
print("Amount: ", amount, "Interest: ", interest)


# The print() Function
a = "Hello World"
b = 100
c = 25.50
d = 5 + 6j
print("Message: a")
print(b, c, b - c)
print(pow(100, 0.5), pow(c, 2))  # power 100 ka 0.5 and 25.50 ka square


# septrated parameter for the print() function.(sep=',')
city = "Hyderabad"
state = "Telangana"
country = "India"
print(city, state, country, sep=",")

# To make these two lines appear in the same line, define end parameter
city = "Hyderabad"
state = "Telangana"
country = "India"

print("City:", city, end=" ")
print("State:", state)
