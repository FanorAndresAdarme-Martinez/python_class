#CASH
import os
os.system("cls")
atras  = ('y')
i = 1
saldo = 1000000
while i <= 3:
    clave = int(input("ingrese clave de acceso: "))
    i = i + 1
    if clave == (147):
        print("clave acertada ")
        while atras == atras:
            print(".:MENÚ TRANSACCIONAL.:")
            print("1:Cambiar clave: ")
            print("2:Mostrar saldo: ")
            print("3:Realizar retiro: ")
            print("4:salir: ")
            opc = int(input(".:Digite opción: "))  
            if opc == 1:
                print("cambio de clave")
                clave = int(input("digite su nueva clave: "))
                if clave == (258):
                    print("su clave a sido cambiada: ")
                    exit()
            elif opc == 2:
                print("mostrar saldo: ")
                saldo == int(input("saldo actual: "))
                print("ok")
                atras = input("desea realizar otra opcion::")
                exit()
            elif opc == 3:
            	print("que valor decea retirar: ")
            	retiro = int(input("\n 10000   20000\n 50000  100000\n200000  400000\n600000 1000000\n digite la cantidad a retirar: "))
            	retiro = retiro - saldo
            	print("su retiro es: ",retiro)	
            elif opc == 4:
            	print("**********************salir*****************************")
            	exit()	
            else:
            	print("el monto a retirar supera el saldo:") 
    else:
        print("clave no valida")                
