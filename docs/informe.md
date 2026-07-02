# INFORME FINAL - LENGUAJES DE PROGRAMACIÓN

---
**Universidad Nacional de Hurlingham (UNAHUR)**  
**Materia:** Lenguajes de Programación  
**Profesor:** Pablo Pandolfo  
**Alumno:** Facundo Cichero  
**Año:** 2026
---

<br><br>

## TRABAJO PRÁCTICO N°1 - Clasificación de los LP
**Consigna:** Clasificar 5 lenguajes según taxonomías específicas y agregar un dato de color.  
**Lenguajes asignados:** ReScript, Unison, Hylo, Inko, Gren.

### Tabla de Clasificación

| LENGUAJE | AÑO | PARADIGMA | NIVEL ABSTRACCIÓN | DOMINIO | TRADUCTOR | ALMACENAMIENTO | GENERACIÓN | ABORDAJE DE TAREA | LUGAR DE EJECUCIÓN | CONCURRENCIA | INTERACTIVIDAD | REALIZACIÓN VISUAL | PREDICCIÓN DE ESTADO | CARACTERÍSTICAS | DATO CURIOSO |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ReScript** | 2020 | Objetos, Funcional | Alto | Específico (web) | Compilado | Dinámico | 4° | Declarativos | Cliente | Concurrente | Orientado a eventos | Textual | Deterministas | Útiles | Facebook utilizó BuckleScript (antecesor de ReScript) para escribir el 50% de Messenger.com y herramientas de WhatsApp. |
| **Unison** | 2020 | Funcional | Alto | Específico (computación distribuida) | Compilado | Dinámico | 5° | Declarativos | Servidor | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | Cada función se identifica por el hash de su contenido. El código nunca se rompe por renombrar variables. |
| **Hylo (ex Val)** | 2022 | Imperativo, Objetos | Alto | Sistemas | Compilado | Algol | 4° | Operativos | Cliente | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | Creado por Dave Abrahams (diseñador de Swift). Su compilador está escrito en Swift. |
| **Inko** | 2015 | Objetos | Alto | General, Sistemas | Compilado | Dinámico | 4° | Operativos | Servidor | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | En 2023 se descartó su VM en Rust y fue reescrito para compilar a código máquina con LLVM. |
| **Gren** | 2022 | Funcional | Alto | General, Scripts | Compilado | Dinámico | 4° | Declarativos | Servidor, Cliente | No concurrente | Orientado a eventos | Textual | Deterministas | Útiles | Fork de Elm. Su nombre significa "rama" en noruego. Apunta a backend usando arrays inmutables. |

<br><br>

## TRABAJO PRÁCTICO N°2 - Análisis de Datos (Ciencia de Datos)
**Consigna:** Explorar y visualizar datos del Índice TIOBE para responder preguntas clave y extraer *Insights*.

### 1. Limpieza de Datos (Data Cleaning)
Para evitar que los gráficos se distorsionen ("no graficar por graficar"), se aplicó un perfilado y limpieza estricta usando Pandas:
- **Nulos:** Imputación con el valor `N/A`.
- **Inconsistencias Categóricas:** Todas las variables de Tipado y Paradigma pasaron a minúsculas (`str.lower()`) para evitar duplicaciones como "Object-Oriented" y "object-oriented".
- **Agrupamiento:** Se mapeó la categoría `visual` dentro de `multi-paradigm`.

### 2. Análisis Exploratorio (EDA)
Se generaron múltiples visualizaciones para entender la industria:
- **Top 5 Lenguajes:** Torta clásica agrupando del 6to al 28vo puesto bajo la categoría "Otros", demostrando el dominio masivo de Python y C.
- **Tipado:** Gráficos que comprueban la supremacía del tipado estático (64%) para desarrollos robustos.
- **Casos de uso:** Al separar las listas separadas por coma en `Primary_Use`, el barplot evidenció que "Web" y "Systems" son las industrias más voraces de lenguajes.

