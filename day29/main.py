# ! Imports
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    # ! Copy to clipboard
    pyperclip.copy(password)


# * -------------------------- SEARCH -------------------------------------- #

def find_password():
    website_search = website_entry.get()
    if len(website_search) <= 0:
        messagebox.showwarning(title='Warning', message='Please enter a value to search')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title='File not found', message='You dont\'t have any password stored')
        else:
            data_result = {website: value for (website, value) in data.items() if website.lower() == website_search.lower()}
            if data_result:
                result = list(data_result)
                website_info = result[0]
                email_info = data_result[result[0]]['Email']
                password_info = data_result[result[0]]['Password']
                messagebox.showinfo(title=f'{website_info} result', message=f'Email: {email_info}\n Password: {password_info}\n')
            else:
                messagebox.showwarning(title='Error', message=f'{website_search} not found in our records')
        finally:
            website_entry.delete(0, tkinter.END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if website_text == '' or password_text == '':
        messagebox.showwarning(title='Invalid', message='Please fill the fields')
    else:
        is_this_ok = messagebox.askokcancel(title=website_text,
                                            message=f'Your info: \nEmail: {email_text}\nPassword: {password_text} \n Is this ok?')
        new_dict = {website_text: {
            'Email': email_text,
            'Password': password_text
        }}
        if is_this_ok:
            try:
                with open('data.json', 'r') as file_to_save:
                    # ! Read json data
                    data = json.load(file_to_save)
            except FileNotFoundError:
                with open('data.json', 'w') as file_to_save:
                    json.dump(new_dict, file_to_save, indent=6)
            else:
                # * Update data
                data.update(new_dict)

                with open('data.json', 'w') as file_to_save:
                    # ! Save the update JSON data
                    json.dump(data, file_to_save, indent=6)
                    # file_to_save.write(f'{website_text} | {email_text} | {password_text}\n')
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                # file_to_save.close()


# !---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.minsize(width=550, height=400)
window.config(padx=30, pady=20)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ! Labels
website_label = tkinter.Label(text='Website:')
website_label.grid(column=0, row=1, columnspan=1)

email_label = tkinter.Label(text='Email/Username')
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password')
password_label.grid(column=0, row=3)

# ! Entries
website_entry = tkinter.Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

email_entry = tkinter.Entry(width=40)
email_entry.insert(0, 'myEmail@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=23)
password_entry.grid(column=1, row=3, columnspan=1)

# ! Buttons
generate_password_button = tkinter.Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=2)

add_button = tkinter.Button(text='Add', width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)

# ! Keep the program running
window.mainloop()
