# Tkinter Tutorial
# Adding a status bar

# Importing everything from Tkinter using the sign *
from os import stat
from tkinter import *

# Importing PILLOW module
from PIL import ImageTk,Image

# Taking the GUI functin as TK
root = Tk()

# Giving a title to our GUI
root.title("Image viewer app")

# Taking images as input
myimage1 = ImageTk.PhotoImage(Image.open("images\pexels-céline-13290875.jpg"))
myimage2 = ImageTk.PhotoImage(Image.open("images\pexels-ryan-klaus-13235420.jpg"))
myimage3 = ImageTk.PhotoImage(Image.open("images\pexels-vinh-lâm-13370190.jpg"))
myimage4 = ImageTk.PhotoImage(Image.open("images\multi.jpg"))

# Making an array to take images for interpreting easily
img_list = [myimage1, myimage2, myimage3, myimage4]

# Output Screen Code
myLabel = Label(image = myimage1)
myLabel.grid(row=0, column=0, columnspan=3)

# Adding a status bar
status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)

# Creating Forward & Back Function
def forward(image_number):
    global myLabel
    global forward_button
    global back_button

    myLabel.grid_forget()
    myLabel = Label(image=img_list[image_number-1])

    forward_button = Button(root, text=">>", command= lambda: forward(image_number+1))
    back_button = Button(root, text="<<", command= lambda: back(image_number-1))

    if image_number == 5:
        forward_button = Button(root, text=">>", command=DISABLED)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)
    myLabel.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global myLabel
    global forward_button
    global back_button

    myLabel.grid_forget()
    myLabel = Label(image=img_list[image_number-1])

    forward_button = Button(root, text=">>", command= lambda: forward(image_number-1))
    back_button = Button(root, text="<<", command= lambda: back(image_number+1))

    if image_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    myLabel.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

# Creating back, exit & forward button
back_button = Button(root, text="<<", command=back, state=DISABLED)
exit_button = Button(root, text="Exit Program", command=root.quit)
forward_button = Button(root, text=">>", command= lambda: forward(2))

# Inputing the back, exit, forward button to screen
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

# Putting the status bar on the screen

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()