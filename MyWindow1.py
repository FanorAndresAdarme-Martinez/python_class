#IMPORTAR LIBRERIAS PARA GUI

from tkinter import *
import tkinter

############################
#Crear ventana
root = tkinter.Tk()
root.geometry("400x400")#W*H o ALT*ANCH

root.title("Mi calculadora")
root.resizable(FALSE, FALSE)
root.configure(background="#111EEB")

############################
def btnClik(valor):
    global operador
    operador=operador+str(valor)
    input_text.set(operador)
def clear():
    global operador
    operador=("")
    input_text.set(operador)
def operacion():
    global operador
    try:
        opera=str(eval(operador))#sirve para realizar la operacion
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#muestra el resultado
#############################
input_text=StringVar()
operador=""

    
Display=Entry(root,font=('arial',20,'bold'),width=25,bd=2,insertwidth=10,bg="#D8D8D8",justify="center",textvariable=input_text).place(x=10,y=20)

Boton1=Button(root,text="1",width=5,height=2,command=lambda:btnClik(1)).place(x=10,y=75)
Boton2=Button(root,text="2",width=5,height=2,command=lambda:btnClik(2)).place(x=70,y=75)
Boton3=Button(root,text="3",width=5,height=2,command=lambda:btnClik(3)).place(x=130,y=75)
Boton4=Button(root,text="4",width=5,height=2,command=lambda:btnClik(4)).place(x=10,y=140)
Boton5=Button(root,text="5",width=5,height=2,command=lambda:btnClik(5)).place(x=70,y=140)
Boton6=Button(root,text="6",width=5,height=2,command=lambda:btnClik(6)).place(x=130,y=140)
Boton7=Button(root,text="7",width=5,height=2,command=lambda:btnClik(7)).place(x=10,y=210)
Boton8=Button(root,text="8",width=5,height=2,command=lambda:btnClik(8)).place(x=70,y=210)
Boton9=Button(root,text="9",width=5,height=2,command=lambda:btnClik(9)).place(x=130,y=210)
Boton0=Button(root,text="0",width=5,height=2,command=lambda:btnClik(0)).place(x=70,y=280)
Boton10=Button(root,text="+",width=5,height=2,command=lambda:btnClik('+')).place(x=220,y=140)
Boton11=Button(root,text="-",width=5,height=2,command=lambda:btnClik('-')).place(x=220,y=75)
Boton12=Button(root,text="/",width=5,height=2,command=lambda:btnClik('/')).place(x=220,y=210)
Boton13=Button(root,text="*",width=5,height=2,command=lambda:btnClik('*')).place(x=220,y=280)
Boton14=Button(root,text="^",width=10,height=2,command=lambda:btnClik('**')).place(x=310,y=75)
Boton15=Button(root,text="=",width=5,height=2,command=operacion).place(x=130,y=280)
Botonc=Button(root,text="CLS",width=5,height=2,command=clear).place(x=10,y=280)



#Abrir ventana
root.mainloop()
