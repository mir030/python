# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temp = int(row[1])
#         temperature.append(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# avg_tmp = sum(temp_list)/len(temp_list)
# print(avg_tmp)
# print(data["temp"].mean())
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)


