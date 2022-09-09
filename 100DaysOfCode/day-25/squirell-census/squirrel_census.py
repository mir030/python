import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = 0
red_count = 0
black_count = 0
for fur_color in data["Primary Fur Color"]:
    if fur_color == "Gray":
        grey_count += 1
    elif fur_color == "Cinnamon":
        red_count += 1
    elif fur_color == "Black":
        black_count += 1

"""Another way of doing it. Instead of using for loops"""
# gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# gray_squirrels_count = len(gray_squirrels)
# print(gray_squirrels_count)

dictionary = pandas.DataFrame({
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_count, red_count, black_count]
})

dictionary.to_csv("squirrel.csv")


