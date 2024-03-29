from tkinter import *
from tkinter import ttk

color1 = '#292828'
color2 = '#f2e9e9'
color3 = '#272a73'
color4 = '#dfdfed'
color5 = '#ff7700'

window =Tk()
window.title('Calculator')
window.geometry('235x314')
window.config(bg=color1)

frame_window = Frame(window, width=275, height=50, bg=color3)
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=275, height=260)
frame_body.grid(row=1, column=0)

all_values = ''

text_value = StringVar()

def enter_value(event):
    global all_values
    all_values = all_values + str(event)
    text_value.set(all_values)

def calculation():
    global all_values
    result = eval(all_values)
    global text_value
    text_value.set(result)
    all_values = str(result)

def clear_window():
    global all_values
    all_values =""
    text_value.set("")

app_label = Label(frame_window, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)

btnC = Button(frame_body, command=clear_window, text="C", width=12, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btnC.place(x=1, y=1)
btn_percent = Button(frame_body, command = lambda: enter_value('%'), text="%", width=4, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_percent.place(x=134, y=1)
btn_division = Button(frame_body, command = lambda: enter_value('/'), text="/", width=4, height=2, bg=color5, fg=color2, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_division.place(x=186, y=1)

btn7 = Button(frame_body, command = lambda: enter_value('7'), text='7', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn7.place(x=1, y=52)
btn8 = Button(frame_body, command = lambda: enter_value('8'), text='8', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=62, y=52)
btn9 = Button(frame_body, command = lambda: enter_value('9'), text='9', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn9.place(x=124, y=52)
btn_multiplication = Button(frame_body, command = lambda: enter_value('*'), text='*', width=4, height=2, bg=color5, fg=color2, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_multiplication.place(x=186, y=52)

btn4 = Button(frame_body, command = lambda: enter_value('4'), text='4', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=1, y=104)
btn5 = Button(frame_body, command = lambda: enter_value('5'), text='5', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn5.place(x=62, y=104)
btn6 = Button(frame_body, command = lambda: enter_value('6'), text='6', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=124, y=104)
btn_minus = Button(frame_body, command = lambda: enter_value('-'), text='-', width=4, height=2, bg=color5, fg=color2, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_minus.place(x=186, y=104)

btn1 = Button(frame_body, command = lambda: enter_value('1'), text='1', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn1.place(x=1, y=156)
btn2 = Button(frame_body, command = lambda: enter_value('2'), text='2', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn2.place(x=62, y=156)
btn3 = Button(frame_body, command = lambda: enter_value('3'), text='3', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn3.place(x=124, y=156)
btn_plus = Button(frame_body, command = lambda: enter_value('+'), text='+', width=4, height=2, bg=color5, fg=color2, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_plus.place(x=186, y=156)

btn0 = Button(frame_body, command = lambda: enter_value('0'), text='0', width=12, height=2, bg=color4, font=('Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
btn0.place(x=1, y=208)
btn_decimal = Button(frame_body, command = lambda: enter_value('.'), text='.', width=5, height=2, bg=color4, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_decimal.place(x=124, y=208)
btn_equal = Button(frame_body, command = calculation, text='=', width=4, height=2, bg=color5, fg=color2, font=('Helvetica 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_equal.place(x=186, y=208)

window.mainloop()
