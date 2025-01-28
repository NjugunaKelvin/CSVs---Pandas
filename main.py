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

import pandas as pd
# Plot a column
df['ColumnName'].plot()

# Plot a histogram
df['ColumnName'].hist()

