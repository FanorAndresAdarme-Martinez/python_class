#calculadora_avanzada
def menu():
	print(".:.MENU.:.")
	print("1.Sumar: ")
	print("2.Restar: ")
	print("3.multiplicar: ")
	print("4.dividir: ")
	print("5.raiz cuadrada: ")
def datos():
	global n1 , n2
	n1 = int(input("ingrese primer numero: "))
	n2 = int(input("ingrese segundo numero: "))
def operaciones():
	if opc == 1 :
		print("el resultado de la operacion es: ",n1 + n2)
	elif opc == 2 :
		print("el resultado de la operacion es: ",n1 - n2)
	elif opc == 3 :
		print("el resultado de la operacion es: ",n1 * n2)
	elif opc == 4 :
		print("el resultado de la operacion es: ",n1 / n2)
	elif opc == 5 :
		print("el resultado de la operacion es: ",n1 ** n2)

datos()
menu()
opc = int(input("digite una opcion: "))
operaciones()


#funcion para operaciones aritmrticas
print("******************************")
def suma():
	suma = a + b
	print("la suma es: ",suma)
def resta():
	res = a - b
	return res 
a = int(input("digite n1: "))
b = int(input("digite n2: "))
suma()
print("la resta es: ",resta())