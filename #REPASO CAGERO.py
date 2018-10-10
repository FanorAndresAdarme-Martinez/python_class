#REPASO CAGERO
opc = 0
intentos = 3
clave = 0
saldo = 800000
monto = 0
for n in range(intentos):
	clave = int(input("ingresar clave: : "))
	if clave == (147):
		print("clave correcta::")
		print("************")
		print(".:MENU TRANSACCIONAL:.")
		print("1:Cambiar clave: ")
		print("2:Mostrar saldo: ")
		print("3:Realizar retiro: ")
		print("4:Salir: ")
		opc = int(input(".:Digite una opcion:."))
		if opc == 1:
			print("cambio de clave::")
			clave = int(input("ingrese su clave nueva::."))
			if clave == (123):
				print("cambio de clave exitoso:")
				break
		elif opc == 2:
			print("::mostrar saldo::")
			clave = int(input("digite su clave de acceso: "))
			saldo = 800000
			print("::su saldo es::",saldo)	
		elif opc == 3:
			print("::::submenu::::")
			print("1:10.000")
			print("2:20.000")
			print("3:50.000")
			print("4:100.000") 
			print("5:200.000")
			print("6:400.000")
			print("7:600.000")
			print("8:1.000.000")
			monto = int(input("digite la opcion deseada:: "))
			while monto >= 8:
				monto = monto - 1
				monto = input("el monto a retirar supera el saldo")
				exit()
			if monto == 1:
				print("acaba de retirar 10.000")
				retiro = 10000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 2:
				print("acaba de retirar 20.000")
				retiro = 20000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 3:
				print("acaba de retirar 50.000")
				retiro = 50000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 4:
				print("acaba de retirar 100.000")
				retiro = 100000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 5:
				print("acaba de retirar 200.000")
				retiro = 200000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 6:
				print("acaba de retirar 400.000")
				retiro = 400000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 7:
				print("acaba de retirar 600.000")
				retiro = 600000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			elif monto == 8:
				print("acaba de retirar 1.000.000")
				retiro = 1000000
				saldo = saldo - retiro
				print("su retiro fue exitoso")
				print("saldo actual es de: ",saldo)
				break
			else:
				print("::fondos insuficientes en la cuenta::")	
		elif opc == 4:
			print("*****salir*****")
			salir = input("::precione enter para salir::")
			break	
	else:
		print("****clave no valida*****")