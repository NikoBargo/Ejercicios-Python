#Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico
#determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en 
# la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es 
# menor que el rango que le corresponde, se determina su resultado como positivo y en caso 
# contrario como negativo. La tabla en la que el médico se basa para obtener el resultado es
#  la siguiente: 
# EDAD NIVEL HEMOGLOBINA
#  0 - 1 mes                     13 - 26 g% 
# > 1 y < = 6 meses       10 - 18 g% 
# > 6 y < = 12 meses     11 - 15 g% 
# > 1 y < = 5 años       11.5 - 15 g% 
# > 5 y < = 10 años     12.6 - 15.5 g% 
# > 10 y < = 15 años    13 - 15.5 g% 
# mujeres > 15 años    12 - 16 g% 
# hombres > 15 años   14 - 18 g% 

edad = int(input("Ingrese la edad de la persona en años: "))
genero = input("Ingrese el género de la persona: ")

if edad <= 1:
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 13:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")
if edad > 1 and edad <= 6:
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 10:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")
if edad > 6 and edad <= 12:
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 11:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")
if edad > 12 and edad <= 15:
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 13:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")
if edad > 15 and genero == "mujer":
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 12:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")
if edad > 15 and genero == "hombre":
    hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    if hemoglobina < 14:
        print("Resultado: Positivo (Anemia)")
    else:
        print("Resultado: Negativo (No Anemia)")