#repaso pro
p = int(input("cantidad de personas a ingresar:: "))
if p > 0:
	edadMujeres = 0
	edadHombres = 0
	contadorMujeres = 0
	contadorHombres = 0
	for n in range (p):
		genero = input("ingrese el genero deseado (m) (f) : ")
		edad = int(input("ingrese la edad:: "))
		if genero == 'm':
			edadHombres += edad
			contadorHombres += 1
		elif genero == 'f':
			edadMujeres += edad
			contadorMujeres += 1
		else:
			print("el genero selecionado no es correcto: ")
	promedio_edadH = edadHombres / contadorHombres
	promedio_edadM = edadMujeres / contadorMujeres
	print("**************")
	print("promedio de todas las edades: ",(edadHombres + edadMujeres)/(contadorHombres + contadorMujeres))
	print("numero total de mujeres: ",contadorMujeres)
	print("numero total de hombres: ",contadorHombres)
	print("promedio de edades de las mujeres: ",promedio_edadM)
	print("proedio de edades de los hombres: ",promedio_edadH)
	print("numero total de personas ingresadas al sistema: ",contadorHombres + contadorMujeres)
else:
	print("incorrecto")	