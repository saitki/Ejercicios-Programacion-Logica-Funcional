def operacion(a, b, opt, callback):
    if(opt == "suma"):
        resultado = a + b 
    elif(opt == "resta"): 
        resultado = a - b 
    callback(resultado)

def mostrar_resultado(result):
    print(f"El resultado es: {result}")

print("-- Operaciones matemáticas con callback --")
print("1.- Suma")
print("2.- Resta")
opt = int(input("Ingrese una opción: "))

if opt == 1:
    caso = "suma"
elif opt == 2:
    caso = "resta"

if (opt < 4 and opt > 0):
    v1 = int(input("Ingrese un valor: "))
    v2 = int(input("Ingrese segundo valor: "))
    operacion(v1, v2, caso, mostrar_resultado)
