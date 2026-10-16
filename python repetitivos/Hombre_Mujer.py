#Calcular la cantidad de hombres y mujeres presentes
#en un salón de clases con un total de n personas. 

personas = int(input("Ingrese la cantidad total de personas en el salón: "))

hombres = 0
mujeres = 0

for i in range(personas):
    genero = input(f"Ingrese el género de la persona {i + 1} (hombre=1 , mujer=2): ").strip().lower()
    
    if genero == "1":
        hombres += 1
    elif genero == "2":
        mujeres += 1
    else:
        print("Género no válido. Por favor ingrese '1' o '2'.")

while True:
    print("===== MENÚ =====")
    print("1. cantidad de hombres")
    print("2. cantidad de mujeres")
    print("3. Salir")
    print("================")

    opcion = input("Elige una opción (1-3): ").strip()

    if opcion == "1":
        print(f"La cantidad de hombres es: {hombres}")
    elif opcion == "2":
        print(f"La cantidad de mujeres es: {mujeres}")
    elif opcion == "3":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")