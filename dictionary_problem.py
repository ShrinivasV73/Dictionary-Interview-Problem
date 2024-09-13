s = """abc kng saj
       1 2 3
       4 5 6
    """

# Step 1: Splitting each line and getting rid off unnecessary spaces
lines = list(map(str.strip, s.split("\n")[0:-1]))

# Extracting only keys
keys = lines[0].split(" ")
print(keys)
# ['abc', 'kng', 'saj']

# Extracting only numbers 
# each line splitted, int function is mapped to conver '1' to 1 and so on
numbers = [list(map(int, line.split())) for line in lines[1:]]
print(numbers)
# [[1, 2, 3], [4, 5, 6]]

# using list comprehension organize first, second and thrid values
# from two nested corresponding lists
values = [[numbers[0][i], numbers[1][i]] for i in range(0,3)]
print(values)
# [[1, 2, 3], [4, 5, 6]]

# creating empty dictionary
dictionary = {}

# assinging key and value
for i in range(0,3):
    dictionary[keys[i]] = values[i]

# expected output
print(dictionary)
# {'abc': [1, 4], 'kng': [2, 5], 'saj': [3, 6]}