from tkinter import*
import math
from tkinter import messagebox

root = Tk()
blank_space = " "
root.title (50 * blank_space + "Cia")
root.resizable(width =FALSE, height = False,)

coverFrame = Frame (root, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame (coverFrame, pady=2, relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame (coverMainFrame, pady=2, relief=RIDGE)
MainFrame.grid()

class Calculator():
    def __init__(self):
        self.total = 0
        self.current =""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = entDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def display(self,value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)

# Operasi system tombol =
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(entDisplay.get())

# Operasi system tombol +, -, *, / dan juga (error handling)
    def valid_function(self):    
        try:
            if self.op == "add":
                self.total += self.current
            if self.op == "min":
                self.total -= self.current
            if self.op == "kali":
                self.total *= self.current
            if self.op == "dev":
                self.total /= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)
        except ZeroDivisionError:
            print("eror woii")

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

# Operasi system tombol BackSpace
    def backspace(self):
        numlen = len(entDisplay.get())
        entDisplay.delete(numlen - 1, 'end')
        if numlen == 1:
            entDisplay.insert(0, "0")

# Operasi system tombol Clear All C
    def Clear_Entry(self):
        self.result = False
        self.current ="0"
        self.display(0)
        self.input_value = True

# Operasi system tombol Clear All C
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0


    def button_click(self, number):
        current = self.result.get()
        self.result.delete(0, END)
        self.result.insert(0, str(current) + str(number))

    def mathsPM(self):
        self.result = False
        self.current = -(float(entDisplay.get()))
        self.display(self.current)

# Operasi system tombol √
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(entDisplay.get()))
        self.display(self.current)

added_value = Calculator()
entDisplay = Entry(MainFrame, font=('arial,', 18, 'bold'), width=26, justify=RIGHT)
entDisplay.grid(row =0, column=0, columnspan=4, pady=1)
entDisplay.insert(0, "0")

numpad = "789456123"
i = 0
btn =[]

# Membuat Tombol 1 - 9
for j in range(3,6):
    for k in range(3):
        btn.append(Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold',), text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] =lambda x=numpad[i]: added_value.numberEnter(x)
        i += 1

# Membuat Tombol Backspace
btnBackSpace=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="", bg="brown", command=added_value.backspace)
btnBackSpace.grid(row=1, column=0, pady=1)

# Membuat Tombol Clear All "C"
btnClear=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text=chr(67), bg="red", command=added_value.all_Clear_Entry)
btnClear.grid(row=1, column=1, pady=1)

# Membuat Tombol =
btnClear=Button(MainFrame, width=13, height=2, font=('arial,', 16, 'bold'), text="=", bg="pink", command=added_value.sum_of_total)
btnClear.grid(row=1, column=2, pady=1, columnspan=3)

# Membuat Tombol +
btnAdd=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="+", bg="pink", command=lambda:added_value.operation("add"))
btnAdd.grid(row=3, column=3, pady=1)

# Membuat Tombol -
btnMin=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="-", bg="pink", command=lambda:added_value.operation("min"))
btnMin.grid(row=4, column=3, pady=1)

# Membuat Tombol /
btnDiv=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text=chr(247), bg="pink", command=lambda:added_value.operation("dev"))
btnDiv.grid(row=5, column=3, pady=1)

# Membuat Tombol x
btnkali=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="x", bg="pink", command=lambda:added_value.operation("kali"))
btnkali.grid(row=6, column=3, pady=1)

# Membuat Tombol 0
btnNol=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="0", bg="lightgrey", command=lambda:added_value.numberEnter("0"))
btnNol.grid(row=6, column=1, pady=1)

# # Membuat Tombol ,
# btnKoma=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), bd=4, text=",", bg="lightgrey", command=lambda:added_value.numberEnter(","))
# btnKoma.grid(row=6, column=3, pady=1)

# Membuat Tombol .
btndot=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text=".", bg="pink", command=lambda:added_value.numberEnter("."))
btndot.grid(row=6, column=2, pady=1)

# Membuat Tombol √
btnAkar=Button(MainFrame, width=6, height=2, font=('arial,', 16, 'bold'), text="√", bg="pink", command=added_value.squared)
btnAkar.grid(row=6, column=0, pady=1)

root.mainloop()

