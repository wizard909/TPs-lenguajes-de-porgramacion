# TP3 - Resolver problemas en múltiples paradigmas

**Alumno:** Facundo Cichero

Se resuelven 3 problemas utilizando los paradigmas **Imperativo/Procedural**, **Orientado a Objetos**, **Funcional** y **Lógico** (Prolog), con el fin de comparar sus características, nivel de abstracción y eficiencia.

---

## Tabla comparativa de paradigmas

La tabla utiliza como lenguajes de implementación:
- **Imperativo:** Python (con variables y ciclos explícitos)
- **Orientado a Objetos (OOP):** Python (moderno y versátil)
- **Funcional:** Python (funciones puras, `filter`, `sorted`, `map`)
- **Lógico:** Prolog (declarativo de inferencia)

---

## Problema 1: Buscar elemento en una colección

**Código:** [`buscar.py`](./buscar.py) y [`buscar.pl`](./buscar.pl)

### Imperativo
```python
def buscar_procedural(lista, objetivo):
    encontrado = False
    for item in lista:      # ciclo explícito
        if item == objetivo:
            encontrado = True
            break
    return encontrado
```

### Orientado a Objetos
```python
class Coleccion:
    def __init__(self, elementos):
        self.elementos = elementos

    def buscar(self, objetivo):
        return objetivo in self.elementos  # comportamiento encapsulado

c = Coleccion([3, 7, 2, 9])
print(c.buscar(7))
```

### Funcional
```python
def buscar_funcional(lista, objetivo):
    return len(list(filter(lambda x: x == objetivo, lista))) > 0
```

### Lógico (Prolog)
```prolog
pertenece(X, [X|_]).
pertenece(X, [_|Cola]) :- pertenece(X, Cola).
```

### Tabla comparativa — Problema 1 (Buscar)

| CRITERIOS | Imperativo (Python) | OOP (Python) | Funcional (Python) | Lógico (Prolog) |
|---|---|---|---|---|
| 1. Claridad y legibilidad | ALTA | ALTA | MEDIA | MEDIA |
| 2. Nivel de abstracción | BAJO | MEDIO-ALTO | ALTO | ALTO |
| 3. Eficiencia y rendimiento | ALTA | ALTA | MEDIA* | MEDIA |
| 4. Facilidad de mantenimiento | MEDIA | ALTA | MEDIA | MEDIA |
| 5. Expresividad y concisión | MEDIA | ALTA | ALTA | ALTA |

> \* El paradigma funcional con `filter` recorre **toda la lista** sin hacer `break`, siendo menos eficiente para listas grandes.

---

## Problema 2: Ordenar elementos en una colección

**Código:** [`ordenar.py`](./ordenar.py)

### Imperativo — Bubble Sort
```python
def ordenar_procedural(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista
```
> Le decimos a la máquina exactamente **cómo** mover cada elemento (doble `for`, variable auxiliar, comparación manual).

### Orientado a Objetos
```python
class ColeccionOrdenable:
    def __init__(self, elementos):
        self.elementos = elementos

    def ordenar(self):
        self.elementos.sort()  # el objeto gestiona su propio estado
```

### Funcional
```python
def ordenar_funcional(lista):
    return sorted(lista)  # retorna NUEVA lista sin modificar la original
```

### Tabla comparativa — Problema 2 (Ordenar)

| CRITERIOS | Imperativo | OOP | Funcional | Lógico |
|---|---|---|---|---|
| 1. Claridad y legibilidad | BAJA | BAJA | ALTA | MEDIA |
| 2. Nivel de abstracción | BAJO | ALTO | ALTO | ALTO |
| 3. Eficiencia y rendimiento | MEDIA | ALTA | ALTA | MEDIA |
| 4. Facilidad de mantenimiento | MEDIA | ALTA | ALTA | MEDIA |
| 5. Expresividad y concisión | BAJA | MEDIA | ALTA | MEDIA |

---

## Problema 3: Gestionar lista de tareas (To-Do List)

**Código:** [`tareas.py`](./tareas.py)

