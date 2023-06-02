import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
my_dic = {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# ! DAY 26 PROJECT

data_file = 'nato_phonetic_alphabet.csv'
read_file = pandas.read_csv(data_file)
data_file_data_frame = pandas.DataFrame(read_file)

phonetic_dict = {row.letter: row.code for (index, row) in data_file_data_frame.iterrows()}

print(phonetic_dict)

user_input = input('Enter a word: \n').upper()

# split_word = [letter for letter in [*user_input]]
output_list = [phonetic_dict[letter] for letter in user_input]

print(output_list)