#challenge  - extract all the temperature into a list in int format

# import csv
# temperature = []
# with open("./weather_data.csv") as datafile:
#     for row in csv.reader(datafile):
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

#calculate the average of the temperature
import pandas

# weather_data = pandas.read_csv("./weather_data.csv")
#
# print(weather_data["temp"].tolist())
# temperature = weather_data["temp"].tolist()
# avg_temperature = sum(temperature) / len(temperature)
# print(f"Average temperature : {avg_temperature}")
#
# print(f"average using pandas : {weather_data['temp'].mean()}")
#
# print(f"Max value using pandas : {weather_data['temp'].max()}\n\n")
#
# # print(weather_data.condition)   #another method to use without weather_data["condition"]
#
# print(weather_data[weather_data.day == "Monday"])
#
# #challenge - get the row which has the maximum temperature
# print(f"\n\nMax temp weather : {weather_data[weather_data.temp == weather_data.temp.max() ]}")
#
# max_temp = weather_data[weather_data.temp == weather_data.temp.max() ]
#
# print(f"\n\nmax temperature condition : {max_temp.condition}\n\n")
#
# #dataframe using dict
# data_dict = {
#     "icecream": ["strawberry", "belgium choco"],
#     "rating": [4, 5]
# }
# df = pandas.DataFrame(data_dict)
# print(df)
# df.to_csv("data.csv")

sq_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = sq_data[sq_data["Primary Fur Color"] == "Gray"]["Primary Fur Color"]
black = sq_data[sq_data["Primary Fur Color"] == "Black"]["Primary Fur Color"]
cinnamon = sq_data[sq_data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"]

data_dict = {"color": ["gray", "black", "cinnamon"], "count": [gray.count(), black.count(), cinnamon.count()]}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("color_count_data.csv")