### Imperativo (Procedural)
```python
lista_tareas = []

def agregar_tarea(titulo, prioridad):
    lista_tareas.append({"titulo": titulo, "prioridad": prioridad, "completada": False})

def completar_tarea(indice):
    lista_tareas[indice]["completada"] = True
```

### Orientado a Objetos
```python
class Tarea:
    def __init__(self, titulo, prioridad):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

class ToDoList:
    def agregar(self, titulo, prioridad):
        self.tareas.append(Tarea(titulo, prioridad))

    def mostrar_pendientes(self):
        pendientes = [t for t in self.tareas if not t.completada]
        for t in sorted(pendientes, key=lambda x: x.prioridad):
            print(f"{t.titulo} | Prioridad: {t.prioridad}")
```

### Funcional (Python)
```python
# Todas las funciones reciben y retornan datos sin mutar el estado original
def agregar_tarea(lista, titulo, prioridad):
    return lista + [{"titulo": titulo, "prioridad": prioridad, "completada": False}]

def completar_tarea(lista, titulo):
    return [{**t, "completada": True} if t["titulo"] == titulo else t for t in lista]
```

### Lógico (Prolog)
```prolog
:- dynamic tarea/3. % tarea(Titulo, Prioridad, Estado)

agregar_tarea(Titulo, Prioridad) :-
    assertz(tarea(Titulo, Prioridad, pendiente)).

completar_tarea(Titulo) :-
    retract(tarea(Titulo, Prioridad, pendiente)),
    assertz(tarea(Titulo, Prioridad, completada)).
```

### Tabla comparativa — Problema 3 (Tareas)

| CRITERIOS | Imperativo | OOP | Funcional | Lógico |
|---|---|---|---|---|
| 1. Claridad y legibilidad | MEDIA | ALTA | MEDIA | MEDIA |
| 2. Nivel de abstracción | BAJO | ALTO | ALTO | ALTO |
| 3. Eficiencia y rendimiento | MEDIA | MEDIA | MEDIA | MEDIA |
| 4. Facilidad de mantenimiento | BAJA | ALTA | ALTA | MEDIA |
| 5. Expresividad y concisión | BAJA | ALTA | MEDIA | MEDIA |

---

## Conclusión Global: Variabilidad según el problema

Al cruzar los datos de las tres tablas comparativas, surge un *Insight* fundamental: **El desempeño, legibilidad y conveniencia de un paradigma no son absolutos, sino que mutan drásticamente según la naturaleza del problema a resolver**.

1. **El costo de la abstracción Funcional:** Para un problema matemático o declarativo (como ordenar una lista en el *Problema 2*), el paradigma funcional brilla por su concisión asombrosa (`sorted(lista)` en 1 línea) con Altísima Legibilidad. Sin embargo, cuando lo forzamos a resolver problemas de estado y manipulación transaccional (como marcar una tarea como completada en una To-Do list iterativa en el *Problema 3*), la inmutabilidad de datos vuelve el código verboso y complejo (Media Claridad).
2. **La robustez del Orientado a Objetos (OOP):** El OOP muestra su máximo esplendor en dominios que simulan la vida real (el *Problema 3* de Tareas). Encapsular estado y comportamiento en una clase `ToDoList` eleva brutalmente la facilidad de mantenimiento y legibilidad. Sin embargo, usar todo el *overhead* de una clase instanciada solo para hacer una búsqueda lineal (*Problema 1*) resulta en una sobreingeniería innecesaria.
3. **El poder (y el peligro) Imperativo:** Es imbatible en eficiencia cruda para el control a bajo nivel (como salir de un ciclo `for` inmediatamente con un `break` en el *Problema 1*), pero sufre un declive fatal en escalabilidad y legibilidad cuando el problema crece (como el doble ciclo incomprensible de un `Bubble Sort` en el *Problema 2*).

En conclusión, ningún paradigma domina todas las métricas. La elección arquitectónica debe estar atada al caso de uso (dominio del problema) y no al fanatismo por un lenguaje.
