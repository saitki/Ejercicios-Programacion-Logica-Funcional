def operaciones(operacion):
    if(operacion == "suma"):
        return lambda x,y: x+y
    if(operacion == "resta"):
        return lambda x,y: x-y
    if(operacion == "multiplicacion"):
        return lambda x,y: x*y
def menu():
    cs = True
    res = 0
    while cs:
        print("-- Sistema de Operaciones --")
        print("1.- Sumar 2 numeros")
        print("2.- Resta 2 numeros")
        print("3.- Multiplicacion 2 numeros")
        print("4.- Salir")
        opt = int(input("Ingrese una opción: "))
        if opt == 1:
            print(" -- Suma de 2 valores --")
            v1 = int(input("Ingrese un valor: "))
            v2 = int(input("Ingrese segundo valor: "))
            suma = operaciones("suma")
            res = suma(v1, v2)
        elif opt == 2:
            print(" -- Resta de 2 valores --")
            v1 = int(input("Ingrese un valor: "))
            v2 = int(input("Ingrese segundo valor: "))
            resta = operaciones("resta")
            res = resta(v1, v2)
        elif opt == 3:
            print(" -- Multiplicacion de 2 valores --")
            v1 = int(input("Ingrese un valor: "))
            v2 = int(input("Ingrese segundo valor: "))
            multiplicacion = operaciones("multiplicacion")
            res = multiplicacion(v1, v2)
        elif opt == 4:
            print("Saliendo del sistema....")
            cs = False
        else:
            print("Opción no válida!!!!")
        if (opt < 4 and opt > 0):
            print(f"La respuesta es: {res}")
menu()
