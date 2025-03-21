def leer_pensamiento(pensamiento):
    return f'lo que pensastes fue: "{pensamiento}"'

print("---- Juego Interactuvo (Leer pensamientos) para pasar el rato en el aula ----")
cs = True
while cs:
    pensamiento = input("Piensa en algo, escribelo y intentare adivinar lo que pensastes: ")
    fun_pensamiento = leer_pensamiento
    print(fun_pensamiento(pensamiento))
    print("¿Quieres continuar?")
    print("1.- Si")
    print("2.- No")
    opt = int(input("Ingrese una opción: "))
    if opt == 1:
        continue
    if opt == 2:
        print("¡Gracias por jugar!")
        cs = False
