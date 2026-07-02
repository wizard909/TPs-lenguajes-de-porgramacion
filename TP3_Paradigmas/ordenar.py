import time
import copy

# --- DATOS DE PRUEBA ---
# Una lista desordenada, replicada para hacer que Bubble Sort demore un poco
numeros_original = [4, 1, 8, 2, 10, 5, 9, 3, 7, 6] * 10

print("========================================")
print("PROBLEMA 2: Ordenar elementos en colección")
print("========================================\n")

# --- PARADIGMA PROCEDURAL / IMPERATIVO (Bubble Sort) ---
# Le decimos a la máquina paso a paso cómo mover los índices
def ordenar_procedural(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Swap manual usando una variable auxiliar temporal
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

copia_proc = copy.copy(numeros_original)
inicio = time.perf_counter()
res_proc = ordenar_procedural(copia_proc)
fin = time.perf_counter()
print(f"[Procedural] Bubble Sort | Tiempo: {(fin - inicio)*1000000:.2f} µs")


# --- PARADIGMA ORIENTADO A OBJETOS ---
# El objeto lista ya sabe cómo ordenarse mutando su propio estado
class ColeccionOrdenable:
    def __init__(self, elementos):
        self.elementos = elementos

    def ordenar(self):
        # Abstracción alta: delegamos el comportamiento al propio objeto
        self.elementos.sort()

mi_lista = ColeccionOrdenable(copy.copy(numeros_original))
inicio = time.perf_counter()
mi_lista.ordenar()
fin = time.perf_counter()
print(f"[Objetos]    list.sort() | Tiempo: {(fin - inicio)*1000000:.2f} µs")


# --- PARADIGMA FUNCIONAL ---
# Se usan funciones puras sin efectos secundarios. Retorna una NUEVA lista en lugar de mutar.
def ordenar_funcional(lista):
    return sorted(lista)

inicio = time.perf_counter()
res_func = ordenar_funcional(numeros_original)
fin = time.perf_counter()
print(f"[Funcional]  sorted()    | Tiempo: {(fin - inicio)*1000000:.2f} µs")
