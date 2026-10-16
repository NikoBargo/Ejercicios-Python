'''
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa se deberá mostrar la cantidad de hombres, 
la cantidad de mujeres, la altura promedio ,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos 
que tiene una altura  menor o igual a 1.50 cm. El programa debe finalizar cuando la edad sea igual a 0. 
'''

hombres = 0
edades_hombres = 0
mujeres = 0
edades_mujeres = 0
altura_total = 0
suma_altura = 0
alumnos_altura_mayor_170 = 0
alumnos_altura_menor_150 = 0

while True:
    try:
          alumno = input("Ingrese el sexo del alumno :").lower()
          if alumno == "hombre":
              hombres += 1
          else:
              mujeres += 1
          edad = int(input("Ingrese la edad del alumno :"))
          altura = int(input("Ingrese la altura del alumno :"))
          suma_altura = suma_altura + altura
          if altura > 170:
              alumnos_altura_mayor_170 += 1
          else:
              alumnos_altura_menor_150 += 1
    except ValueError:
        print("Por favor, ingrese valores válidos.")
        continue

    if edad == 0:
        break


while True:
    print("===== MENÚ =====")
    print("1.cantidad de hombres")
    print("2. cantidad de mujeres")
    print("3. Altura promedio")
    print("4. cantidad de alumnos que tienen una altura mayor a 1.70 cm")
    print("5. cantidad de alumnos que tiene una altura  menor o igual a 1.50 cm")
    print("6. Salir")
    print("================")

    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
            print(f"La cantidad de hombres es: {hombres}")
    else:
            print("No hay hombres en el grupo.")

    if opcion == "2":
            print(f"La cantidad de mujeres es: {mujeres}")
    else:
            print("No hay mujeres en el grupo.")

    if opcion == "3":
        suma_altura / (hombres + mujeres)
        print(f"La altura promedio es: {suma_altura / (hombres + mujeres)} cm")

    elif opcion == "4":
        print(f"La cantidad de alumnos con altura mayor a 1.70 cm es: {alumnos_altura_mayor_170}")
    elif opcion == "5":
        print(f"La cantidad de alumnos con altura menor o igual a 1.50 cm es: {alumnos_altura_menor_150}")
    elif opcion == "6":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")