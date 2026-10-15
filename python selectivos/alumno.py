#Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente:
#si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, se le 
# hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 
#deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar 
#un alumno. 

promedio = float(input("Ingrese el promedio del alumno: "))
pension = int(input("Ingrese el valor de la pensión: "))
if promedio >= 4.0:
    descuento = pension * 0.30
    valor_a_pagar = pension - descuento
    print("Valor de la pensión: ", pension)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
else:
    iva = pension * 0.10
    valor_a_pagar = pension + iva
    print("Valor de la pensión: ", pension)
    print("Valor del IVA: ", iva)
    print("Valor a pagar: ", valor_a_pagar)