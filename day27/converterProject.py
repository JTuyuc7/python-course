import tkinter

window = tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

MILES_CONSTANT = 1.60934


# ! Labels and Button config
def button_converter():
    user_data = float(user_input.get())
    result_km = user_data * MILES_CONSTANT
    label_conversion.config(text=f'{result_km}')


# ! Input
user_input = tkinter.Entry(width=15)
user_input.grid(column=1, row=0)

# ! Miles Label
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

# ! Equal to label
label_equal = tkinter.Label(text='Is equal to')
label_equal.grid(column=0, row=1)

# ! Result label
label_conversion = tkinter.Label(text=f'{0}')
label_conversion.grid(column=1, row=1)
label_conversion.config(pady=15)

# ! Km result
label_km = tkinter.Label(text='Km')
label_km.grid(column=2, row=1)

# ! Button element
button = tkinter.Button(text='Convert', command=button_converter)
button.grid(column=1, row=2)
button.config(pady=5)

window.mainloop()
