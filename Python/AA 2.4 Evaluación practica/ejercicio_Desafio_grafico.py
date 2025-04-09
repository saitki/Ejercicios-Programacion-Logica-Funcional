# Importamos funciones
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

# Variables globales
materia = ""
LenguajeSumaTotal = 0
LenguajeSumaTotalGeneral = 0
LenguajePromedioTotal = 0
LenguajePromedioTotalGeneral = 0
respuestas_mayores_lenguaje = 0
respuestas_mayores_lenguaje_general = 0
respuestas_menores_lenguaje = 0
respuestas_menores_lenguaje_general = 0
lista_respuesta_Lenguaje = []
lista_respuesta_promedio_lenguaje_general = []

TemasSumaTotal = 0
TemasSumaTotalGeneral = 0
TemasPromedioTotal = 0
TemasPromedioTotalGeneral = 0
respuestas_mayores_Temas = 0
respuestas_mayores_Temas_general = 0
respuestas_menores_Temas = 0
respuestas_menores_Temas_general = 0
lista_respuesta_Temas = []
lista_respuesta_promedio_Temas_general = []

HerramientasSumaTotal = 0
HerramientasSumaTotalGeneral = 0
HerramientasPromedioTotal = 0
HerramientasPromedioTotalGeneral = 0
respuestas_mayores_Herramientas = 0
respuestas_mayores_Herramientas_general = 0
respuestas_menores_Herramientas = 0
respuestas_menores_Herramientas_general = 0
lista_respuesta_Herramientas = []
lista_respuesta_promedio_Herramientas_general = []

ActividadesSumaTotal = 0
ActividadesSumaTotalGeneral = 0
ActividadesPromedioTotal = 0
ActividadesPromedioTotalGeneral = 0
respuestas_mayores_Actividades = 0
respuestas_mayores_Actividades_general = 0
respuestas_menores_Actividades = 0
respuestas_menores_Actividades_general = 0
lista_respuesta_Actividades = []
lista_respuesta_promedio_Actividades_general = []

ContenidoSumaTotal = 0
ContenidoSumaTotalGeneral = 0
ContenidoPromedioTotal = 0
ContenidoPromedioTotalGeneral = 0
respuestas_mayores_Contenido = 0
respuestas_mayores_Contenido_general = 0
respuestas_menores_Contenido = 0
respuestas_menores_Contenido_general = 0
lista_respuesta_Contenido = []
lista_respuesta_promedio_Contenido_general = []

contador_usuario = 1

# Funcion orden superior como herramienta
def menu_operaciones(opr):
    # Funcion suma de 2 valores y retornar resultado
    def suma(x, y):
        return x + y
    # Funcion Conversion de str a int
    def conversion_entero(x):
        return int(x)
    # Funcion filtrar mayor, en este caso 5
    def filtrar_mayor_a_5(x):
        return x == 5
    # Funcion filtrar menor, en este caso 0
    def filtrar_menor_a_0(x):
        return x == 0
    # Funcion de contar una lista y devolver el conteo en una nueva lista de los elementos contados
    def lista_contador(lista, x, valor):
        # suma desde el valor dado x
        x = x + 1
        # guarda x en la lista dada
        lista = lista + [x]
        # retorna lista si x es igual al valor dado a alcanzar, sino llamar a la misma funcion hasta llegar 
        return lista if x == valor else lista_contador(lista, x, valor)
    # Llamaddo del tipo de funcion
    if(opr == "suma"):
        return suma
    if(opr == "toInt"):
        return conversion_entero
    if(opr == "mayor"):
        return filtrar_mayor_a_5
    if(opr == "menor"):
        return filtrar_menor_a_0
    if(opr == "contar"):
        return lista_contador

