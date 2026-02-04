# CASE CONVERSION METHODS

# upper() - Convert to uppercase
s = "hello"
print(s.upper())  # HELLO


# lower() - Convert to lowercase
pythons = "HELLO"
print(s.lower())  # hello

# capitalize() - First character uppercase, rest lowercase
s = "hello world"
print(s.capitalize())  # Hello world

# title() - First character of each word uppercase
s = "hello world"
print(s.title())  # Hello World

# swapcase() - Swap case of all characters
s = "Hello World"
print(s.swapcase())  # hELLO wORLD


# casefold() - Aggressive lowercase (for case-insensitive comparisons)
s = "HELLO"
print(s.casefold())  # hello
# Better than lower() for comparisons with special characters
