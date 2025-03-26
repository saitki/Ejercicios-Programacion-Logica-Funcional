def agregar_Asignatura(lista):
    asing_nueva = input("Ingrese una nueva asignatura: ")
    if(asing_nueva == "exit"):
        return lista
    return agregar_Asignatura(lista + [asing_nueva])

asignaturas_viii = ["Programacion logica y funcional", "Adm. Redes", "Inteligencia Artificial"]
nueva_lista = agregar_Asignatura(asignaturas_viii)
print(asignaturas_viii)
print(nueva_lista)
