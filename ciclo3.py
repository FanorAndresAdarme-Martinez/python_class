#TABLAS DE MULTIPLICAR ...
rango = 1
tabla_max = int(input("ingrese el numero de la tabla a realizar: "))
rango_max = int(input("ingrese el rango hasta donde desea desarrollar: "))
while rango <= rango_max :
	print (tabla_max, "*", rango, "=", tabla_max * rango)
	rango = rango + 1
