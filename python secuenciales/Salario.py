nombre = input("Ingrese su nombre: ")
mensual= float(input("Ingrese su pago mensual: "))
salario = mensual / 30
horas = float(input("Ingrese la cantidad de horas trabajadas al dia: "))
print ("El empleado:", nombre, "tiene un salario por dia de: ", round(salario, 2), "y un salario por hora de: ", round(salario/horas, 2))