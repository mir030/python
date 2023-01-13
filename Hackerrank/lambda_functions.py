from functools import reduce

# Square just one number
sqr = lambda x: x * x
print(sqr(5))

# Square a list
my_list = [1, 2, 3]
print(list(map(sqr, my_list)))

# Filter
print(list(filter(lambda x: x % 2 != 0, my_list)))

# Zip
# it can be used on iterable like tuples, etc
your_list = [10, 20, 30]
print(list(zip(my_list, your_list)))

# Reduce
# Find the single element in an array
arr = [1, 2, 3, 4, 3, 2, 1]
result = reduce(lambda x, y: x ^ y, arr)
print(result)

# Reverse sort of a list
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1], reverse=True)
print(a)
