import time

# --- DATOS DE PRUEBA ---
# Creamos una lista un poco más grande para que la medición de tiempo sea apreciable
numeros = [3, 7, 2, 9, 15, 8, 42, 99, 101, 7, 12] * 100 
objetivo = 42

print("========================================")
print("PROBLEMA 1: Buscar elemento en colección")
print("========================================\n")

# --- PARADIGMA PROCEDURAL / IMPERATIVO ---
def buscar_procedural(lista, objetivo):
    encontrado = False
    for item in lista:
        if item == objetivo:
            encontrado = True
            break
    return encontrado

inicio = time.perf_counter()
res_proc = buscar_procedural(numeros, objetivo)
fin = time.perf_counter()
print(f"[Procedural] Resultado: {res_proc} | Tiempo: {(fin - inicio)*1000000:.2f} µs")


# --- PARADIGMA ORIENTADO A OBJETOS ---
class Coleccion:
    def __init__(self, elementos):
        self.elementos = elementos

    def buscar(self, objetivo):
        return objetivo in self.elementos

mi_lista = Coleccion(numeros)
inicio = time.perf_counter()
res_oo = mi_lista.buscar(objetivo)
fin = time.perf_counter()
print(f"[Objetos]    Resultado: {res_oo} | Tiempo: {(fin - inicio)*1000000:.2f} µs")


# --- PARADIGMA FUNCIONAL ---
def buscar_funcional(lista, objetivo):
    # Uso de filter y funciones lambda puras
    resultado = list(filter(lambda x: x == objetivo, lista))
    return len(resultado) > 0

inicio = time.perf_counter()
res_func = buscar_funcional(numeros, objetivo)
fin = time.perf_counter()
print(f"[Funcional]  Resultado: {res_func} | Tiempo: {(fin - inicio)*1000000:.2f} µs")
