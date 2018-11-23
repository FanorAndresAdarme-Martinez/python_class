#simulador
porc_interes = 1.2;
elif opc == 2:
porc_interes = 1.3;
elif opc == 3:
porc_interes = 1.4;
print "| Monto solicitado ($): ", valor
print "| Total intereses ($): ", interes * cuotas
#SIMULADOR DE CREDITO

cuota_sin_int = round(valor / cuotas,2)
interes = round((valor * porc_interes)/100,2)
cuota_a_pagar = cuota_sin_int + interes
print "\n______________________________________________________________________"
print "| TABLA DE AMORTIZACION"
print "______________________________________________________________________"
print "|Nro. cuota | Vr. cuota sin interes | Interes | Cuota a pagar |"
print "______________________________________________________________________"
while i <= cuotas :
print "|",i," ",cuota_sin_int," ",interes," ",cuota_a_pagar
total_credito = round(total_credito + cuota_a_pagar,2)
i = i + 1
print "______________________________________________________________________"
print "| Edad: ", age
print "| Tasa de interes: ", porc_interes
print "| Total credito ($): ", total_credito
print "| Probabilidad de prestamo: ", probabilidad
print "______________________________________________________________________"