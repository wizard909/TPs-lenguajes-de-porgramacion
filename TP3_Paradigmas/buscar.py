def buscar_procedural(lista, objetivo):
    """Paradigma Procedural / Imperativo
    Uso un ciclo para recorrer la lista preguntando en cada posición si encuentro el
    valor, comprobando esto con una variable de estado."""
    encontrado = False
    for item in lista:
        if item == objetivo:
            encontrado = True
            break
    return encontrado

print("Procedural:", buscar_procedural([3, 7, 2, 9], 7))


class Coleccion:
    """Paradigma Orientado a Objetos
    El objeto 'Coleccion' ya sabe buscar si contiene algo. El comportamiento
    está encapsulado dentro del propio objeto."""
    def __init__(self, elementos):
        self.elementos = elementos

    def buscar(self, objetivo):
        return objetivo in self.elementos

mi_lista = Coleccion([3, 7, 2, 9])
print("POO:", mi_lista.buscar(7))


def buscar_funcional(lista, objetivo):
    """Paradigma Funcional
    Usando funciones que reciben otras funciones (Higher Order Functions).
    Es un estilo mucho más declarativo y matemático."""
    resultado = list(filter(lambda x: x == objetivo, lista))
    return len(resultado) > 0

print("Funcional:", buscar_funcional([3, 7, 2, 9], 7))
