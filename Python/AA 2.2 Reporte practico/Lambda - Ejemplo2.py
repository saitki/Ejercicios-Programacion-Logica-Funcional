print("-- Filtrado de estudiantes --")
estudiantesDelTec = {"Diego Amanecer": 85, "Jose Rodrigo": 92, "Armando Hernandez": 70, "Adriel Balam": 58}
aprobados = dict(filter(lambda x: x[1] >= 75, estudiantesDelTec.items()))
print(aprobados)
