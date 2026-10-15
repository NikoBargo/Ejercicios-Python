#En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento 
#dependiendo de un color  que se escoge al azar. Si el color de la balota es rojo  el 
#descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 
#20%. Si  el color es diferente a los indicados no obtendrá descuento.  Imprimir el valor de
# la compra, el color de la balota, el descuento y el valor a pagar. 

#modificaciones: se tiene la oportunidad de sacar dos balotas para tener un descuento 
# acumulado por lo tanto si se sacan dos rojas se tendran un descuento de 30% y si se sacan 
# dos verdes un descuento de 40% y si se saca una roja y una verde un descuento de 35% y 
# si se saca una balota diferente a las indicadas no obtendra descuento.

balota1 = input("Ingrese el color de la primera balota: ")
balota2 = input("Ingrese el color de la segunda balota: ")
total_compra = int(input("Ingrese el valor total de la compra: "))

if balota1 == "rojo" and balota2 == "rojo":
    descuento = total_compra * 0.30
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Color de la primera balota: ", balota1)
    print("Color de la segunda balota: ", balota2)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
    
elif balota1 == "verde" and balota2 == "verde":
    descuento = total_compra * 0.40
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Color de la primera balota: ", balota1)
    print("Color de la segunda balota: ", balota2)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
elif (balota1 == "rojo" and balota2 == "verde") or (balota1 == "verde" and balota2 == "rojo"):
    descuento = total_compra * 0.35
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Color de la primera balota: ", balota1)
    print("Color de la segunda balota: ", balota2)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
else:
    print("Color de la balota no válido")
    print("Valor de la compra: ", total_compra)
    print("Color de la primera balota: ", balota1)
    print("Color de la segunda balota: ", balota2)
    print("Valor del descuento: 0")
    print("Valor a pagar: ", total_compra)