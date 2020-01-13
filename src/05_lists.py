# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)
# Should Return: 
[1, 2, 3, 4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
 x.extend(y)
print(x)
# Should Return:
[1, 2, 3, 4, 8, 9, 10]


# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)
# Should Return: 
[1, 2, 3, 4, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(len(x) -1, 99)
print(x)
# Should Return: 
[1, 2, 3, 4, 9, 99, 10]

# Print the length of list x
print(len(x))
# Should Return: 
8

# Print all the values in x multiplied by 1000
for val in x: 
    print(val * 1000)