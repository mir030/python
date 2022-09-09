# numbers = [1, 2, 3]
# list = [n+1 for n in numbers]
# print(list)
#
# name = "Mir Karim"
# new_list = [n for n in name]
# print(new_list)
# print(name.split())

# list = [n * 2 for n in range(1, 5)]
# print(list)
#
names = ["Jim", "Pam", "Meredith", "Creed", "Ryan"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
#
# numbers = [1, 2, 3, 4, 9]
# squared_numbers = [n for n in numbers if n % 2 == 0]
# print(squared_numbers)

# with open("file1.txt") as file:
#     list_1 = file.read().split()
# with open("file2.txt") as file:
#     list_2 = file.read().split()
#
# new_list = [int(n) for n in list_1 if n in list_2]
#
# print(new_list)
# {new_key:new_value for item in list/Dict}
# import random
#
# sales_score = {name: random.randint(1, 100) for name in names}
# passed_students = {key: value for (key, value) in sales_score.items() if value>=60}
# print(passed_students)

# sentence = "My name is Mir and I am learning python. I am a python developer"
# sentence_list = sentence.split()
#
# result_dict = {key: len(key) for key in sentence_list}
# print(result_dict)
#
# celsius_dict = {
#     "Monday": 35,
#     "Tuesday": 40,
#     "Wednesday": 20
# }
#
# fahrenheit_dict = {key: (value * 9 / 5) + 32 for (key, value) in celsius_dict.items()}
# print(fahrenheit_dict)