### 3. Insights
Analizando la métrica de variación `Change_Pct`, concluimos las tendencias actuales:
🚀 **Mayor crecimiento:** Python (+1.85%), Perl (+0.90%).
📉 **Mayor caída:** C (-5.41%), Java (-3.38%).

<br><br>

## TRABAJO PRÁCTICO N°3 - Multiparadigma
**Consigna:** Resolver 3 problemas utilizando los paradigmas Imperativo, OOP, Funcional y Lógico, incluyendo tablas comparativas. Se incluye justificación empírica midiendo tiempos de ejecución en Python.

### Problema 1: Buscar elemento en una colección
- **Imperativo:** Recorre explícitamente con `for` y variable `encontrado` (Alta eficiencia).
- **OOP:** Encapsula la lógica en un método `buscar()` dentro de una clase (Alto nivel de abstracción).
- **Funcional:** Usa lambdas puras y `filter`. (Menor eficiencia ya que evalúa toda la colección sin hacer break, pero Altísima expresividad/concisión en una línea).

### Problema 2: Ordenar elementos
- **Imperativo:** Se implementó `Bubble Sort` con doble ciclo anidado. Explica el **cómo** paso a paso (Baja legibilidad, Baja concisión).
- **OOP / Funcional:** Abstraen el algoritmo con llamadas a `sort()` (muta el objeto) y `sorted()` (retorna una nueva lista, sin efectos colaterales). Altísimo nivel de abstracción.

### Problema 3: Gestionar lista de tareas (To-Do List)
- **OOP:** Modela una clase `Tarea` (estado: completada) y `ToDoList` (estado: lista). 
- **Funcional:** Gestiona la misma lógica sin mutar estados, usando listas inmutables y diccionarios donde cada función retorna la colección modificada sin afectar la original.

<br><br>

## TRABAJO PRÁCTICO N°4 - Gramática de la sentencia IF
**Consigna:** Camino de derivación desde el axioma principal hasta los terminales.

**Comparativa Sintáctica Formal:**

| Característica | Java | Python | Kotlin | C++ | Go | C |
|---|---|---|---|---|---|---|
| **Axioma Principal** | `<CompilationUnit>` | `<file>` | `<kotlinFile>` | `<translation-unit>` | `<SourceFile>` | `<translation-unit>` |
| **Pasos hasta el IF** | 15 (Muy anidado) | 5 (Rápido) | 10 | 9 | 8 | 8 |
| **Condición entre `( )`** | ✔️ Obligatorio | ❌ No | ✔️ Obligatorio | ✔️ Obligatorio | ❌ No | ✔️ Obligatorio |
| **Marcador de bloque** | `{ }` | `:` + indentación | `{ }` | `{ }` | `{ }` | `{ }` |
| **if como expresión** | ❌ Sentencia | ❌ Sentencia | ✔️ Expresión | ❌ Sentencia | ❌ Sentencia | ❌ Sentencia |

<br><br>

## TRABAJO PRÁCTICO N°5 - Tabla 61C, Lenguaje BRA
**Consigna:** Formalizar la sintaxis del lenguaje BRA (P. Pandolfo) en BNF, EBNF y ABNF.

### Gramáticas Obtenidas
- **BNF:** Basado en `<programa> ::= "começo" <lista-sentencias> "final"`. Variables implícitas, máximo 4 letras.
- **EBNF:** Introduce cuantificadores `{ }` para bucles y eliminar la recursión por izquierda.
- **ABNF:** Formaliza la repetición con `1*` y las terminales directas con `/` en vez del `|` lógico.

### Tabla 61C: Comparativa de Metasímbolos

| Significado / Operación | BNF Original | EBNF | ABNF |
|-------------------------|--------------|------|------|
| **Definición** | `::=` | `=` | `=` |
| **Alternativa (O) lógica** | `\|` | `\|` | `/` |
| **No Terminales** | `<nombre>` | `Nombre` | `nombre` |
| **Opcionalidad**| No soportado | `[ ]` | `[ ]` |
| **Repetición (0 a N)**| No soportado | `{ }` | `*` |
