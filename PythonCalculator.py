# Made By Syed Ali Zain Naqvi (syedalizain03@gmail.com) (@syedalizain033 FB/INSTA)
import tkinter #This library is used for making frames.
from tkinter import * #This is the 2nd important line to use tkinter
from tkinter import messagebox
# Global variables for val(value printed on calculator), A(int value to operate), oper(to check the operator either + or any other)
val = ""
A=0
oper=""
# Here are the functions called in buttons(+,-,x,/) with the keyword "command".
def clickPlus():
    global val
    global A
    global oper
    A=int (val)
    oper="+"
    val=val + "+"
    data.set(val) #Data is variable and setting a value for it
def clickMinus():
    global val
    global A
    global oper
    A=int (val)
    oper="-"
    val=val + "-"
    data.set(val)
def clickMulti():
    global val
    global A
    global oper
    A=int (val)
    oper="x"
    val=val + "x"
    data.set(val)
def clickDivide():
    global val
    global A
    global oper
    A=int (val)
    oper="/"
    val=val + "/"
    data.set(val)
def clickC():
    global A
    global val
    global oper
    A=0
    val=""
    data.set(val)    
def clickEqual():
    global A
    global val
    global oper
    val2 = val
    if oper=="+": # These if will check for the operator
# split function us used to split values. It splits value before + and after + and assigned to 2 indexes [0] and [1]
# as we used [1] so it gave us value after + as 1+2 so we will get 2
        number = int((val2.split("+")[1])) 
        C = A + number
        data.set(C)
        val=str(C)
    elif oper=="-":
        number = int((val2.split("-")[1]))
        C = A - number
        data.set(C)
        val=str(C)
    elif oper=="x":
        number = int((val2.split("x")[1]))
        C = A * number
        data.set(C)
        val=str(C)
    elif oper=="/":
        number = int((val2.split("/")[1]))
        if number==0:
            # Error message, already in tkinter but still need to import
            messagebox.showerror("Error", "Division By 0")
            data.set("Error")
            
        C = A / number
        data.set(round(C,6)) # round function to round value to 6 digits
        val=str(C)
#------------------------------------------------------- Operation Functions End
def click1():
    global val
    val = val + "1"
    data.set(val)
def click2():
    global val
    val = val + "2"
    data.set(val)
def click3():
    global val
    val = val + "3"
    data.set(val)
def click4():
    global val
    val = val + "4"
    data.set(val)
def click5():
    global val
    val = val + "5"
    data.set(val)
def click6():
    global val
    val = val + "6"
    data.set(val)
def click7():
    global val
    val = val + "7"
    data.set(val)
def click8():
    global val
    val = val + "8"
    data.set(val)
def click9():
    global val
    val = val + "9"
    data.set(val)
def click0():
    global val
    val = val + "0"
    data.set(val)
#----------------------------------------------------- Number Functions End
root = tkinter.Tk() #Making a Root Frame as the Main frame or we can say the overall body present at the back side
root.geometry("250x400+900+100")
root.resizable(0,0) #resize is disabled as bool values 0,0 are being sent.
root.title("Made by Ali")

data = StringVar() 
textLabel = Label(
    root,
    anchor=SE,
    bg="Black",
    fg="Green",
    font=("Bold", 25),
    textvariable = data,

)
textLabel.pack( # Pack is used for 
    expand=True, 
    fill="both",
)

row1 = Frame(root, bg = "white") # root as parameter because frame is on root window
row1.pack(expand = True, fill = "both")

row2 = Frame(root, bg = "black")
row2.pack(expand = True, fill = "both")

row3 = Frame(root, bg = "white")
row3.pack(expand = True, fill = "both")

row4 = Frame(root, bg = "black")
row4.pack(expand = True, fill = "both")

button1 = Button(
    row1, # row1 as parameter because values will be displayed in this row already present on root, so wont use root 
    bg="Grey",
    text = "1",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click1,  # command is telling the action aand click2 is the functions defined above.
)
button1.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button2 = Button(
    row1,
    bg="Grey",
    text = "2",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click2,
)
button2.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button3 = Button(
    row1,
    bg="Grey",
    text = "3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0, 
    command = click3,
)
button3.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

buttonPlus = Button(
    row1,
    bg="Grey",
    text = "+",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = clickPlus,
)
buttonPlus.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)



button4 = Button(
    row2,
    bg="Grey",
    text = "4",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click4,
)
button4.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button5 = Button(
    row2,
    bg="Grey",
    text = "5",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click5,
)
button5.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button6 = Button(
    row2,
    bg="Grey",
    text = "6",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click6
)
button6.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

buttonMinus = Button(
    row2,
    bg="Grey",
    text = "-",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = clickMinus,
)
buttonMinus.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)



button7 = Button(
    row3,
    bg="Grey",
    text = "7",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click7
)
button7.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button8 = Button(
    row3,
    bg="Grey",
    text = "8",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click8
)
button8.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button9 = Button(
    row3,
    bg="Grey",
    text = "9",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click9
)
button9.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

buttonMulti = Button(
    row3,
    bg="Grey",
    text = "x",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = clickMulti,
)
buttonMulti.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)




buttonC = Button(
    row4,
    bg="Grey",
    text = "c",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = clickC,
)
buttonC.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

button0 = Button(
    row4,
    bg="Grey",
    text = "0",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = click0,
)
button0.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

buttonEqual = Button(
    row4,
    bg="Grey",
    text = "=",
    font=("Verdana", 22), 
    relief=GROOVE,
    border=0,
    command = clickEqual,
)
buttonEqual.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)

buttonDivide = Button(
    row4,
    bg="Grey",
    text = "/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0, 
    command = clickDivide,
)
buttonDivide.pack( 
    side = "left", 
    expand=True, 
    fill="both"
)




root.mainloop() # necessary Line