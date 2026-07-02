# TP3 - Multiparadigma

**Alumno:** Facundo Cichero  
**Problema resuelto:** Buscar elemento en una colección.

En este trabajo práctico se resolvió un mismo problema utilizando diferentes paradigmas de programación para evidenciar las diferencias de enfoque y comparar sus características.

## Códigos Fuente
- El código para los paradigmas **Procedural**, **Orientado a Objetos** y **Funcional** se encuentra implementado en el archivo `buscar.py` (usando Python).
- El código para el paradigma **Lógico** se encuentra implementado en `buscar.pl` (usando Prolog).

---

## Tabla Comparativa de Criterios

| Criterio | Procedural / Imperativo | Orientado a Objetos | Funcional | Lógico |
|----------|-------------------------|---------------------|-----------|--------|
| **Claridad y legibilidad del código** | MEDIA | ALTA | BAJA | MEDIA |
| **Nivel de abstracción** | BAJA | ALTA | ALTA | ALTA |
| **Eficiencia y rendimiento** | ALTA | MEDIA | BAJA | MEDIA |
| **Facilidad de mantenimiento y escalabilidad** | MEDIA | ALTA | ALTA | MEDIA |
| **Expresión y concisión** | BAJA | ALTA | ALTA | ALTA |

---

### Breve justificación de los enfoques:

1. **Paradigma Procedural (Imperativo):** 
   Se utiliza un ciclo `for` para recorrer la lista preguntando en cada posición si se encuentra el valor, comprobando esto mediante una variable de estado booleana (`encontrado`). Se debe explicitar el "cómo" hacerlo paso a paso.
2. **Paradigma Orientado a Objetos:**
   El objeto lista (o colección) ya sabe cómo buscar si contiene un elemento en su interior. El comportamiento está encapsulado dentro del propio objeto, exponiendo solo un método `buscar()`.
3. **Paradigma Funcional:**
   Se utilizan funciones de orden superior (`filter`) que reciben otras funciones anónimas (`lambda`) como argumentos. Es un enfoque matemático y declarativo donde uno se concentra en definir "qué" es el resultado sin importar los ciclos internos.
4. **Paradigma Lógico:**
   Se define una regla matemática de pertenencia pura. El programador solo establece los hechos ("X pertenece a la lista si X es la cabeza") y las reglas lógicas ("X pertenece si está en el resto del cuerpo"). El motor interno de inferencia se hace cargo de buscar si se cumple la condición.
