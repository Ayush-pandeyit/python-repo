# This might surprise you:
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3!)

# Why? Because 0.1 and 0.2 can't be represented exactly in binary

# Comparing Floats
# Because of precision issues, never compare floats with == for equality
a = 0.1 + 0.2
print(a == 0.3)  # False
