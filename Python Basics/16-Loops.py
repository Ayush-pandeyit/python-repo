# The for Loop
words = ["one", "two", "three"]
for x in words:
    print(x)

# The while Loop
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
x = 0

while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")

# The continue Statement
for letter in "Python":
    # continue when letter is 'h'
    if letter == "h":
        continue
    print("Current Letter :", letter)
