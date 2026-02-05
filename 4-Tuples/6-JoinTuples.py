# Joining Tuples Using Concatenation ("+") Operator

# Two tuples to be joined
t1 = (10, 20, 30, 40)
t2 = ("one", "two", "three", "four")
# joining the tuples
joined_tuple = t1 + t2
# printing the joined tuple
print("joined tuple: ", joined_tuple)


# Joining Tuples Using List Comprehension

# Two tuples to be joined
T1 = (36, 24, 3)
T2 = (84, 5, 81)
# Joining the tuples using list comprehension
joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# Printing the joined tuple
print("Joined Tuple:", joined_tuple)


# Joining Tuples Using extend() Function

T1 = (10, 20, 30, 40)
T2 = ("one", "two", "three", "four")
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print("Joined Tuple:", T1)


# Join Tuples using sum() Function

T1 = (10, 20, 30, 40)
T2 = ("one", "two", "three", "four")
T3 = sum((T1, T2), ())
print("Joined Tuple:", T3)
