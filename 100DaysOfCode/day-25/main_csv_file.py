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
#

import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"]
print(temperatures)