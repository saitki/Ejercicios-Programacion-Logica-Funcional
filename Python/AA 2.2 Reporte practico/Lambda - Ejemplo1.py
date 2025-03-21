from functools import reduce

print("-- Calculo de calificaiones --")
cant_calificaciones = int(input("Ingrese la cantidad de calificicaciones a calificar: "))
calificaciones = []  
cont = 0

for i in range(cant_calificaciones):
    calificaciones.append(int(input(f"Ingrese la calificacion {i+1}: ")))
    cont +=1
suma_total = reduce(lambda x, y: x + y, calificaciones)
cal_total = suma_total/cont
print(cal_total)