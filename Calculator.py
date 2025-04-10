from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clearf():
    e.delete(0, END)

def button_addf():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equalf():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))

def button_subtract():
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
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_add(0))
button_plus = Button(root, text="+", padx=40, pady=20, command=lambda: button_addf())
button_equal = Button(root, text="=", padx=40, pady=20, command=lambda: button_equalf())
button_clear = Button(root, text="C", padx=40, pady=20, command=lambda: button_clearf())
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: button_subtract())
button_mul = Button(root, text="*", padx=40, pady=20, command=lambda: button_multiply())
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: button_divide())

button_1.grid(row = 3, column =0)
button_2.grid(row = 3, column =1)
button_3.grid(row = 3, column =2)

button_4.grid(row = 2, column =0)
button_5.grid(row = 2, column =1)
button_6.grid(row = 2, column =2)

button_7.grid(row = 1, column =0)
button_8.grid(row = 1, column =1)
button_9.grid(row = 1, column =2)

button_0.grid(row =4 , column =1)
button_plus.grid(row =5 , column =0)
button_clear.grid(row =4 , column =0)
button_equal.grid(row =5 , column =1)
button_sub.grid(row =4, column=2)
button_mul.grid(row =5, column=2)
button_div.grid(row =6, column=0)

root.mainloop()
