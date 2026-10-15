#Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas
#se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas
#un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y 
#el valor a pagar una vez aplicado el descuento. 

cantidad_zap = int (input("Ingrese la cantidad de zapatillas a comprar: "))
if cantidad_zap >= 3:
    precio_unitario = int(input("Ingrese el precio unitario de las zapatillas: "))
    total_compra = cantidad_zap * precio_unitario
    descuento = total_compra * 0.20
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
else:
    precio_unitario = int(input("Ingrese el precio unitario de las zapatillas: "))
    total_compra = cantidad_zap * precio_unitario
    descuento = total_compra * 0.10
    valor_a_pagar = total_compra - descuento
    print("Valor de la compra: ", total_compra)
    print("Valor del descuento: ", descuento)
    print("Valor a pagar: ", valor_a_pagar)
