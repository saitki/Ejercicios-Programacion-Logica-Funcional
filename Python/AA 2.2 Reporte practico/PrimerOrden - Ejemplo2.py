def consulta_saldo(saldo):
    return f'su saldo actual es {saldo}'

def ingreso_dinero(saldo_actual, saldo_ingresado):
    return saldo_actual + saldo_ingresado

def retirar_dinero(saldo_actual, saldo_ingresado):
    return saldo_actual - saldo_ingresado

def main():
    cs = True
    saldo = 100

    while(cs):
        print("---- Banco BanTec ----")
        print("1.- Consultar saldo")
        print("2.- Ingresar saldo")
        print("3.- Retirar saldo")
        print("4.- Salir de la aplicacion")
        opt = int(input("Ingrese una opcion: "))
        if(opt == 1):
            print("-- Saldo Disponible --")
            print(consulta_saldo(saldo))
        elif(opt == 2):
            print("-- Ingreso de Saldo --")
            ingreso = int(input("Ingrese una cantidad: "))
            saldo = ingreso_dinero(saldo, ingreso)
        elif(opt == 3):
            print("-- Retiro de Saldo --")
            ingreso = int(input("Ingrese una cantidad: "))
            if(ingreso>saldo):
                print("No dispone de suficiente saldo...")
            else:
                saldo = retirar_dinero(saldo, ingreso)
        elif (opt == 4):
            print("-- Saliste de la aplicacion --")
            cs = False
        else:
            print("Opcion no valida!!")
main()