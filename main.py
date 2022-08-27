import tkinter

#---------------------Constant---------------------------#
GREEN = "green"
SKYBLUE = "SkyBlue3"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔️"
index = 0
countdown_timer = ""

#------------------timer reset-------------------------#


def reset_timer():
    global index
    index = 0
    title_lable.config(text="Timer")
    check_mark_label.config(text="")
    canvas.itemconfig(time_text, text="00:00")
    global countdown_timer
    window.after_cancel(id=countdown_timer)


#-------------------timer mechanism--------------------#


def start_timer():
    global index
    index += 1
    if index % 8 == 0:
        check_mark_label.config(text=CHECK_MARK*(index // 2))
        title_lable.config(text="Long Break")
        count_down(LONG_BREAK_MIN*60)
    elif index % 2 == 0:
        check_mark_label.config(text=CHECK_MARK*(index // 2))
        title_lable.config(text="Break")
        count_down(SHORT_BREAK_MIN*60)
    elif index % 2 == 1:
        title_lable.config(text="Work")
        count_down(WORK_MIN*60)


#-------------------countdown mechanism---------------#


def count_down(sec_number):

    min = sec_number // 60
    sec = sec_number % 60
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(time_text, text=f"{min}:{sec}")
    if sec_number > 0:
        global countdown_timer
        countdown_timer = window.after(1000, count_down, sec_number - 1)
    else:
        start_timer()


#-------------------UI Setup---------------------------#
# create the window
window = tkinter.Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=SKYBLUE)


# create a canvas so we can put things on top of each other
canvas = tkinter.Canvas(width=200, height=224,
                        bg=SKYBLUE, highlightthickness=0)
# it can have the png file directrly so we have to use photoimage
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 23, "bold"), fill="snow")
canvas.grid(column=1, row=1)

# creat timer label
title_lable = tkinter.Label(text="Timer", font=(
    FONT_NAME, 33, "bold"), padx=20, pady=20, bg=SKYBLUE, fg="snow")
title_lable.grid(column=1, row=0)

# start bottun
start_button = tkinter.Button(text="Start", font=(
    FONT_NAME, 20, "bold"), padx=20, pady=10, bg=SKYBLUE, fg="snow", borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)


# reset button
reset_button = tkinter.Button(text="Reset", font=(
    FONT_NAME, 20, "bold"), padx=20, pady=10, bg=SKYBLUE, fg="snow", borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# check marks label
check_mark_label = tkinter.Label(
    text="", padx=20, pady=20, bg=SKYBLUE, fg=GREEN, font=(
        FONT_NAME, 15, "bold"))
check_mark_label.grid(column=1, row=3)
window.mainloop()
