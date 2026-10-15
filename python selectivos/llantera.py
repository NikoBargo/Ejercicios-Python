#En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”, dicha 
#promoción consiste en lo siguiente: 
#Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se 
#compran de cinco a 10 y de $200.000 si se compran más de 10. Obtener la cantidad de dinero 
# que una persona tiene que pagar por cada una de las llantas que compre.

cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))
if cantidad_llantas < 5:
    precio_unitario = 300000
    valor_a_pagar = cantidad_llantas * precio_unitario
    print("Valor a pagar por cada llanta: ", precio_unitario)
    print("Valor total a pagar: ", valor_a_pagar)
elif 5 <= cantidad_llantas <= 10:
    precio_unitario = 250000
    valor_a_pagar = cantidad_llantas * precio_unitario
    print("Valor a pagar por cada llanta: ", precio_unitario)
    print("Valor total a pagar: ", valor_a_pagar)
else:
    precio_unitario = 200000
    valor_a_pagar = cantidad_llantas * precio_unitario
    print("Valor a pagar por cada llanta: ", precio_unitario)
    print("Valor total a pagar: ", valor_a_pagar)