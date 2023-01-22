from tkinter import *


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate():
    a = int(first_number.get())
    b = int(second_number.get())
    if operation.get() == 1:
        result.set(add(a, b))
    elif operation.get() == 2:
        result.set(subtract(a, b))
    elif operation.get() == 3:
        result.set(multiply(a, b))
    elif operation.get() == 4:
        result.set(divide(a, b))
    else:
        result.set("Invalid operation")


root = Tk()
root.title("Mini Calculator")
root.geometry("300x300")
root.resizable(0, 0)

first_number = StringVar()
second_number = StringVar()
operation = IntVar()
result = StringVar()

Label(root, text="First Number").grid(row=0, column=0)
Entry(root, textvariable=first_number).grid(row=0, column=1)
Label(root, text="Second Number").grid(row=1, column=0)
Entry(root, textvariable=second_number).grid(row=1, column=1)

Radiobutton(root, text="Add", variable=operation, value=1).grid(row=2, column=0)
Radiobutton(root, text="Subtract", variable=operation, value=2).grid(row=2, column=1)
Radiobutton(root, text="Multiply", variable=operation, value=3).grid(row=3, column=0)
Radiobutton(root, text="Divide", variable=operation, value=4).grid(row=3, column=1)

Button(root, text="Calculate", command=calculate).grid(row=4, column=0)
Label(root, text="Result").grid(row=5, column=0)
Entry(root, textvariable=result).grid(row=5, column=1)

root.mainloop()
