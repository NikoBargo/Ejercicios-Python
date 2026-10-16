#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué,  cuantos entran con calcomanía
#  de cada color. Conociendo el ultimo dígito de la placa de cada carro, se puede determinar el color de la calcomanía utilizando
#  la siguiente relación:

import random


autos = int(input("Ingrese la cantidad de autos que entran a la ciudad: "))
cont_amarillo = 0
cont_rosa = 0
cont_rojo= 0
cont_verde = 0
cont_azul = 0


for i in range(autos):
    placa = random.randint(0, 9)

    if placa == 1 or placa == 2:
        cont_amarillo = cont_amarillo + 1
    elif placa == 3 or placa == 4:
        cont_rosa = cont_rosa + 1
    elif placa == 5 or placa == 6:
        cont_rojo = cont_rojo + 1
    elif placa == 7 or placa == 8:
        cont_verde = cont_verde + 1
    else:
        cont_azul = cont_azul + 1
    print (f"Auto {i + 1}: último dígito de la placa {placa}")

while True:
    print("===== MENÚ =====")
    print("1. Placas amarrillas")
    print("2. Placas rosas")
    print("3. Placas rojas")
    print("4. Placas verdes")
    print("5. Placas azules")
    print("6. Salir")
    print("================")

    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        print(f"Autos con calcomanía amarilla: {cont_amarillo}\n")
    elif opcion == "2":
        print(f"Autos con calcomanía rosa: {cont_rosa}\n")
    elif opcion == "3":
        print(f"Autos con calcomanía roja: {cont_rojo}\n")
    elif opcion == "4":
        print(f"Autos con calcomanía verde: {cont_verde}\n")
    elif opcion == "5":
        print(f"Autos con calcomanía azul: {cont_azul}\n")
    elif opcion == "6":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        continue