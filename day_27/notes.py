# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300) # set size of the window

my_label = Label(text="I am a label", font = ("Ariel", 24, "bold")) #SET at object creation 
my_label.pack() # makes the label centered, after cfreating the component we must also specify how the component is displayed on the screen
# pack has various parameters

my_label["text"] = "New Text" # AFTER object creation
my_label.config(text="New Text") # to UPDATE

# BUTTON

def button_clicked():
    # my_label.config(text="I got clicked")
    my_label.config(text=input.get())
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()

# ENTRY

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop() # will keep window on screen, must be at the very end of the program