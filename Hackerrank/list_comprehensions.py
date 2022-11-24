def square_numbers(x):
    squares = []
    for i in x:
        squares.append(i * i)
    return squares


print(square_numbers([1, 2, 3]))

x = [1, 2, 3]
print(list(map(lambda i: i * i, x)))

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

my_list = []
for n in x:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

my_list = [n for n in x if n % 2 == 0]
print(my_list)

my_list = [(x, y) for x in "abcd" for y in range(4)]
print(my_list)

names = ["Bruce", "Clark", "Peter"]
heroes = ["Batman", "Superman", "Spiderman"]

my_dict = {x: y for x, y in zip(names, heroes) if x != "Peter"}
print(my_dict)

nums = [1, 1, 2, 2, 3, 4]
my_set = {n for n in nums}
print(my_set)

my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)

my_dict = {key: value for key, value in zip([1, 2, 3], ["A", "B", "C"])}
print(my_dict)


# return a list of all the elements that occurs more than one times
some_list = ['a', 'a', 'b', 'c']
duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)