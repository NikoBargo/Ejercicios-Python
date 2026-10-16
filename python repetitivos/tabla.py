#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitará por teclado. 
# Imprimir el multiplicando, el multiplicador y el producto

numero = int(input("Ingrese un número para calcular su tabla de multiplicar: "))

for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")