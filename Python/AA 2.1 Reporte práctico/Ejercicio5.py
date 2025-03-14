#formula para calcular la cadena de bits de un número entero 
def cadenaBits(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return cadenaBits(numero // 2) + str(numero % 2)


print(cadenaBits(10))

