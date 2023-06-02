import tkinter

# ! Initialize the tkinter class
window = tkinter.Tk()

# ! Change the title of the program
window.title('My first program using TKInter')

# ! Change the width and height of the screen
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# ! Create labels
my_label = tkinter.Label(text='My Label', font=('Arial', 26, 'bold'))
# my_label.pack()
# ! Using place
# my_label.place(x=0, y=0)
# ! Using Grid
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text='Button got clicked')
    new_text = input.get()
    my_label.config(text=new_text)
    print(f'They clicked me xD')
    window.title(new_text)


# ! Buttons
button = tkinter.Button(text='Click me XD', command=button_clicked )
# button.pack()
button.grid(column=1, row=1)

button_1 = tkinter.Button(text='Another button', command=button_clicked)
button_1.grid(column=2, row=0)

# ! Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=2, row=2)



window.mainloop()
