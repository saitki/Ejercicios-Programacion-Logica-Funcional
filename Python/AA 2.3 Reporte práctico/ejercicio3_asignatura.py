
asignaturas_viii = ["Programacion logica y funcional"]
asignaturas_nueva = asignaturas_viii + ["bbdd"]

print(asignaturas_nueva)

def agregar_asignatura(lista,asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignaturas_viii, input("Ingrese una materia: ")))