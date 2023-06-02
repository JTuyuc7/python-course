# ! List comprehension
# ! Is the way of creating a list from a previous list
import random
import pandas
numbers = [1, 2, 3, 4, 5, 6]

new_list = [n + 1 for n in numbers]

# print(new_list)

name = 'James'
letter_list = [letter for letter in name]
# print(letter_list)

list_range_double = [n * 2 for n in range(1, 5)]

# print(list_range_double)

list_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_list_name = [name for name in list_names if len(name) <= 4]

long_list_name = [n.upper() for n in list_names if len(n) >= 5]
# print(long_list_name)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

# print(result)

# ! Dictionary Comprehension

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}

# print(students_scores)

passed_students = {new_name: new_score for (new_name, new_score) in students_scores.items() if new_score > 61}
# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
letter_list = sentence.split()
dict_list = {word: len(word) for word in letter_list}

# print(letter_list)
# print(dict_list)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

# print(weather_f)

# ! Looping over nested dictionary
student_dict = {
    'students': ['Angela', 'James', 'Penny'],
    'score': [56, 76, 98]
}

students_data_frame = pandas.DataFrame(student_dict)

# print(students_data_frame)
# ! Loop through rows of a data frame
for (index, row) in students_data_frame.iterrows():
    # print(index) # Print the index
    # print(row) # Print all row
    print(row.students)
    print(row.score)