# Clase principal para la aplicación
class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Encuestas")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Funciones de operaciones
        self.suma = menu_operaciones("suma")
        self.entero = menu_operaciones("toInt")
        self.mayor = menu_operaciones("mayor")
        self.menor = menu_operaciones("menor")
        self.lista_contador = menu_operaciones("contar")
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Crear frames para cada pestaña
        self.frame_inicio = ttk.Frame(self.notebook)
        self.frame_lenguaje = ttk.Frame(self.notebook)
        self.frame_temas = ttk.Frame(self.notebook)
        self.frame_herramientas = ttk.Frame(self.notebook)
        self.frame_actividades = ttk.Frame(self.notebook)
        self.frame_contenido = ttk.Frame(self.notebook)
        self.frame_resultados = ttk.Frame(self.notebook)
        
        # Añadir frames al notebook
        self.notebook.add(self.frame_inicio, text="Inicio")
        self.notebook.add(self.frame_lenguaje, text="Lenguaje")
        self.notebook.add(self.frame_temas, text="Temas")
        self.notebook.add(self.frame_herramientas, text="Herramientas")
        self.notebook.add(self.frame_actividades, text="Actividades")
        self.notebook.add(self.frame_contenido, text="Contenido")
        self.notebook.add(self.frame_resultados, text="Resultados")
        
        # Inicializar componentes
        self.init_inicio()
        self.init_lenguaje()
        self.init_temas()
        self.init_herramientas()
        self.init_actividades()
        self.init_contenido()
        self.init_resultados()
    
    def init_inicio(self):
        # Frame de inicio
        titulo = ttk.Label(self.frame_inicio, text="Sistema de Encuestas Educativas", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)
        
        info = ttk.Label(self.frame_inicio, text="Esta aplicación permite evaluar diferentes aspectos de una materia.",
                         font=("Arial", 12))
        info.pack(pady=10)
        
        # Frame para materia
        frame_materia = ttk.Frame(self.frame_inicio)
        frame_materia.pack(pady=20)
        
        ttk.Label(frame_materia, text="Materia:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_materia = ttk.Entry(frame_materia, width=30, font=("Arial", 12))
        self.entry_materia.grid(row=0, column=1, padx=5, pady=5)
        
        if materia:
            self.entry_materia.insert(0, materia)
        
        ttk.Button(frame_materia, text="Guardar Materia", command=self.guardar_materia).grid(row=0, column=2, padx=5, pady=5)
        
        # Información de usuario
        global contador_usuario
        frame_usuario = ttk.Frame(self.frame_inicio)
        frame_usuario.pack(pady=20)
        
        ttk.Label(frame_usuario, text=f"Usuario actual: {contador_usuario}", font=("Arial", 12)).pack()
        
        # Instrucciones
        instrucciones = """
        Instrucciones:
        1. Ingrese el nombre de la materia
        2. Complete cada sección de la encuesta (Lenguaje, Temas, etc.)
        3. Vea los resultados en la pestaña "Resultados"
        4. Finalice su encuesta para permitir que otro usuario pueda completarla
        """
        ttk.Label(self.frame_inicio, text=instrucciones, font=("Arial", 12)).pack(pady=20)
        
        # Botón para finalizar encuesta
        ttk.Button(self.frame_inicio, text="Finalizar Mi Encuesta", 
                  command=self.finalizar_encuesta, padding=10).pack(pady=20)
    
    def crear_seccion_encuesta(self, frame, preguntas, titulo):
        # Título de la sección
        ttk.Label(frame, text=f"Encuesta - {titulo}", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Instrucciones
        ttk.Label(frame, text="Califique cada aspecto del 0 al 5 (0=Deficiente, 5=Excelente)", 
                 font=("Arial", 12)).pack(pady=10)
        
        # Crear frame para preguntas
        frame_preguntas = ttk.Frame(frame)
        frame_preguntas.pack(pady=10, fill="both", expand=True)
        
        # Variables para almacenar respuestas
        respuestas = []
        
        # Crear widgets para cada pregunta
        for i, pregunta in enumerate(preguntas):
            frame_pregunta = ttk.Frame(frame_preguntas)
            frame_pregunta.pack(fill="x", pady=5)
            
            ttk.Label(frame_pregunta, text=pregunta, font=("Arial", 12)).pack(side="left", padx=10)
            
            # Crear variable para el valor de la escala
            var = tk.IntVar(value=0)
            respuestas.append(var)
            
            # Frame para escala y valor
            frame_escala = ttk.Frame(frame_pregunta)
            frame_escala.pack(side="right", padx=10)
            
            # Etiqueta para mostrar el valor
            lbl_valor = ttk.Label(frame_escala, text="0", width=2)
            lbl_valor.pack(side="right", padx=5)
            
            # Escala
            escala = ttk.Scale(frame_escala, from_=0, to=5, orient="horizontal", 
                               variable=var, length=200)
            escala.pack(side="right")
            
            # Función para actualizar la etiqueta cuando cambia la escala
            def actualizar_valor(var=var, lbl=lbl_valor):
                lbl.config(text=str(int(var.get())))
            
            escala.config(command=lambda val, v=var, l=lbl_valor: l.config(text=str(int(float(val)))))
        
        # Botón para guardar respuestas
        btn_guardar = ttk.Button(frame, text=f"Guardar Respuestas de {titulo}", 
                                padding=10, command=lambda p=preguntas, r=respuestas, t=titulo: self.guardar_respuestas(p, r, t))
        btn_guardar.pack(pady=20)
        
        return respuestas
    
    def init_lenguaje(self):
        lista_preguntas_Lenguaje = [
            "1.- ¿Es comprensible las expresiones que utiliza el maestro?", 
            "2.- ¿Son muy complejo las expresiones?", 
            "3.- ¿Es muy tecnico la expresion al sentido comun?", 
            "4.- ¿Conoces las expresiones?"
        ]
        self.respuestas_lenguaje = self.crear_seccion_encuesta(self.frame_lenguaje, lista_preguntas_Lenguaje, "Lenguaje")
    
    def init_temas(self):
        lista_preguntas_Temas = [
            "1.- ¿Los temas tratados fueron interesantes?", 
            "2.- ¿Los temas estaban relacionados con tu carrera?",
            "3.- ¿Se cubrieron todos los temas planeados en el curso?",
            "4.- ¿Los temas fueron explicados de manera clara?"
        ]
        self.respuestas_temas = self.crear_seccion_encuesta(self.frame_temas, lista_preguntas_Temas, "Temas")
    
    def init_herramientas(self):
        lista_preguntas_Herramientas = [
            "1.- ¿Las herramientas utilizadas ayudaron a tu aprendizaje?", 
            "2.- ¿Fue fácil acceder a las herramientas del curso?", 
            "3.- ¿Las herramientas estaban actualizadas?",
            "4.- ¿Se utilizaron herramientas digitales (software, plataformas) de forma efectiva?"
        ]
        self.respuestas_herramientas = self.crear_seccion_encuesta(self.frame_herramientas, lista_preguntas_Herramientas, "Herramientas")
    
    def init_actividades(self):
        lista_preguntas_Actividades = [
            "1.- ¿Las actividades ayudaron a entender los temas?",
            "2.- ¿Fueron claras las instrucciones de las actividades?",
            "3.- ¿Las actividades fueron adecuadas al nivel del curso?",
            "4.- ¿Hubo suficiente variedad de actividades?"
        ]
        self.respuestas_actividades = self.crear_seccion_encuesta(self.frame_actividades, lista_preguntas_Actividades, "Actividades")
    
    def init_contenido(self):
        lista_preguntas_Contenido = [
            "1.- ¿El contenido fue útil para tu formación profesional?",
            "2.- ¿Estuvo bien organizado el contenido del curso?",
            "3.- ¿El contenido estaba actualizado?",
            "4.- ¿El contenido fue suficiente para comprender los temas?"
        ]
        self.respuestas_contenido = self.crear_seccion_encuesta(self.frame_contenido, lista_preguntas_Contenido, "Contenido")
    
    def init_resultados(self):
        # Frame principal de resultados
        frame_resultados_scroll = ttk.Frame(self.frame_resultados)
        frame_resultados_scroll.pack(fill="both", expand=True)
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(frame_resultados_scroll)
        scrollbar = ttk.Scrollbar(frame_resultados_scroll, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        
        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título
        ttk.Label(scroll_frame, text="Resultados de la Encuesta", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Crear pestañas para los diferentes resultados
        self.notebook_resultados = ttk.Notebook(scroll_frame)
        self.notebook_resultados.pack(fill="both", expand=True, pady=10)
        
        # Frames para cada categoría
        self.frame_res_general = ttk.Frame(self.notebook_resultados)
        self.frame_res_lenguaje = ttk.Frame(self.notebook_resultados)
        self.frame_res_temas = ttk.Frame(self.notebook_resultados)
        self.frame_res_herramientas = ttk.Frame(self.notebook_resultados)
        self.frame_res_actividades = ttk.Frame(self.notebook_resultados)
        self.frame_res_contenido = ttk.Frame(self.notebook_resultados)
        
        # Añadir frames al notebook
        self.notebook_resultados.add(self.frame_res_general, text="General")
        self.notebook_resultados.add(self.frame_res_lenguaje, text="Lenguaje")
        self.notebook_resultados.add(self.frame_res_temas, text="Temas")
        self.notebook_resultados.add(self.frame_res_herramientas, text="Herramientas")
        self.notebook_resultados.add(self.frame_res_actividades, text="Actividades")
        self.notebook_resultados.add(self.frame_res_contenido, text="Contenido")
        
        # Botón para actualizar resultados
        ttk.Button(scroll_frame, text="Actualizar Resultados", 
                  command=self.actualizar_resultados, padding=10).pack(pady=20)
        
        # Botón para mostrar gráficos
        ttk.Button(scroll_frame, text="Mostrar Gráficos Comparativos", 
                  command=self.mostrar_graficos, padding=10).pack(pady=10)
        
        # Inicializar los frames de resultados
        self.init_frame_resultados()
    
    def init_frame_resultados(self):
        # Inicializar con información básica
        categorias = ["General", "Lenguaje", "Temas", "Herramientas", "Actividades", "Contenido"]
        frames = [self.frame_res_general, self.frame_res_lenguaje, self.frame_res_temas, 
                 self.frame_res_herramientas, self.frame_res_actividades, self.frame_res_contenido]
        
        for cat, frame in zip(categorias, frames):
            ttk.Label(frame, text=f"Resultados de {cat}", font=("Arial", 14, "bold")).pack(pady=10)
            ttk.Label(frame, text="Complete la encuesta para ver los resultados", font=("Arial", 12)).pack(pady=10)
    
    def guardar_materia(self):
        global materia
        materia = self.entry_materia.get()
        if materia:
            messagebox.showinfo("Información", f"Materia '{materia}' guardada correctamente")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar el nombre de la materia")
    
    def guardar_respuestas(self, preguntas, respuestas_vars, categoria):
        global lista_respuesta_Lenguaje, lista_respuesta_Temas, lista_respuesta_Herramientas
        global lista_respuesta_Actividades, lista_respuesta_Contenido
        global LenguajeSumaTotal, LenguajePromedioTotal, respuestas_mayores_lenguaje, respuestas_menores_lenguaje
        global TemasSumaTotal, TemasPromedioTotal, respuestas_mayores_Temas, respuestas_menores_Temas
        global HerramientasSumaTotal, HerramientasPromedioTotal, respuestas_mayores_Herramientas, respuestas_menores_Herramientas
        global ActividadesSumaTotal, ActividadesPromedioTotal, respuestas_mayores_Actividades, respuestas_menores_Actividades
        global ContenidoSumaTotal, ContenidoPromedioTotal, respuestas_mayores_Contenido, respuestas_menores_Contenido
        
        # Obtener los valores de las respuestas
        respuestas = [var.get() for var in respuestas_vars]
        
        # Guardar respuestas según la categoría
        if categoria == "Lenguaje":
            lista_respuesta_Lenguaje = respuestas
            respuestas_mayores_lenguaje = len(list(filter(self.mayor, lista_respuesta_Lenguaje)))
            respuestas_menores_lenguaje = len(list(filter(self.menor, lista_respuesta_Lenguaje)))
            LenguajeSumaTotal = reduce(self.suma, lista_respuesta_Lenguaje, 0)
            LenguajePromedioTotal = LenguajeSumaTotal / len(preguntas)
        elif categoria == "Temas":
            lista_respuesta_Temas = respuestas
            respuestas_mayores_Temas = len(list(filter(self.mayor, lista_respuesta_Temas)))
            respuestas_menores_Temas = len(list(filter(self.menor, lista_respuesta_Temas)))
            TemasSumaTotal = reduce(self.suma, lista_respuesta_Temas, 0)
            TemasPromedioTotal = TemasSumaTotal / len(preguntas)
        elif categoria == "Herramientas":
            lista_respuesta_Herramientas = respuestas
            respuestas_mayores_Herramientas = len(list(filter(self.mayor, lista_respuesta_Herramientas)))
            respuestas_menores_Herramientas = len(list(filter(self.menor, lista_respuesta_Herramientas)))
            HerramientasSumaTotal = reduce(self.suma, lista_respuesta_Herramientas, 0)
            HerramientasPromedioTotal = HerramientasSumaTotal / len(preguntas)
        elif categoria == "Actividades":
            lista_respuesta_Actividades = respuestas
            respuestas_mayores_Actividades = len(list(filter(self.mayor, lista_respuesta_Actividades)))
            respuestas_menores_Actividades = len(list(filter(self.menor, lista_respuesta_Actividades)))
            ActividadesSumaTotal = reduce(self.suma, lista_respuesta_Actividades, 0)
            ActividadesPromedioTotal = ActividadesSumaTotal / len(preguntas)
        elif categoria == "Contenido":
            lista_respuesta_Contenido = respuestas
            respuestas_mayores_Contenido = len(list(filter(self.mayor, lista_respuesta_Contenido)))
            respuestas_menores_Contenido = len(list(filter(self.menor, lista_respuesta_Contenido)))
            ContenidoSumaTotal = reduce(self.suma, lista_respuesta_Contenido, 0)
            ContenidoPromedioTotal = ContenidoSumaTotal / len(preguntas)
        
        # Mostrar resultados
        resultado = f"""
        Resultados para {categoria}:
        Suma total: {reduce(self.suma, respuestas, 0)}
        Promedio: {reduce(self.suma, respuestas, 0) / len(preguntas):.2f}
        Respuestas con valor 5: {len(list(filter(self.mayor, respuestas)))}
        Respuestas con valor 0: {len(list(filter(self.menor, respuestas)))}
        """
        messagebox.showinfo(f"Resultados - {categoria}", resultado)
        
        # Actualizar resultados
        self.actualizar_resultados()
    
    def actualizar_resultados(self):
        # Limpiar frames
        for widget in self.frame_res_general.winfo_children():
            widget.destroy()
        for widget in self.frame_res_lenguaje.winfo_children():
            widget.destroy()
        for widget in self.frame_res_temas.winfo_children():
            widget.destroy()
        for widget in self.frame_res_herramientas.winfo_children():
            widget.destroy()
        for widget in self.frame_res_actividades.winfo_children():
            widget.destroy()
        for widget in self.frame_res_contenido.winfo_children():
            widget.destroy()
        
        # Función para crear sección de resultados
        def crear_seccion_resultados(frame, titulo, suma, promedio, mayores, menores, lista_respuestas=None):
            ttk.Label(frame, text=f"Resultados de {titulo}", font=("Arial", 14, "bold")).pack(pady=10)
            
            # Frame para la información
            frame_info = ttk.Frame(frame)
            frame_info.pack(pady=10, fill="x")
            
            # Mostrar información
            info_text = f"""
            Suma total: {suma}
            Promedio: {promedio:.2f}
            Respuestas con valor 5: {mayores}
            Respuestas con valor 0: {menores}
            """
            ttk.Label(frame_info, text=info_text, font=("Arial", 12)).pack(pady=10)
            
            # Si hay respuestas, mostrar gráfico
            if lista_respuestas and len(lista_respuestas) > 0:
                fig = plt.Figure(figsize=(5, 4), dpi=100)
                ax = fig.add_subplot(111)
                
                # Índices para el eje x
                indices = list(range(1, len(lista_respuestas) + 1))
                
                # Crear gráfico
                ax.bar(indices, lista_respuestas)
                ax.set_title(f"Respuestas - {titulo}")
                ax.set_xlabel("Pregunta")
                ax.set_ylabel("Valor")
                ax.set_ylim(0, 5)
                
                # Añadir gráfico al frame
                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas.draw()
                canvas.get_tk_widget().pack(pady=10, fill="both", expand=True)
        
        # Actualizar secciones de resultados
        # General (promedio de todas las categorías)
        if len(lista_respuesta_promedio_lenguaje_general) > 0:
            general_promedio = (
                sum(lista_respuesta_promedio_lenguaje_general) / len(lista_respuesta_promedio_lenguaje_general) if lista_respuesta_promedio_lenguaje_general else 0 +
                sum(lista_respuesta_promedio_Temas_general) / len(lista_respuesta_promedio_Temas_general) if lista_respuesta_promedio_Temas_general else 0 +
                sum(lista_respuesta_promedio_Herramientas_general) / len(lista_respuesta_promedio_Herramientas_general) if lista_respuesta_promedio_Herramientas_general else 0 +
                sum(lista_respuesta_promedio_Actividades_general) / len(lista_respuesta_promedio_Actividades_general) if lista_respuesta_promedio_Actividades_general else 0 +
                sum(lista_respuesta_promedio_Contenido_general) / len(lista_respuesta_promedio_Contenido_general) if lista_respuesta_promedio_Contenido_general else 0
            ) / 5
            
            crear_seccion_resultados(
                self.frame_res_general,
                "Todas las Categorías",
                sum(lista_respuesta_promedio_lenguaje_general) + sum(lista_respuesta_promedio_Temas_general) + 
                sum(lista_respuesta_promedio_Herramientas_general) + sum(lista_respuesta_promedio_Actividades_general) + 
                sum(lista_respuesta_promedio_Contenido_general),
                general_promedio,
                respuestas_mayores_lenguaje_general + respuestas_mayores_Temas_general + 
                respuestas_mayores_Herramientas_general + respuestas_mayores_Actividades_general + 
                respuestas_mayores_Contenido_general,
                respuestas_menores_lenguaje_general + respuestas_menores_Temas_general + 
                respuestas_menores_Herramientas_general + respuestas_menores_Actividades_general + 
                respuestas_menores_Contenido_general,
                [LenguajePromedioTotal, TemasPromedioTotal, HerramientasPromedioTotal, 
                 ActividadesPromedioTotal, ContenidoPromedioTotal]
            )
        else:
            ttk.Label(self.frame_res_general, 
                     text="Complete al menos una encuesta y finalícela para ver resultados generales", 
                     font=("Arial", 12)).pack(pady=20)
        
        # Lenguaje
        crear_seccion_resultados(
            self.frame_res_lenguaje,
            "Lenguaje",
            LenguajeSumaTotal,
            LenguajePromedioTotal,
            respuestas_mayores_lenguaje,
            respuestas_menores_lenguaje,
            lista_respuesta_Lenguaje
        )
        
        # Temas
        crear_seccion_resultados(
            self.frame_res_temas,
            "Temas",
            TemasSumaTotal,
            TemasPromedioTotal,
            respuestas_mayores_Temas,
            respuestas_menores_Temas,
            lista_respuesta_Temas
        )
        
        # Herramientas
        crear_seccion_resultados(
            self.frame_res_herramientas,
            "Herramientas",
            HerramientasSumaTotal,
            HerramientasPromedioTotal,
            respuestas_mayores_Herramientas,
            respuestas_menores_Herramientas,
            lista_respuesta_Herramientas
        )
        
        # Actividades
        crear_seccion_resultados(
            self.frame_res_actividades,
            "Actividades",
            ActividadesSumaTotal,
            ActividadesPromedioTotal,
            respuestas_mayores_Actividades,
            respuestas_menores_Actividades,
            lista_respuesta_Actividades
        )
        
# Contenido
        crear_seccion_resultados(
            self.frame_res_contenido,
            "Contenido",
            ContenidoSumaTotal,
            ContenidoPromedioTotal,
            respuestas_mayores_Contenido,
            respuestas_menores_Contenido,
            lista_respuesta_Contenido
        )
    
    def finalizar_encuesta(self):
        global contador_usuario
        global lista_respuesta_Lenguaje, lista_respuesta_Temas, lista_respuesta_Herramientas
        global lista_respuesta_Actividades, lista_respuesta_Contenido
        global LenguajeSumaTotal, LenguajePromedioTotal, respuestas_mayores_lenguaje, respuestas_menores_lenguaje
        global TemasSumaTotal, TemasPromedioTotal, respuestas_mayores_Temas, respuestas_menores_Temas
        global HerramientasSumaTotal, HerramientasPromedioTotal, respuestas_mayores_Herramientas, respuestas_menores_Herramientas
        global ActividadesSumaTotal, ActividadesPromedioTotal, respuestas_mayores_Actividades, respuestas_menores_Actividades
        global ContenidoSumaTotal, ContenidoPromedioTotal, respuestas_mayores_Contenido, respuestas_menores_Contenido
        global lista_respuesta_promedio_lenguaje_general, lista_respuesta_promedio_Temas_general
        global lista_respuesta_promedio_Herramientas_general, lista_respuesta_promedio_Actividades_general
        global lista_respuesta_promedio_Contenido_general
        global respuestas_mayores_lenguaje_general, respuestas_menores_lenguaje_general
        global respuestas_mayores_Temas_general, respuestas_menores_Temas_general
        global respuestas_mayores_Herramientas_general, respuestas_menores_Herramientas_general
        global respuestas_mayores_Actividades_general, respuestas_menores_Actividades_general
        global respuestas_mayores_Contenido_general, respuestas_menores_Contenido_general
        
        # Verificar que se hayan completado todas las secciones
        if not lista_respuesta_Lenguaje or not lista_respuesta_Temas or not lista_respuesta_Herramientas or not lista_respuesta_Actividades or not lista_respuesta_Contenido:
            messagebox.showwarning("Advertencia", "Debe completar todas las secciones de la encuesta antes de finalizar")
            return
        
        # Guardar resultados en las variables generales
        lista_respuesta_promedio_lenguaje_general.append(LenguajePromedioTotal)
        respuestas_mayores_lenguaje_general += respuestas_mayores_lenguaje
        respuestas_menores_lenguaje_general += respuestas_menores_lenguaje
        
        lista_respuesta_promedio_Temas_general.append(TemasPromedioTotal)
        respuestas_mayores_Temas_general += respuestas_mayores_Temas
        respuestas_menores_Temas_general += respuestas_menores_Temas
        
        lista_respuesta_promedio_Herramientas_general.append(HerramientasPromedioTotal)
        respuestas_mayores_Herramientas_general += respuestas_mayores_Herramientas
        respuestas_menores_Herramientas_general += respuestas_menores_Herramientas
        
        lista_respuesta_promedio_Actividades_general.append(ActividadesPromedioTotal)
        respuestas_mayores_Actividades_general += respuestas_mayores_Actividades
        respuestas_menores_Actividades_general += respuestas_menores_Actividades
        
        lista_respuesta_promedio_Contenido_general.append(ContenidoPromedioTotal)
        respuestas_mayores_Contenido_general += respuestas_mayores_Contenido
        respuestas_menores_Contenido_general += respuestas_menores_Contenido
        
        # Reiniciar variables para el siguiente usuario
        lista_respuesta_Lenguaje = []
        respuestas_mayores_lenguaje = 0
        respuestas_menores_lenguaje = 0
        LenguajeSumaTotal = 0
        LenguajePromedioTotal = 0
        
        lista_respuesta_Temas = []
        respuestas_mayores_Temas = 0
        respuestas_menores_Temas = 0
        TemasSumaTotal = 0
        TemasPromedioTotal = 0
        
        lista_respuesta_Herramientas = []
        respuestas_mayores_Herramientas = 0
        respuestas_menores_Herramientas = 0
        HerramientasSumaTotal = 0
        HerramientasPromedioTotal = 0
        
        lista_respuesta_Actividades = []
        respuestas_mayores_Actividades = 0
        respuestas_menores_Actividades = 0
        ActividadesSumaTotal = 0
        ActividadesPromedioTotal = 0
        
        lista_respuesta_Contenido = []
        respuestas_mayores_Contenido = 0
        respuestas_menores_Contenido = 0
        ContenidoSumaTotal = 0
        ContenidoPromedioTotal = 0
        
        # Incrementar contador de usuario
        contador_usuario += 1
        
        # Actualizar la interfaz
        self.actualizar_resultados()
        
        # Reiniciar las escalas en todas las secciones
        for var in self.respuestas_lenguaje + self.respuestas_temas + self.respuestas_herramientas + self.respuestas_actividades + self.respuestas_contenido:
            var.set(0)
        
        messagebox.showinfo("Encuesta Finalizada", f"Encuesta finalizada para el usuario {contador_usuario-1}. Ahora puede completar la encuesta el usuario {contador_usuario}.")
        
        # Volver a la pestaña de inicio
        self.notebook.select(0)
        
        # Actualizar información de usuario en la pestaña de inicio
        for widget in self.frame_inicio.winfo_children():
            if isinstance(widget, ttk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, ttk.Label) and f"Usuario actual:" in child.cget("text"):
                        child.config(text=f"Usuario actual: {contador_usuario}")
    
    def mostrar_graficos(self):
        # Crear una nueva ventana para los gráficos
        ventana_graficos = tk.Toplevel(self.root)
        ventana_graficos.title("Gráficos Comparativos")
        ventana_graficos.geometry("800x600")
        
        # Crear un notebook para organizar los gráficos
        notebook_graficos = ttk.Notebook(ventana_graficos)
        notebook_graficos.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frames para cada tipo de gráfico
        frame_general = ttk.Frame(notebook_graficos)
        frame_categorias = ttk.Frame(notebook_graficos)
        frame_usuarios = ttk.Frame(notebook_graficos)
        
        notebook_graficos.add(frame_general, text="General")
        notebook_graficos.add(frame_categorias, text="Por Categorías")
        notebook_graficos.add(frame_usuarios, text="Por Usuarios")
        
        # Gráfico general (promedio de todas las categorías)
        if lista_respuesta_promedio_lenguaje_general:
            fig_general = plt.Figure(figsize=(10, 6), dpi=100)
            ax_general = fig_general.add_subplot(111)
            
            categorias = ["Lenguaje", "Temas", "Herramientas", "Actividades", "Contenido"]
            promedios = [
                sum(lista_respuesta_promedio_lenguaje_general) / len(lista_respuesta_promedio_lenguaje_general) if lista_respuesta_promedio_lenguaje_general else 0,
                sum(lista_respuesta_promedio_Temas_general) / len(lista_respuesta_promedio_Temas_general) if lista_respuesta_promedio_Temas_general else 0,
                sum(lista_respuesta_promedio_Herramientas_general) / len(lista_respuesta_promedio_Herramientas_general) if lista_respuesta_promedio_Herramientas_general else 0,
                sum(lista_respuesta_promedio_Actividades_general) / len(lista_respuesta_promedio_Actividades_general) if lista_respuesta_promedio_Actividades_general else 0,
                sum(lista_respuesta_promedio_Contenido_general) / len(lista_respuesta_promedio_Contenido_general) if lista_respuesta_promedio_Contenido_general else 0
            ]
            
            ax_general.bar(categorias, promedios)
            ax_general.set_title(f"Promedio General por Categoría - {materia}")
            ax_general.set_xlabel("Categoría")
            ax_general.set_ylabel("Promedio")
            ax_general.set_ylim(0, 5)
            
            for i, v in enumerate(promedios):
                ax_general.text(i, v + 0.1, f"{v:.2f}", ha='center')
            
            canvas_general = FigureCanvasTkAgg(fig_general, master=frame_general)
            canvas_general.draw()
            canvas_general.get_tk_widget().pack(pady=10, fill="both", expand=True)
            
            # Información adicional
            info_general = f"""
            Materia: {materia}
            Número de usuarios encuestados: {len(lista_respuesta_promedio_lenguaje_general)}
            Promedio general: {sum(promedios) / len(promedios):.2f}
            """
            ttk.Label(frame_general, text=info_general, font=("Arial", 12)).pack(pady=10)
        else:
            ttk.Label(frame_general, text="No hay datos suficientes para mostrar gráficos", font=("Arial", 14)).pack(pady=50)
        
        # Gráfico por categorías (evolución por usuario)
        if lista_respuesta_promedio_lenguaje_general:
            fig_cat = plt.Figure(figsize=(10, 6), dpi=100)
            ax_cat = fig_cat.add_subplot(111)
            
            usuarios = list(range(1, len(lista_respuesta_promedio_lenguaje_general) + 1))
            
            ax_cat.plot(usuarios, lista_respuesta_promedio_lenguaje_general, 'o-', label='Lenguaje')
            ax_cat.plot(usuarios, lista_respuesta_promedio_Temas_general, 's-', label='Temas')
            ax_cat.plot(usuarios, lista_respuesta_promedio_Herramientas_general, '^-', label='Herramientas')
            ax_cat.plot(usuarios, lista_respuesta_promedio_Actividades_general, 'd-', label='Actividades')
            ax_cat.plot(usuarios, lista_respuesta_promedio_Contenido_general, '*-', label='Contenido')
            
            ax_cat.set_title(f"Evolución de Promedios por Usuario - {materia}")
            ax_cat.set_xlabel("Usuario")
            ax_cat.set_ylabel("Promedio")
            ax_cat.set_ylim(0, 5)
            ax_cat.legend()
            ax_cat.grid(True)
            
            canvas_cat = FigureCanvasTkAgg(fig_cat, master=frame_categorias)
            canvas_cat.draw()
            canvas_cat.get_tk_widget().pack(pady=10, fill="both", expand=True)
        else:
            ttk.Label(frame_categorias, text="No hay datos suficientes para mostrar gráficos", font=("Arial", 14)).pack(pady=50)
        
        # Gráfico por usuarios (promedio por usuario)
        if lista_respuesta_promedio_lenguaje_general:
            fig_usr = plt.Figure(figsize=(10, 6), dpi=100)
            ax_usr = fig_usr.add_subplot(111)
            
            usuarios = list(range(1, len(lista_respuesta_promedio_lenguaje_general) + 1))
            
            # Función recursiva para calcular los promedios por usuario
            def calcular_promedios_recursivo(i=0, promedios_usuarios=None):
                # Caso base: si hemos procesado todos los usuarios, devolvemos el resultado
                if i >= len(usuarios):
                    return promedios_usuarios
                
                # Inicializamos la lista de promedios en la primera llamada
                if promedios_usuarios is None:
                    promedios_usuarios = []
                
                # Calculamos el promedio para el usuario actual
                promedio_usuario = (
                    lista_respuesta_promedio_lenguaje_general[i] +
                    lista_respuesta_promedio_Temas_general[i] +
                    lista_respuesta_promedio_Herramientas_general[i] +
                    lista_respuesta_promedio_Actividades_general[i] +
                    lista_respuesta_promedio_Contenido_general[i]
                ) / 5
                
                # Añadimos el promedio a la lista
                promedios_usuarios.append(promedio_usuario)
                
                # Llamada recursiva para el siguiente usuario
                return calcular_promedios_recursivo(i + 1, promedios_usuarios)
            
            # Llamamos a la función recursiva para obtener los promedios
            promedios_usuarios = calcular_promedios_recursivo()
            
            ax_usr.bar(usuarios, promedios_usuarios)
            ax_usr.set_title(f"Promedio General por Usuario - {materia}")
            ax_usr.set_xlabel("Usuario")
            ax_usr.set_ylabel("Promedio")
            ax_usr.set_ylim(0, 5)
            
            for i, v in enumerate(promedios_usuarios):
                ax_usr.text(i + 1, v + 0.1, f"{v:.2f}", ha='center')
            
            canvas_usr = FigureCanvasTkAgg(fig_usr, master=frame_usuarios)
            canvas_usr.draw()
            canvas_usr.get_tk_widget().pack(pady=10, fill="both", expand=True)
        else:
            ttk.Label(frame_usuarios, text="No hay datos suficientes para mostrar gráficos", font=("Arial", 14)).pack(pady=50)
            
# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = EncuestaApp(root)
    root.mainloop()