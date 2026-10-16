#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números. 
import random
numNeg = 0
suma = 0

while numNeg < 10:
    try:
        num = random.randint(-2, -1)
        if num < 0:
            numNeg += 1
            numPos = abs(num)
            suma = suma + numPos
        else:
            print("El número ingresado no es negativo. Por favor, ingrese un número negativo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

print ("la suma de los números convertidos a positivos es: ", suma)