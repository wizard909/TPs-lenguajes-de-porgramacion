import time

# =====================================================
# PROBLEMA 3: Gestionar lista de tareas (To-Do List)
# =====================================================

print("=============================================")
print("PROBLEMA 3: Gestionar lista de tareas")
print("=============================================\n")

# ---- PARADIGMA IMPERATIVO / PROCEDURAL (Python) ----
# Usa variables globales y modifica el estado directamente paso a paso.

lista_tareas_global = []

def agregar_tarea_proc(titulo, prioridad):
    lista_tareas_global.append({"titulo": titulo, "prioridad": prioridad, "completada": False})

def completar_tarea_proc(indice):
    lista_tareas_global[indice]["completada"] = True

def mostrar_pendientes_proc():
    print("--- Lista de pendientes (Procedural) ---")
    for tarea in lista_tareas_global:
        if not tarea["completada"]:
            print(f"  {tarea['titulo']} | Prioridad: {tarea['prioridad']}")
    print()

print("[Procedural - Python]")
agregar_tarea_proc("Comprar pan", 2)
agregar_tarea_proc("Estudiar Python", 1)
agregar_tarea_proc("Pagar servicios", 3)
mostrar_pendientes_proc()
completar_tarea_proc(1)
mostrar_pendientes_proc()


# ---- PARADIGMA ORIENTADO A OBJETOS (Python) ----
# La lógica y el estado están encapsulados dentro del objeto.
# El objeto "sabe" cómo gestionarse a sí mismo.

class Tarea:
    def __init__(self, titulo, prioridad):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

class ToDoList:
    def __init__(self):
        self.tareas = []

    def agregar(self, titulo, prioridad):
        self.tareas.append(Tarea(titulo, prioridad))

    def completar(self, indice):
        self.tareas[indice].completar()

    def mostrar_pendientes(self):
        pendientes = [t for t in self.tareas if not t.completada]
        print("--- Lista de pendientes ---")
        for t in sorted(pendientes, key=lambda x: x.prioridad):
            print(f"  {t.titulo} | Prioridad: {t.prioridad}")
        print()

print("[OO - Python]")
lista = ToDoList()
lista.agregar("Comprar pan", 2)
lista.agregar("Estudiar Python", 1)
lista.agregar("Pagar servicios", 3)
lista.mostrar_pendientes()
lista.completar(1)  # Completar "Estudiar Python"
lista.mostrar_pendientes()


# ---- PARADIGMA FUNCIONAL (Python puro) ----
# No hay objetos ni estado mutable. Las funciones reciben datos y
# retornan NUEVAS estructuras sin modificar las originales.

def agregar_tarea(lista, titulo, prioridad):
    return lista + [{"titulo": titulo, "prioridad": prioridad, "completada": False}]

def completar_tarea(lista, titulo):
    return [
        {**t, "completada": True} if t["titulo"] == titulo else t
        for t in lista
    ]

def mostrar_pendientes_func(lista):
    pendientes = list(filter(lambda t: not t["completada"], lista))
    ordenados = sorted(pendientes, key=lambda t: t["prioridad"])
    print("--- Lista de pendientes ---")
    for t in ordenados:
        print(f"  {t['titulo']} | Prioridad: {t['prioridad']}")
    print()

print("[Funcional - Python]")
tareas = []
tareas = agregar_tarea(tareas, "Comprar pan", 2)
tareas = agregar_tarea(tareas, "Estudiar Python", 1)
tareas = agregar_tarea(tareas, "Pagar servicios", 3)
mostrar_pendientes_func(tareas)
tareas = completar_tarea(tareas, "Estudiar Python")
mostrar_pendientes_func(tareas)
