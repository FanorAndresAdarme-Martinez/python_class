#operaciones_aritmeticas
import os
os.system("cls")
n1 = 0
n2 = 0
opc = 0
resultado = 0
print("OPERACIONES ARITMETICAS")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
print(".:menu de operaciones.:")
print("1.sumar numeros")
print("2.restar numeros")
print("3.multiplicar numeros")
print("4.dividir numeros")
opc = int(input("digite la operacion a realizar:"))
if opc == 1 :
	print("el resultado de la operacion es: ",num1 + num2)
elif opc == 2 :
	print("el resultado de la operacion es: ",num1 - num2)
elif opc == 3 :
	print("el resultado de la operacion es: ",num1 * num2)
elif opc == 4 :
	print("el resultado de la operacion es: ",num1 / num2)
else :
	print("Ha digitado una opcion incorrecta !!!")

	
	
	
	
  	


		
	
