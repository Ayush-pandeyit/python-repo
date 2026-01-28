#Python Bitwise NOT Operator (~)

-1 is complement(1 - 1) = complement(0) = "11111111"
-10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110"

# Python Bitwise NOT Operator (~) - Explanation
# What is NOT?
# The NOT operator (~) flips every bit: 1 becomes 0, and 0 becomes 1.
# Simple flip:
# -0 = 1
# -1 = 0

# But Why Does ~5 Give -6?
# This is where it gets interesting! Python uses 2's...
#  ...complement representation for negative numbers.
# The Formula:
# ~x = -(x + 1)
# Examples :
# ~5 = -6
# ~10 = -11
# ~0 = -1
# ~(-1) = 0