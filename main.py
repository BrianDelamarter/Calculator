import tkinter as tk
number = ""
type = ""
num1 = 0

def press(num):
    global number
    number = number + str(num)
    show.set(number)

def addition():
    global number, type, num1
    num1 = int(number)
    type = "+"
    number = ""
    show.set(number)

def subtraction():
    global number, type, num1
    num1 = int(number)
    type = "-"
    number = ""
    show.set(number)

def multiplication():
    global number, type, num1
    num1 = int(number)
    type = "*"
    number = ""
    show.set(number)

def division():
    global number, type, num1
    num1 = int(number)
    type = "/"
    number = ""
    show.set(number)

def equal():
    global number, type, num1
    num2 = int(number)
    if type =="+":
        number = num1 + num2
    elif type == "-":
        number = num1 - num2
    elif type == "*":
        number = num1 * num2

    elif type == "/":
        number = num1 // num2
    show.set(str(number))

def clear():
    global number, type, num1
    number, type, num1 = "","",""
    show.set(number)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    window.geometry('440x400')
    show = tk.StringVar()
    display = tk.Label(textvariable= show, background = "White", relief = "sunken")
    display.grid(columnspan = 4, ipadx = 200, ipady = 5, padx = 14,pady=10)

    button1 = tk.Button(window, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=5, width=14)
    button1.grid(row=2, column=0)

    button2 = tk.Button(window, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=5, width=14)
    button2.grid(row=2, column=1)

    button3 = tk.Button(window, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=5, width=14)
    button3.grid(row=2, column=2)

    button4 = tk.Button(window, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=5, width=14)
    button4.grid(row=3, column=0)

    button5 = tk.Button(window, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=5, width=14)
    button5.grid(row=3, column=1)

    button6 = tk.Button(window, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=5, width=14)
    button6.grid(row=3, column=2)

    button7 = tk.Button(window, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=5, width=14)
    button7.grid(row=4, column=0)

    button8 = tk.Button(window, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=5, width=14)
    button8.grid(row=4, column=1)

    button9 = tk.Button(window, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=5, width=14)
    button9.grid(row=4, column=2)

    button0 = tk.Button(window, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=5, width=14)
    button0.grid(row=5, column=0)

    plus = tk.Button(window, text=' + ', fg='black', bg='red',
                  command=lambda: addition(), height=5, width=14)
    plus.grid(row=2, column=3)

    minus = tk.Button(window, text=' - ', fg='black', bg='red',
                   command=lambda: subtraction(), height=5, width=14)
    minus.grid(row=3, column=3)

    multiply = tk.Button(window, text=' * ', fg='black', bg='red',
                      command=lambda: multiplication(), height=5, width=14)
    multiply.grid(row=4, column=3)

    divide = tk.Button(window, text=' / ', fg='black', bg='red',
                    command=lambda: division(), height=5, width=14)
    divide.grid(row=5, column=3)

    equal = tk.Button(window, text=' = ', fg='black', bg='red',
                    command=equal, height=5, width=14)
    equal.grid(row=5, column=2)

    clear = tk.Button(window, text='Clear', fg='black', bg='red',
                   command=clear, height=5, width=14)
    clear.grid(row=5, column='1')

    window.mainloop()