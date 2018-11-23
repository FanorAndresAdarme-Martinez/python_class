#LOGIN.PY
from tkinter import *
def menuWindow():
    ventana2=Tk()
    ventana2.title("menu de control")
    ventana2.geometry("400x200")
    
ventana_login=Tk()
ventana_login.title("login")
ventana_login.geometry("300x400")
ventana_login.resizable(FALSE, FALSE)
ventana_login.configure(background="SkyBlue4")
color_boton=("gray77")

Boton_Acceso = Button(ventana_login, text = "ingresar", width = 10 , height = 5, command = menuWindow).place(x=50,y=50)

ventana_login.mainloop()
