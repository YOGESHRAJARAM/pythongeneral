from tkinter import *

# Create the main window
root = Tk()
root.title("Sample Tkinter App")

# Create a label widget
label1 = Label(root, text="This is a label widget")
label1.pack()  # Use pack geometry manager

# Create an entry widget for user input
entry1 = Entry(root)
entry1.pack()  # Use pack geometry manager

# Create a button widget with a function call
def button_clicked():
    print("Button clicked!")
    # You can add more logic here, like updating the label text or performing other actions

button1 = Button(root, text="Click me", command=button_clicked)
button1.pack()  # Use pack geometry manager

# Start the main event loop
root.mainloop()