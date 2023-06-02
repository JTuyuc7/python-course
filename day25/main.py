# ! Open a CSV file

# import csv
#
# with open('weather_data.csv', mode='r') as data_file:
#     # data = data_file.readlines()
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


import pandas

file = 'weather_data.csv'

data = pandas.read_csv(file)

# print(type(data))
temperatures = data['temp']
# print(temperatures)

# ! Convert a data CSV to a dictionary
data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(temp_list)

# average = 0
# for t in temp_list:
#     average += t
#
# print(f"Average temperature is {average / len(temp_list)}")

# ! Average data using pandas mean()
# print(data['temp'].mean())

# ! Maximum value using pandas max()
# print(data['temp'].max())

# ! Get a specific data in a row using pandas
# print(data[data['day'] == 'Monday'])

# ! Get the row with the maximum temperature on the file
# print(data[data['temp'] == data['temp'].max()])

monday = data[data['day'] == 'Monday']
# print(monday.condition)

monday_temp = monday['temp']
monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# ! Create a DataFrame from scratch
data_dict_frame = {'student': ['Amy', 'Penny', 'Bernadette'], 'scored': [76, 56, 65]}

# ! Initialize the DataFrame class and pass the date you want to crete a data frame
data_frame = pandas.DataFrame(data_dict_frame)
print(data_frame)

# ! Create a new csv file from the date frame created
data_frame.to_csv('my_first_data_frame.csv')
