import serial
from tkinter import *

import tkinter

arduinoData = serial.Serial ('COM3',9600)

def onOff(valor):
    arduinoData.write(valor)

led_control_window = Tk()
#Button = TKinter.Button
btn1 = Button(led_control_window, text="ON", command=lambda:onOff(0))
btn2 = Button(led_control_window, text="OFF", command=lambda:onOff(1))
btn3 = Button(led_control_window, text="ON", command=lambda:onOff(2))
btn4 = Button(led_control_window, text="OFF", command=lambda:onOff(3))
btn4 = Button(led_control_window, text="ON", command=lambda:onOff(4))
btn6 = Button(led_control_window, text="OFF", command=lambda:onOff(5))
btn7 = Button(led_control_window, text="ON", command=lambda:onOff(6))
btn8 = Button(led_control_window, text="OFF", command=lambda:onOff(7))

btn1.grid(row=0,column=1)
btn2.grid(row=1,column=1)
btn1.grid(row=2,column=3)
btn2.grid(row=3,column=3)
btn1.grid(row=4,column=5)
btn2.grid(row=5,column=5)
btn1.grid(row=6,column=7)
btn2.grid(row=7,column=7)

led_control_window.mainloop()

    
