# Using % operator

name = "Tutorialspoint"
print("Welcome to %s!" % name)


# Using format() method
str = "Welcome to {}"
print(str.format("Tutorialspoint"))


# Using f-string
item1_price = 2500
item2_price = 300
total = f"Total: {item1_price +  item2_price}"
print(total)


# Using String Template class

from string import Template

str = "Hello and welcomne to $name !"
templateObj = Template(str)
new_str = templateObj.substitute(name="TUtorialspoint")
print(new_str)
