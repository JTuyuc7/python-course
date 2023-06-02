# # ! Introduction to read files using paython
#
# # ! Open the desired file
# file = open("my_file.txt", 'r')
#
# # ! Read the content of the file
# content = file.read()
#
# # ! print the content file
# print(content)
#
# # ! Close the file
# file.close()

# ! Other way to open a file using python
# with open("my_file.txt") as file:
#     content =  file.read()
#     print(content)

with open("my_file.txt", mode='a') as file:
    file.write('\nThis should be a new content written inside the document \n')

# with open("/Users/jaimetuyuc/Desktop/my_file1.txt", mode='a') as file:
#     file.write('\nUsing a new document with Python and relative path? \n')

with open("../../../../my_file1.txt", mode='a') as file:
    file.write('\nUsing a new document with Python and relative path? \n')

# ! a = append
# ! w = write
# ! r = read
