from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width = 35, borderwidth = 8)
e.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
        
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
        
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
        
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



button1 = Button(root, text = "1", padx=30, pady=20, command= lambda: buttonClick(1))
button2 = Button(root, text = "2", padx=30, pady=20, command= lambda: buttonClick(2))
button3 = Button(root, text = "3", padx=30, pady=20, command= lambda: buttonClick(3))
button4 = Button(root, text = "4", padx=30, pady=20, command= lambda: buttonClick(4))
button5 = Button(root, text = "5", padx=30, pady=20, command= lambda: buttonClick(5))
button6 = Button(root, text = "6", padx=30, pady=20, command= lambda: buttonClick(6))
button7 = Button(root, text = "7", padx=30, pady=20, command= lambda: buttonClick(7))
button8 = Button(root, text = "8", padx=30, pady=20, command= lambda: buttonClick(8))
button9 = Button(root, text = "9", padx=30, pady=20, command= lambda: buttonClick(9))
button0 = Button(root, text = "0", padx=30, pady=20, command= lambda: buttonClick(0))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_equal = Button(root, text = "=", padx = 91, pady = 20, command = button_equal)
button_Clear = Button(root, text = "Clear", padx = 79, pady = 20, command = button_clear)

button_substract = Button(root, text = "-", padx = 40, pady = 20, command = button_substract)
button_multiply = Button(root, text = "*", padx = 39, pady = 20, command = button_multiply)
button_division = Button(root, text = "/", padx = 39, pady = 20, command = button_division)

button1.grid(row=3, column = 0)
button2.grid(row=3, column = 1)
button3.grid(row=3, column = 2)

button4.grid(row=2, column = 0)
button5.grid(row=2, column = 1)
button6.grid(row=2, column = 2)

button7.grid(row=1, column = 0)
button8.grid(row=1, column = 1)
button9.grid(row=1, column = 2)

button0.grid(row=4, column = 0)
button_Clear.grid(row=4, column=1, columnspan = 2)
button_add.grid(row=5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_division.grid(row=6, column=2)

root.mainloop()