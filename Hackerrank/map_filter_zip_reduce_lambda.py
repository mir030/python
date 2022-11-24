from functools import reduce
# map
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


"""map doesn't change the initial list. 
So it doesn't affect the outside world"""
print(list(map(multiply_by2, my_list)))
print(my_list)


# Filter


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

# Zip
# it can be used on iterable like tuples, etc
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
print(my_list)
print(your_list)


# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))

# lambda expressions
my_list = [1, 2, 3]
print(list(map(lambda i: i * 2, my_list)))

# filter elements similar to if condition
print(list(filter(lambda item: item % 2 != 0, my_list)))

# square with lambda
print(list(map(lambda x: x * x, my_list)))

# List sorting based on second element of tuples
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1], reverse=True)
print(a)

# List comprehensions


