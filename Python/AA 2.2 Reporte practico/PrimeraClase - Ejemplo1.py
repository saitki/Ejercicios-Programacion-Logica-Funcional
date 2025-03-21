def obtener_pizza():
    return "🍕"

def obtener_hamburguesa():
    return "🍔"

def obtener_Bebida():
    return "🍹"

def main():
    cs = True
    while cs:
        print("-- Restaruante laTec --")
        print("-- Menu de Alimentos --")
        print("1.- Humburguesa")
        print("2.- Pizza")
        print("3.- Bebida")
        print("4.- Salir")
        opt = int(input("Ingrese una opción: "))
        if opt == 1:
            res = obtener_pizza
        if opt == 2:
            res = obtener_hamburguesa
        if opt == 3:
            res = obtener_Bebida
        elif opt == 4:
            cs = False

        if (opt < 4 and opt > 0):
            print(f"La Comida solicitada es: {res()}")
main()