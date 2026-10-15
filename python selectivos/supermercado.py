#En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento 
#dependiendo de un color  que se escoge al azar. Si el color de la balota es rojo  el 
#descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 
#20%. Si  el color es diferente a los indicados no obtendrá descuento.  Imprimir el valor de
# la compra, el color de la balota, el descuento y el valor a pagar. 

balota = input("Ingrese el color de la balota: ")
total_compra = int(input("Ingrese el valor total de la compra: "))
if balota == "rojo":
    descuento = total_compra * 0.15
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Color de la balota: ", balota)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
elif balota == "verde":
    descuento = total_compra * 0.20
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Color de la balota: ", balota)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
else:
    print("Color de la balota no válido")
    print("Valor de la compra: ", total_compra)
    print("Color de la balota: ", balota)
    print("Valor del descuento: 0")
    print("Valor a pagar: ", total_compra)