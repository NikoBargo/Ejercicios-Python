#Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de 
#ejercicio aeróbico; la fórmula que se aplica es: 
#cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10
# y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 

genero = input("Ingrese su género (femenino/masculino): ")
edad = int(input("Ingrese su edad: "))

if genero == "femenino":
    pulsaciones = (220 - edad) / 10
    print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)
elif genero == "masculino":
    pulsaciones = (210 - edad) / 10
    print("El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)
else:
    print("Género no válido")