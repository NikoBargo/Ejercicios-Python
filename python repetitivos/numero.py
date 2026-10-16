#Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos neutros. 
import random
num = 0
pos = 0
neg = 0
neut = 0

while num < 20:
    try:
        numero = random.randint(-10, 10)
        print(f"Número generado: {numero}")
       
        if numero > 0:
            pos += 1
        elif numero < 0:
            neg += 1
        else:
            neut += 1
        num += 1
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

print(f"Cantidad de números positivos: {pos}")
print(f"Cantidad de números negativos: {neg}")
print(f"Cantidad de números neutros: {neut}")
    