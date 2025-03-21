def operaciones(operacion):
    def agregar_producto(lista, id, nombre):
        if id in lista:
            print("El ID ya existe.")
        else:
            lista[id] = nombre
            print(f"Producto {nombre} fue agregado")
    def eliminar_producto(lista, id):
        if id in lista:
            del lista[id]
            print(f"Producto {id} eliminado.")
        else:
            print("ID no encontrado.")
    if(operacion == "Agregar"):
        return agregar_producto
    elif(operacion=="Eliminar"):
        return eliminar_producto
def menu():
    listaProductos = {}  
    cs = True
    while cs:
        print("-- Sistema de Inventario --")
        print("1.- Consultar productos")
        print("2.- Agregar nuevo producto")
        print("3.- Eliminar producto")
        print("4.- Salir")
        opt = int(input("Ingrese una opción: "))
        if opt == 1:
            if listaProductos:
                print(" -- Lista de Productos --")
                for id, nombre in listaProductos.items():
                    print(f"ID: {id} \nNombre: {nombre}")
                    print("---------")
            else:
                print("No hay productos en inventario...")
        elif opt == 2:
            print(" -- Ingreso de Productos --")
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            agregar = operaciones("Agregar")
            agregar(listaProductos, id, nombre)
        elif opt == 3:
            print(" -- Eliminacion de Productos --")
            id = input("Ingrese el ID del producto a eliminar: ")
            eliminar = operaciones("Eliminar")
            eliminar(listaProductos, id)
        elif opt == 4:
            print("Saliendo del sistema....")
            cs = False
        else:
            print("Opción no válida!!!!")
menu()
