'''
Un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un algoritmo que lea por cada estudiante la calificación 
obtenida. Al finalizar calcule e imprima: 
• La cantidad de estudiantes que obtuvieron una calificación menor a 50.  
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70. 
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.  
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más. 
'''

import random


estudiantes = 23
calif50 = 0
calif70 = 0
calif80 = 0
califMas80 = 0


contados = 0   
intentos = 0  


while contados < estudiantes:
    intentos = intentos + 1
    calificacion = random.randint(-10, 100)

    if calificacion < 0:
        print(f"Lectura {intentos}: calificación {calificacion} no válida")
        continue

    contados = contados + 1

    if calificacion < 50:
        calif50 = calif50 + 1
    elif calificacion >= 50 and calificacion < 70:
        calif70 = calif70 + 1
    elif calificacion >= 70 and calificacion < 80:
        calif80 = calif80 + 1
    else:
        califMas80 = califMas80 + 1
    print(f"Estudiante {contados}: calificación {calificacion}")

print(f"\nSe hicieron {intentos} lecturas para obtener {contados} calificaciones válidas.\n")


while True:
    print("===== MENÚ =====")
    print("1. Estudiantes con calificación menor a 50")
    print("2. Estudiantes con calificación de 50 o más pero menor que 70")
    print("3. Estudiantes con calificación de 70 o más pero menor que 80")
    print("4. Estudiantes con calificación de 80 o más")
    print("5. Salir")
    print("================")

    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "1":
        print(f"Estudiantes con calificación menor a 50: {calif50}\n")
    elif opcion == "2":
        print(f"Estudiantes con calificación de 50 o más pero menor que 70: {calif70}\n")
    elif opcion == "3":
        print(f"Estudiantes con calificación de 70 o más pero menor que 80: {calif80}\n")
    elif opcion == "4":
        print(f"Estudiantes con calificación de 80 o más: {califMas80}\n")
    elif opcion == "5":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        continue