import time

def obtener_datos(callback):
    print("Obteniendo datos...")
    time.sleep(2)  
    datos = {"nombre": "Alejandro Lenier", "edad": 22, "semestre": "8", "grupo": "B", "nocontrol": "211k0063"}
    callback(datos)  

def procesar_datos(datos):
    print(" -- Datos recibidos --")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Semestre: {datos['semestre']}")
    print(f"Grupo: {datos['grupo']}")
    print(f"No.control: {datos['nocontrol']}")

print("-- Simulador datos de llegada a Api --")
print("Estudiante del Tec")
obtener_datos(procesar_datos)
