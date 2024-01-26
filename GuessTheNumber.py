# Created by Jim Grysmpolakis.
# Please do not claim as yours.

from tkinter import *
import random
import time
from tkinter import ttk
from ttkthemes import ThemedTk

# Set the screen.
screen = ThemedTk(theme="breeze")
screen.configure(themebg="breeze")
screen.geometry("600x470")
screen.title("Guess the Number")

# Set game variables.
tries = 0
State = DISABLED
number = 0
num = 0
Tries = ttk.Label()


# When enter is pressed. Checks the number of the entry and
# changes the color of the tries Label.
def start(event):
    global number
    global tries
    global Tries

    try:
        num = int(entry.get())
        if number == num:
            Image.configure(image=correct)
            entry.configure(state=DISABLED)
            stats.configure(text="You can't write now! Press Generate.")
            stats.place(x=190, y=230)
            entry.delete(0, END)
            tries += 1
            GenerateButton.configure(state=NORMAL)
        elif num > number:
            Image.configure(image=downarrow)
            entry.delete(0, END)
            tries += 1
        elif num < number:
            Image.configure(image=uparrow)
            entry.delete(0, END)
            tries += 1

        if tries == 0:
            Tries.configure(foreground="black")
        elif tries > 0 and tries <= 4:
            Tries.configure(foreground="green")
        elif tries > 4 and tries <= 8:
            Tries.configure(foreground="orange")
        elif tries > 8:
            Tries.configure(foreground="red")

        Tries.configure(text="Tries: " + str(tries))

    # If user has not pressed generate.
    except:
        print("Before you press enter, press generate to start the game.")


# Generate Number.
def generate():
    global State
    global tries
    global Tries
    global number

    tries = 0
    entry.delete(0, END)

    number = 1
    entry.delete(0, END)

    difficulty = RB.get()
    if difficulty == "Easy":
        number = random.randint(1, 49)
    elif difficulty == "Normal":
        number = random.randint(1, 99)
    elif difficulty == "Hard":
        number = random.randint(1, 199)

    LoadingMenu = ttk.Label(screen, text="",
        font=("Helvetica", 13, "bold"))
    LoadingMenu.place(x=20, y=450)

    for i in range(2):
        LoadingMenu.configure(text="Loading.")
        screen.update()
        time.sleep(1)

        LoadingMenu.configure(text="Loading..")
        screen.update()
        time.sleep(1)

        LoadingMenu.configure(text="Loading...")
        screen.update()
        time.sleep(1)

    LoadingMenu.destroy()

    State = NORMAL
    entry.configure(state=State)
    stats.config(text="Write a number you think.\nBe careful with the arrows.")
    stats.place(x=225, y=210)

    Tries = ttk.Label(screen, text="Tries: " + str(tries), font=("Helvetica", 15, "bold"))
    Tries.place(x=270, y=300)
    entry.delete(0, END)

    Image.configure(image=dice)

    GenerateButton.configure(state=DISABLED)


instructions = "Welcome to guess the number! Try to find a random number \n " \
               "    with the least tries you can. To start press generate."

Title = ttk.Label(screen, text="Guess The Number", borderwidth=15, relief="groove", font=("Helvetica", 30, "bold"))

Title.place(x=110, y=10)
Instructions = ttk.Label(screen, text=instructions, font=("Helvetica", 13, "bold"))
Instructions.place(x=60, y=160)

Credentials = ttk.Label(screen, text="Created by Jim Grysmpolakis", font=("Helvetica", 11, "bold"))
Credentials.place(x=390, y=450)

RB = StringVar(value="Normal")

RadioButton1 = ttk.Radiobutton(screen, text="Easy: (0 - 50)", value="Easy", variable=RB)
RadioButton1.place(x=100, y=110)
RadioButton2 = ttk.Radiobutton(screen, text="Normal: (0 - 100)", value="Normal", variable=RB)
RadioButton2.place(x=250, y=110)
RadioButton3 = ttk.Radiobutton(screen, text="Hard: (0 - 200)", value="Hard", variable=RB)
RadioButton3.place(x=400, y=110)

GenerateButton = ttk.Button(screen, text="Generate", command=generate, state=NORMAL)
GenerateButton.place(x=500, y=385)
ExitButton = ttk.Button(screen, text="Exit", command=exit)
ExitButton.place(x=500, y=350)

entry = ttk.Entry(screen, width=20, state=State)
entry.place(x=230, y=260)
stats = ttk.Label(screen, text="You can't write now! Press Generate.", font=("Helvetica", 10, "bold"))
stats.place(x=190, y=230)

correct = PhotoImage(file="correct.png")
downarrow = PhotoImage(file="downarrow.png")
uparrow = PhotoImage(file="uparrow.png")
dice = PhotoImage(file="die.png")

Image = Label(screen, image=dice)
Image.place(x=20, y=332)

screen.bind("<Return>", start)

screen.mainloop()
