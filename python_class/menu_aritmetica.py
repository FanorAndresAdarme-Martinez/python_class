#declaracion de variables
#creado por: Fanor Andres Adarme M
#Fecha de creacion 22082018
import os
os.system("cls")
print("MENU PRINCIPAL")
print("1. Sumar numeros")
print("2. Restar numeros")
print("3. multiplicar numeros")
print("4. dividir numeros")
print(" :: digite una su opcion: ")
num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero: "))
opc = int(input("digite la operacion a realizar: "))
if opc == 1 :
	suma = num1 + num2
	print("la suma es: ",suma)
elif opc == 2 :
	resta = num1 - num2
	print("la resta es: ",resta)
elif opc == 3 :
	multiplicacion = num1 * num2
	print("la multiplicacion es: ",multiplicacion)
elif opc == 4 :
	divicion = num1 / num2
	print("la divicion es: ",divicion)
else : 
	print("ingrese una opcion valida")
