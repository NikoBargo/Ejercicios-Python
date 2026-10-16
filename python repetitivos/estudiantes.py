#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. Realizar un algoritmo para calcular el
#promedio  y la calificación más alta y  más baja de todo el grupo.

import random

alumnos = 20
suma = 0
notamax = 0    
notamin = 10   

for i in range(alumnos):
    numero = random.randint(0, 10)
    print(f"Alumno {i + 1}: {numero}")
    suma = suma + numero
    if numero > notamax:
        notamax = numero
    if numero < notamin:
        notamin = numero

promedio = suma / alumnos
print()

while True:
    print("===== MENÚ =====")
    print("1. Promedio")
    print("2. Calificacion alta")
    print("3. Calificacion baja")
    print("4. Salir")
    print("================")

    opcion = input("Elige una opción (1-4): ").strip()

    if opcion == "1":
        print(f">>> El promedio es: {promedio:.2f}\n")
    elif opcion == "2":
        print(f">>> La calificación más alta es: {notamax}\n")
    elif opcion == "3":
        print(f">>> La calificación más baja es: {notamin}\n")
    elif opcion == "4":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
