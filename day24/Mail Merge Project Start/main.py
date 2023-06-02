# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# ! Open the file

PLACE_HOLDER = '[name]'
names = []

with open('./Input/Names/invited_names.txt', 'r') as file_name:
    names = file_name.readlines()
    # print(names, 'ahora si')

with open('./Input/Letters/starting_letter.txt', 'r') as letter:
    content = letter.read()
    # clean_content = content.strip()

    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACE_HOLDER, f"{stripped_name}")
        with open(f'./Output/ReadyToSend/{stripped_name}_letter.txt', mode='w') as final_letter:
            final_letter.write(new_letter)
        # new_letter = content.replace(PLACE_HOLDER, name + ',')
        # with open(f"./Output/ReadyToSend/{name}_letter.txt", mode='w') as final_letter:
        #     final_letter.write(new_letter)
