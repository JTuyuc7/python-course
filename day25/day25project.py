
# ! Day 25 project

import pandas

data_file = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(data_file['Primary Fur Color'])

grey_squirrels = data_file[data_file['Primary Fur Color'] == 'Gray']
gray_squirrels_count = len(data_file[data_file['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data_file[data_file['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data_file[data_file['Primary Fur Color'] == 'Black'])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {"Fur Color": ['Gray', 'Cinnamon', 'Black'], "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]}
new_data_frame = pandas.DataFrame(data_dict)
print(new_data_frame)
new_data_frame.to_csv('Squirrels_count.csv')