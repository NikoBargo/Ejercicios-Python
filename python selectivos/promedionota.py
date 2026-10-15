# Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobará si su
# promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario. 

nota1 = int(input("Ingrese la primera calificación: "))
nota2 = int(input("Ingrese la segunda calificación: "))   
nota3 = int(input("Ingrese la tercera calificación: "))

promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 70:
    print("El aprendiz aprueba Algoritmia con un promedio de:", promedio)
else:
    print("El aprendiz reprueba Algoritmia con un promedio de:", promedio)