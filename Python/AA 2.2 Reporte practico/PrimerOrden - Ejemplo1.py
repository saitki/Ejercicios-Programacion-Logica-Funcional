def menu():
    print("---- Menu de opciones aritmeticas ----")
    print("1 - Sumar")
    print("2 - Restar")
    return int(input("Ingrese una opcion: "))

def suma(valor1, valor2):
    return valor1 + valor2
def resta(valor1, valor2):
    return valor1 - valor2

def main():
    opt = menu()
    res = 0
    if opt == 1:
        print("-- Opcion de suma --")
        valor1 = int(input("Ingrese un valor:"))
        valor2 = int(input("Ingrese segunda valor:"))
        res = suma(valor1, valor2)
    elif opt == 2:
        print("-- Opcion de resta --")
        valor1 = int(input("Ingrese un valor:"))
        valor2 = int(input("Ingrese segunda valor:"))
        res = resta(valor1, valor2)
    else:
        print("Opcion no valida!!")

    if (opt < 3 and opt > 0):
        print(f"La respuesta es: {res}")

main()
