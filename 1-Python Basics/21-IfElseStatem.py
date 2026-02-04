# Python is used to execute a block of code when the condition in the if..
# ..statement is true,and another block of code when the condition is false.

# if elif else
amount = 2500
print("Amount = ", amount)
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
else:
    discount = 0

print("Payable amount = ", amount - discount)
