# ======================= Imports ====================== 

from tkinter import *
from tkinter import ttk

# ==================== GUI Creation ====================

cal = Tk()
cal.geometry("440x550")
cal.config(bg ="DarkOliveGreen3")
cal.title("Calculator")
cal.resizable(0,0)

# ======================= Label ========================

L1= Label(cal,text ="Simple Math Calculator",font = ("Bradley Hand ITC",25))
L1.config(bg = "DarkOliveGreen3")
L1.place(x = 55, y = 5)

# ====================== Main Code =====================

expression = "" 
def press(num): 
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress(): 
    try: 
        global expression
        total = str(eval(expression)) 
        equation.set(total)
        expression = "" 
    except:
        equation.set(" Error ") 
        expression = ""

def clear(): 
    global expression 
    expression = "" 
    equation.set("")

equation = StringVar() 

# ====================== Entry Box ======================

expression_field = Entry(cal, textvariable=equation, font =("Baskerville Old Face",20))
expression_field.place(x = 15, y =60, width = '308', height = '58')

# ======================= Buttons =======================

button1 = Button(cal, text=' 1 ', font =("Baskerville Old Face",32), fg='black', bg='cyan',command=lambda: press(1), height= 1, width=3) 
button1.place(x=15, y=140) 
 
button2 = Button(cal, text=' 2 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(2), height = 1, width = 3) 
button2.place(x=120, y=140) 
 
button3 = Button(cal, text=' 3 ', font =("Baskerville Old Face",32), fg='black', bg='cyan',command=lambda: press(3), height = 1, width = 3) 
button3.place(x=225, y=140) 
 
button4 = Button(cal, text=' 4 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(4), height = 1, width = 3) 
button4.place(x=15, y= 240) 
 
button5 = Button(cal, text=' 5 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(5), height = 1, width = 3) 
button5.place(x=120, y=240) 
 
button6 = Button(cal, text=' 6 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(6), height = 1, width = 3) 
button6.place(x=225, y=240) 
 
button7 = Button(cal, text=' 7 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(7), height = 1, width = 3) 
button7.place(x=15, y=340) 
 
button8 = Button(cal, text=' 8 ', font =("Baskerville Old Face",32), fg='black', bg='cyan',command=lambda: press(8), height = 1, width = 3) 
button8.place(x=120, y=340) 
 
button9 = Button(cal, text=' 9 ', font =("Baskerville Old Face",32), fg='black', bg='cyan', command=lambda: press(9), height = 1, width = 3) 
button9.place(x=225, y=340) 
 
button0 = Button(cal, text=' 0 ', font =("Baskerville Old Face",32), fg='black', bg='cyan',command=lambda: press(0), height = 1, width = 3) 
button0.place(x=120, y=440) 
 
plus = Button(cal, text=' + ', font =("Baskerville Old Face",32), fg='black', bg='magenta4',command=lambda: press("+"), height = 1, width = 3) 
plus.place(x=330, y=140) 
 
minus = Button(cal, text=' - ', font =("Baskerville Old Face",32), fg='black', bg='magenta4',command=lambda: press("-"), height = 1, width = 3) 
minus.place(x=330, y=240) 
 
multiply = Button(cal, text=' x ', font =("Baskerville Old Face",32), fg='black', bg='magenta4',command=lambda: press("*"), height = 1, width = 3) 
multiply.place(x=330, y=340) 
 
divide = Button(cal, text=' / ', font =("Baskerville Old Face",32), fg='black', bg='magenta4',command=lambda: press("/"), height = 1, width = 3) 
divide.place(x=330, y=440) 
 
equal = Button(cal, text=' = ', font =("Baskerville Old Face",32), fg='black', bg='sienna2', command=equalpress, height = 1, width = 3) 
equal.place(x=225, y=440) 
 
del_clear = Button(cal, text='Clear', font =("Bodoni MT",21), fg='black', bg='red',command=clear, height = 1, width = 4) 
del_clear.place(x=333, y=60) 
 
Decimal= Button(cal, text='.', font =("Baskerville Old Face",32), fg='black', bg='magenta4',command=lambda: press('.'), height = 1, width = 3) 
Decimal.place(x=15, y=440)

# ==============================================================

cal.mainloop()

# ======================= End of Program =======================