#AVERAGE2
p = int(input("cantidad de personas a ingresar: "))
if p > 0:
	edadMujeres = 0
	edadHombres = 0
	contadorMujeres = 0
	contadorHombres = 0
	for n in range (p):	
		edad = int(input ("ingrese la edad: "))
		genero = input("ingrese el genero de la persona (M) (F): ")
		if genero.upper() == 'M':
			edadHombres += edad
			contadorHombres += 1
		elif genero.upper() == 'F':
			edadMujeres += edad
			contadorMujeres += 1
		else:
			print ("el genero seleccionado no es correcto: ")	
	promedio_edadH = edadHombres / contadorHombres		
	promedio_edadM = edadMujeres / contadorMujeres
	print ("*****************************: ")
	print ("promedios de los datos recogidos: ")
	print ("*****************************: ")
	print ("1:promedio de todas las edades: ",(edadMujeres + edadHombres) / (contadorHombres + contadorMujeres))
	print ("2:numero total de mujeres: ",contadorMujeres)
	print ("3:numero total de hombres: ",contadorHombres)
	print ("4:promedio de edades de mujeres: ",promedio_edadM)
	print ("5:promedio de edades de hombres: ",promedio_edadH)
	print ("6:numero total de personas ingresadas al sistema: ",contadorHombres + contadorMujeres)
else:
	print ("incorrecto")
