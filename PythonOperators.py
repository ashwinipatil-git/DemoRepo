
# Usage of is and is not operator
# is ans is not operators are identity operators in Python.
# They are used to check if two values(or variables) are located
# on the same part of the memory
x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# here x1 and y1 are integers of same values, so they are equal as well as identical
# Output False
print(x1 is not y1)

print(x2 is y2)

print(x3 is y3)

# Membership Operators

# in and in not are membership operators in Python. They are used to test whether a value
# or variable is found in sequence(string, list, tuple, set and dictionary)

x = "Hello World"
y = {1: 'a', 2: 'b'}

print("Now membership operators:")
# output : True
print('H' in x)

print('hello' not in x)

print(1 in y)

print('a' in y)


