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

## TRABAJO PRÁCTICO N°2 - Análisis de Datos
**Consigna:** Análisis de datos referidos a los LP, limpieza y visualización mediante gráficos (Colab).

Se trabajó sobre un dataset basado en el Índice TIOBE y popularidad de lenguajes. El código completo en Python (`pandas`, `matplotlib`, `seaborn`) se encuentra en el repositorio de GitHub asociado. 

### Decisiones de Limpieza de Datos (Data Cleaning)
1. **Tratamiento de Nulos:** Los valores faltantes (`NaN`) en la columna de Paradigmas fueron identificados y rellenados con el valor por defecto `'Unknown'`.
2. **Normalización de Strings:** Se limpiaron espacios en blanco adicionales usando funciones de `strip()` y se normalizó el texto a título (`title()`) para evitar duplicaciones lógicas (ej: " python " y "Python").
3. **Descarte de Duplicados:** Se eliminaron las filas repetidas exactas mediante `drop_duplicates()`.

### Resultados de Visualización
- Se generaron gráficos de barra mostrando a C y Python liderando el ranking histórico.
- Se graficó una distribución porcentual (gráfico de torta) que evidenció cómo el paradigma Multiparadigma y Orientado a Objetos acaparan gran parte del uso de la industria frente al lógico puro o funcional.

<br><br>

## TRABAJO PRÁCTICO N°3 - Solución en Diferentes Paradigmas
**Consigna:** Resolver el problema "Buscar un elemento en una colección" utilizando distintos paradigmas y generar una tabla comparativa en base a 5 criterios.

### Códigos Desarrollados

**1. Paradigma Procedural / Imperativo (Python)**
```python
def buscar_procedural(lista, objetivo):
    encontrado = False
    for item in lista:
        if item == objetivo:
            encontrado = True
            break
    return encontrado
```

**2. Paradigma Orientado a Objetos (Python)**
```python
class Coleccion:
    def __init__(self, elementos):
        self.elementos = elementos

    def buscar(self, objetivo):
        return objetivo in self.elementos
```

**3. Paradigma Funcional (Python)**
```python
def buscar_funcional(lista, objetivo):
    resultado = list(filter(lambda x: x == objetivo, lista))
    return len(resultado) > 0
```

**4. Paradigma Lógico (Prolog)**
```prolog
pertenece(X, [X|_]).
pertenece(X, [_|Cola]) :- pertenece(X, Cola).
```

### Tabla Comparativa de Criterios

| Criterio | Procedural | Orientado a Objetos | Funcional | Lógico |
|---|---|---|---|---|
| **Claridad y legibilidad del código** | MEDIA | ALTA | BAJA | MEDIA |
| **Nivel de abstracción** | BAJA | ALTA | ALTA | ALTA |
| **Eficiencia y Rendimiento** | ALTA | MEDIA | BAJA | MEDIA |
| **Facilidad de mantenimiento** | MEDIA | ALTA | ALTA | MEDIA |
| **Expresión y concisión** | BAJA | ALTA | ALTA | ALTA |

<br><br>

## TRABAJO PRÁCTICO N°4 - Gramática de la sentencia IF
**Consigna:** Identificar la gramática del `if` en distintos lenguajes proporcionados desde sus fuentes oficiales, reescribiendo las producciones desde el axioma hasta los terminales.

**1. Java** (JLS SE7)
```bnf
<IfThenStatement> ::= "if" "(" <Expression> ")" <Statement>
<IfThenElseStatement> ::= "if" "(" <Expression> ")" <Statement> "else" <Statement>
```

**2. Python** (Language Reference 3)
```bnf
<if_stmt> ::= "if" <named_expression> ":" <block> <elif_stmt> 
            | "if" <named_expression> ":" <block> [<else_block>]
```

**3. Kotlin** (Language Reference)
```bnf
<ifExpression> ::= "if" "(" <expression> ")" <controlStructureBody> [ "else" <controlStructureBody> ]
```

**4. C++** (ISO Standard)
```bnf
<selection-statement> ::= "if" [<constexpr>] "(" [<init-statement>] <condition> ")" <statement> [ "else" <statement> ]
```

**5. Go** (Language Specification)
```bnf
<IfStmt> ::= "if" [ <SimpleStmt> ";" ] <Expression> <Block> [ "else" ( <IfStmt> | <Block> ) ]
```

**6. C** (BNF Syntax)
```bnf
<selection-statement> ::= "if" "(" <expression> ")" <statement> [ "else" <statement> ]
```

**Análisis Comparativo:** Java, C, C++ y Kotlin exigen que la expresión esté entre paréntesis, mientras que Go y Python no. Python es el único que marca los bloques mediante indentación obligatoria (marcada con el token `:`). C++ y Go permiten declarar una variable de inicialización en la misma cabecera del condicional.

<br><br>

## TRABAJO PRÁCTICO N°5 - Tabla 61C, Lenguaje BRA
**Consigna:** Formalizar la sintaxis del lenguaje BRA de la cátedra utilizando BNF, EBNF y ABNF, construyendo luego la tabla comparativa de metasímbolos 61C.

### Gramáticas

**1. BNF Original**
```bnf
<programa>         ::= "começo" <lista-sentencias> "final"
<lista-sentencias> ::= <sentencia> | <sentencia> <lista-sentencias>
<sentencia>        ::= <asignacion> | <entrada> | <salida>
<asignacion>       ::= <id> "::=" <expresion> ";"
<entrada>          ::= "ler" "(" <lista-id> ")" ";"
<salida>           ::= "escrever" "(" <lista-expr> ")" ";"
<lista-id>         ::= <id> | <id> "," <lista-id>
<lista-expr>       ::= <expresion> | <expresion> "," <lista-expr>
```

**2. EBNF (Extended)**
```ebnf
Programa      = "começo", Sentencia, { Sentencia }, "final" ;
Sentencia     = Asignacion | Entrada | Salida ;
Asignacion    = ID, "::=", Expresion, ";" ;
Entrada       = "ler", "(", ID, { ",", ID }, ")", ";" ;
Salida        = "escrever", "(", Expresion, { ",", Expresion }, ")", ";" ;
```

**3. ABNF (Augmented)**
```abnf
programa      = "começo" 1*sentencia "final"
sentencia     = asignacion / entrada / salida
asignacion    = id "::=" expresion ";"
entrada       = "ler" "(" id *( "," id ) ")" ";"
salida        = "escrever" "(" expresion *( "," expresion ) ")" ";"
```

### Tabla 61C: Comparativa de Metasímbolos

| Significado / Operación | BNF Original | EBNF | ABNF |
|-------------------------|--------------|------|------|
| **Definición** | `::=` | `=` | `=` |
| **Alternativa (O) lógica** | `\|` | `\|` | `/` |
| **Concatenación** | (espacio en blanco) | `,` | (espacio en blanco) |
| **No Terminales** | `<nombre>` | `Nombre` | `nombre` |
| **Terminales** | `"texto"` | `"texto"` o `'texto'` | `"texto"` o `%xHEX` |
| **Opcionalidad (0 o 1 vez)**| No soportado (requiere recursión) | `[ ]` | `[ ]` |
| **Repetición (0 o Múltiples)**| No soportado (requiere recursión) | `{ }` | `*` |
| **Repetición (1 o Múltiples)**| No soportado | No soportado directo | `1*` |
| **Fin de la regla** | (salto de línea) | `;` | (salto de línea) |
