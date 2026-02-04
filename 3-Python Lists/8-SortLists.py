# Sorting List in Lexicographical order

list1 = ["Physics", "Biology", "Chemistry", "Maths"]
print("list before sort :", list1)
list1.sort()
print("list after sort :", list1)

# Sorting list in numerical order

list2 = [8, 9, 4, 43, 31]
print("list before sort :", list2)
list2.sort()
print("List after sort : ", list2)


# Sorting Lists Using sorted() Method

numbers = [3, 1, 4, 5, 7, 8, 9, 4, 6, 2]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)


# Using str.lower() as key Parameter

list1 = ["Physics", "biology", "Biomechanics", "psychology"]
print("list before sort", list1)
list1.sort(key=str.lower)
print("list after sort : ", list1)


# Using user-defined Function as key Parameter
def myfunction(x):
    return x % 10


list1 = [17, 23, 46, 51, 90]
print("list before sort", list1)
list1.sort(key=myfunction)
print("list after sort : ", list1)
