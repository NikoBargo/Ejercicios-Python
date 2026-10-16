# Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.  

import random


hombres = 0
edades_hombres = 0
mujeres = 0
edades_mujeres = 0
todos = int(input("Ingrese la cantidad total de alumnos: "))

for i in range(todos):
    genero = random.randint(1, 2)
    edad = random.randint(15, 18)

    if genero == 1:
        hombres += 1
        edades_hombres += edad
    else:
        mujeres += 1
        edades_mujeres += edad

    print(f"Persona {i + 1}: edad {edad} años, genero {'masculino' if genero == 1 else 'femenino'}")


while True:
    print("===== MENÚ =====")
    print("1.promedio de edades de hombres")
    print("2. promedio de edades de mujeres")
    print("3. Promedio de edades de todo el grupo")
    print("4. Salir")
    print("================")

    opcion = input("Elige una opción (1-4): ").strip()

    if opcion == "1":
            promedio_hombres = edades_hombres / hombres
            print(f"El promedio de edades de los hombres es: {promedio_hombres} años")
    else:
            print("No hay hombres en el grupo.")

    if opcion == "2":
            promedio_mujeres = edades_mujeres / mujeres
            print(f"El promedio de edades de las mujeres es: {promedio_mujeres} años")
    else:
            print("No hay mujeres en el grupo.")

    if opcion == "3":
        total_alumnos = hombres + mujeres
        promedio_total = (edades_hombres + edades_mujeres) / total_alumnos
        print(f"El promedio de edades de todo el grupo es: {promedio_total} años")

    elif opcion == "4":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")