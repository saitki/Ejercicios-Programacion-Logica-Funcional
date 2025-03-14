#tipos de datos
#colecciones
#listas
lista = [1,2,3,4,5]
print(lista)
print(lista[0])
print(lista[1])

#tuplas
tupla = (1,2,3,4,5)
print(tupla)
print(tupla[0])
print(tupla[1])

#diccionarios
diccionario = {'nombre': 'juan', 'edad': 22}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])

#conjuntos
conjunto = {1,2,3,4,5}
print(conjunto)

#convertir cadena a entero
numero = int("10")
print(numero)

#convertir cadena a flotante
numero = float("10.5")
print(numero)

#convertir entero a cadena
numero = str(10)
print(numero)

#convertir flotante a cadena
numero = str(10.5)
print(numero)

#convertir entero a flotante
numero = float(10)
print(numero)

#convertir flotante a entero
numero = int(10.5)
print(numero)

#operaciones aritméticas
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("Division: ", num1 / num2)

#operaciones relacionales
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print("¿El primer numero es mayor que el segundo?: ", num1 > num2)
print("¿El primer numero es menor que el segundo?: ", num1 < num2)
print("¿El primer numero es mayor o igual que el segundo?: ", num1 >= num2)
print("¿El primer numero es menor o igual que el segundo?: ", num1 <= num2)
print("¿El primer numero es igual que el segundo?: ", num1 == num2)
print("¿El primer numero es diferente que el segundo?: ", num1 != num2)

#operaciones logicas
print("Operaciones logicas")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False", False or False)
print("Not True: ", not True)
print("Not False: ", not False)

#operaciones de asignacion
num1 = 10
num1 += 5
print(num1)
num1 -= 5
print(num1)
num1 *= 5
print(num1)
num1 /= 5
print(num1)
num1 %= 5
print(num1)
num1 **= 5 #exponente
print(num1)
num1 //= 5 #division entera
print(num1)

#Operaciones de pertenencia
lista = [1,2,3,4,5]
print(1 in lista)
print(6 in lista) #imprime false
print(1 not in lista) #imprime false
print(6 not in lista)

aprobado = float(input("Ingresa tu calificacion: "))
print("¿Aprobaste?: ", aprobado)


