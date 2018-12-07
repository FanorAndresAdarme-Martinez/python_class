import serial
from tkinter import*
import tkinter

arduinoData = serial.Serial ('COM7',9600)

#CREAR VENTANA
ventana= Tk()
ventana.title("CasaDomotica")
ventana.geometry("300x400")
ventana.resizable(FALSE, FALSE)
ventana.configure(background="#111EEB")
color_boton=("gray77")

def on_off(valor):
        valor= str(valor)
        #arduinoData.write(b'valor')
        arduinoData.write(str.encode(valor))
        
def leds():
        global leds
        led=Tk()
        led.title("menu leds")
        led.geometry("400x200")
        led.resizable(FALSE, FALSE)
        led.configure (background="#111EEB")
        led_Disco1 = Button(led, text="Disco1",width = 10, height = 2, command= lambda :on_off('1')).place (x=10, y=40)
        led_Disco2 = Button(led, text="Disco2",width = 10, height = 2, command= lambda :on_off('2')).place (x=110, y=40)
        led_Gradas = Button(led, text="Gradas",width = 10 , height = 2, command=lambda :on_off('4')).place (x=310, y=40)
        led_Sala = Button(led, text="Sala",width= 10 , height = 2, command=lambda :on_off('5')).place (x=170, y=120)
	        
def todo():
        global todo
        todo=Tk()
        todo.title("on_off_Todo")
        todo.geometry("200x200")
        todo.resizable(FALSE, FALSE)
        todo.configure (background="#111EEB")
        todo = Button(todo, text="on_off_Todo",width = 15, height = 2,command= lambda :on_off('6')).place (x=10, y=60)

def servo():
        global servo
        servoM=Tk()
        servoM.title("Abrir/Cerrar")
        servoM.geometry("200x200")
        servoM.resizable(FALSE, FALSE)
        servoM.configure (background="#111EEB")
        PuertaDisco = Button(servoM, text="Abrir P/Cerrar P",width=15 ,height =2 ,command = lambda:on_off('7')).place (x=10, y=60)

#***************************#
	
Boton_leds = Button(ventana, text = "Encender Leds ", width = 30 , height = 3, command = leds).place(x=50,y=50)
Boton_todo = Button(ventana, text = "on_off_leds", width = 30 , height = 3, command = todo).place(x=50,y=150)
Boton_Acceso = Button(ventana, text = "servoM", width = 30 , height = 3, command = servo).place(x=50,y=260)

#ABRIR VENTANA PARA EL PROGRAMA
ventana.mainloop()
arduinoData.close()
