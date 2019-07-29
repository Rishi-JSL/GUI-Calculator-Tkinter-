from tkinter import *
root = Tk()

equa=""

equation = StringVar()

calculation = Label(root, textvariable = equation)

calculation.grid(columnspan =4)

equation.set("Enter Your Equation")


def btnpress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def equalpress():
    global equa
    result = str(eval(equa))
    equation.set(result)
    equa=""

def clearpress():
    global equa
    equa = ""
    equation.set("Enter Your Equation")


but1 = Button(text = "     1     ", command = lambda:btnpress(1))
but1.grid(row = 1 , column = 0)

but2 = Button(text = "     2     ", command = lambda:btnpress(2))
but2.grid(row = 1 , column = 1)

but3 = Button(text = "     3     ", command = lambda:btnpress(3))
but3.grid(row = 1 , column = 2)

but4 = Button(text = "     4     ", command = lambda:btnpress(4))
but4.grid(row = 2 , column = 0)

but5 = Button(text = "     5     ", command = lambda:btnpress(5))
but5.grid(row = 2 , column = 1)

but6 = Button(text = "     6     ", command = lambda:btnpress(6))
but6.grid(row = 2 , column = 2)

but7 = Button(text = "     7     ", command = lambda:btnpress(7))
but7.grid(row = 3 , column = 0)

but8 = Button(text = "     8     ", command = lambda:btnpress(8))
but8.grid(row = 3 , column = 1)

but9 = Button(text = "     9     ", command = lambda:btnpress(9))
but9.grid(row = 3 , column = 2)

but0 = Button(text = "     0     ", command = lambda:btnpress(0))
but0.grid(row = 4 , column = 1)

butadd = Button(text = "     +    ", command = lambda:btnpress('+'))
butadd.grid(row = 1 , column = 3)

butsub = Button(text = "     -     ", command = lambda:btnpress('-'))
butsub.grid(row = 2 , column = 3)

butmul = Button(text = "     *     ", command = lambda:btnpress('*'))
butmul.grid(row = 3 , column = 3)

butdiv = Button(text = "     /     ", command = lambda:btnpress('/'))
butdiv.grid(row = 4 , column = 3)

equal = Button(text = "     =     ",command = equalpress)
equal.grid(row =4 , column = 2)

clear = Button(text = "     C     ",command = clearpress)
clear.grid(row = 4 , column = 0 )



root.mainloop()