# ! IMPORTS
import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ! ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    global reps
    # ! Cancel timer
    window.after_cancel(timer)
    # ! Reset text timer
    canvas.itemconfig(text_timer, text="00:00")
    # ! Reset Reps
    reps = 0
    # ! REset title
    timer_label.config(text='Timer')


# !---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break Time", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break Time", foreground=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", foreground=GREEN)


# !---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(text_timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += '✓'
        check_marks.config(text=mark)


# !---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()

# ! Title
window.title('Pomodoro Program xD')
window.config(padx=100, pady=50, bg=YELLOW)

# ! Canvas Image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# ! Get the image from the file
tomato_img = tkinter.PhotoImage(file='tomato.png')
# ! Put the image on the canvas object
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

# ! Create a text using canvas
text_timer = canvas.create_text(108, 130, text="00:00", fill='white', font=(FONT_NAME, 40, 'normal'))

# ! Timer label
timer_label = tkinter.Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
timer_label.grid(column=1, row=0)

# ! Start button
start_button = tkinter.Button(text="Start", foreground='black', bg=YELLOW, highlightbackground=YELLOW,
                              font=(FONT_NAME, 18, 'bold'), command=start_timer)
start_button.config(pady=0, padx=0)
start_button.grid(column=0, row=2)

# ! Reset Button
reset_button = tkinter.Button(text='Reset', foreground='black', bg=YELLOW, highlightbackground=YELLOW,
                              font=(FONT_NAME, 18, 'bold'), command=reset_timer)
reset_button.grid(column=2, row=2)

# ! Check label
check_marks = tkinter.Label(foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
check_marks.grid(column=1, row=3)

# ! Keep the program running
window.mainloop()
