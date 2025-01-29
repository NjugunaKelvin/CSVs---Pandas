# with open("./weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)


# import csv

# with open("./weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     # a csv object is created
#     temperatures = []
#     # loop through
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)



# CSV CAN BE UNRELIABLE SOMETIMES
# THAT'S WHERE PANDAS COMES IN

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

# print(type(data))

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# turn to a list

temp_list = data["temp"].to_list()

# Get data in columns
# print(temp_list)
print(max(data["temp"]))


# Get data in rows
# print(data[data.day == "Monday"])

# The day we had maximum temp

# print(data[data.temp == max(data["temp"])])

# create a data frame from scratch
data_dict = {
    "students": ["Tom", "James", "Abel"],
    "scores": [78, 89, 65]
}

data_set = pandas.DataFrame(data_dict)

print(data_set)

data_set.to_csv("new_data.csv")