# Escape Character

# normal string
normal = "Hello"
print(normal)

# raw string
raw = r"Hello"
print(raw)

# In normal circumstances, there is no difference between the two
# whereas the raw string doesn't process the escape character.
# Example

normal = "Hello\nWorld"
print(normal)
raw = r"Hello\nWorld"
print(raw)

# In the following example, when a normal string is printed..
# the escape character '\n' is processed to introduce a newline.
# However, because of the raw string operator 'r' the effect of escape ..
# character is not translated as per its meaning.


# Escape Characters Example
# ignore \
s = "This string will not include \
backslashes or newline characters."
print(s)

# escape backslash
s = s = "The \\character is called backslash"
print(s)

# escape single quote
s = "Hello 'Python'"
print(s)

# escape double quote
s = 'Hello "Python"'
print(s)

# escape \b to generate ASCII backspace
s = "Hel\blo"
print(s)

# ASCII Bell character
s = "Hello\a"
print(s)

# newline
s = "Hello\nPython"
print(s)

# Horizontal tab
s = "Hello\tPython"
print(s)

# form feed
s = "hello\fworld"
print(s)

# Octal notation
s = "\101"
print(s)

# Hexadecimal notation
s = "\x41"
print(s)

# This string will not include backslashes or newline characters.
# The \character is called backslash
# Hello 'Python'
# Hello "Python"
# Helo
# Hello
# Hello
# Python
# Hello Python
# hello
# world
# A
# A
