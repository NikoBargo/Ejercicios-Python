#Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jóvenes, adultos
# y ancianos  que existen en su zona.

import random

personas = 5

suma_niños = 0
cont_niños = 0
suma_jovenes = 0
cont_jovenes = 0
suma_adultos = 0
cont_adultos = 0
suma_ancianos = 0
cont_ancianos = 0

for i in range(personas):
    edad = random.randint(0, 90)

    if edad <= 12:
        peso = random.randint(10, 40)
        suma_niños = suma_niños + peso
        cont_niños = cont_niños + 1
    elif edad <= 29:
        peso = random.randint(45, 85)
        suma_jovenes = suma_jovenes + peso
        cont_jovenes = cont_jovenes + 1
    elif edad <= 59:
        peso = random.randint(55, 95)
        suma_adultos = suma_adultos + peso
        cont_adultos = cont_adultos + 1
    else:
        peso = random.randint(50, 85)
        suma_ancianos = suma_ancianos + peso
        cont_ancianos = cont_ancianos + 1

    print(f"Persona {i + 1}: edad {edad} años, peso {peso} kg")

print()

while True:
    print("===== MENÚ =====")
    print("1. Promedio niños (0-12)")
    print("2. Promedio jóvenes (13-29)")
    print("3. Promedio adultos (30-59)")
    print("4. Promedio ancianos (60+)")
    print("5. Salir")
    print("================")

    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "1":
        suma, cont, grupo = suma_niños, cont_niños, "niños"
    elif opcion == "2":
        suma, cont, grupo = suma_jovenes, cont_jovenes, "jóvenes"
    elif opcion == "3":
        suma, cont, grupo = suma_adultos, cont_adultos, "adultos"
    elif opcion == "4":
        suma, cont, grupo = suma_ancianos, cont_ancianos, "ancianos"
    elif opcion == "5":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        continue
    if cont == 0:
        print(f">>> No hay {grupo} en el muestreo.\n")
