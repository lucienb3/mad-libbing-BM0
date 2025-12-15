from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("500x200")

msgbox = Text(root, height = 5, width = 30)

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text='Green', background='green')
color_button = Button(root, text='Color of Light', background='white')

#Add a label
label = Label(root, text=" What color is the light")


# Place widgets in window (with pack function!)
red_button.grid(row=0,column=0)
yellow_button.grid(row=0,column=5)
green_button.grid(row=0,column=10)
label.grid(row=10,column=5)
msgbox.grid(row=20,column=5)
color_button.grid(row=20,column=0)

# Start the GUI event loop
root.mainloop()