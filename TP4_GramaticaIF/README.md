# TP4 - Gramática de Sentencias (IF)

**Alumno:** Facundo Cichero  
**Sentencia a analizar:** `if` (Condicional)

En este trabajo se extraen y reescriben las producciones gramaticales (desde el axioma de selección hasta los terminales) de la sentencia `if` en 6 lenguajes de programación, basándose en su documentación oficial.

## 1. Java
**Fuente:** Oracle Java SE 7 Language Specification

```bnf
<IfThenStatement> ::= "if" "(" <Expression> ")" <Statement>
<IfThenElseStatement> ::= "if" "(" <Expression> ")" <Statement> "else" <Statement>
```

## 2. Python
**Fuente:** Python 3 Language Reference

```bnf
<if_stmt> ::= "if" <named_expression> ":" <block> <elif_stmt> 
            | "if" <named_expression> ":" <block> [<else_block>]
<elif_stmt> ::= "elif" <named_expression> ":" <block> <elif_stmt> 
              | "elif" <named_expression> ":" <block> [<else_block>]
<else_block> ::= "else" ":" <block>
```

## 3. Kotlin
**Fuente:** Kotlin Language Reference

```bnf
<ifExpression> ::= "if" "(" <expression> ")" <controlStructureBody> [ "else" <controlStructureBody> ]
```

## 4. C++
**Fuente:** ISO C++ Standard Grammar

```bnf
<selection-statement> ::= "if" [<constexpr>] "(" [<init-statement>] <condition> ")" <statement>
                        | "if" [<constexpr>] "(" [<init-statement>] <condition> ")" <statement> "else" <statement>
```

## 5. Go
**Fuente:** Go Programming Language Specification

```bnf
<IfStmt> ::= "if" [ <SimpleStmt> ";" ] <Expression> <Block> [ "else" ( <IfStmt> | <Block> ) ]
```

## 6. C
**Fuente:** The syntax of C in Backus-Naur form

```bnf
<selection-statement> ::= "if" "(" <expression> ")" <statement>
                        | "if" "(" <expression> ")" <statement> "else" <statement>
```

---

## Comparativa y Análisis Sintáctico

A partir del análisis de las gramáticas, podemos identificar similitudes y diferencias clave en el diseño del condicional:

1. **Paréntesis en la condición:** 
   - **Java, C, C++ y Kotlin** exigen obligatoriamente que la expresión a evaluar esté encerrada entre paréntesis `( )`.
   - **Python y Go** omiten los paréntesis, haciendo la sintaxis más limpia. En Go se asume que la expresión termina antes de abrir la llave del bloque `{`. En Python, termina con los dos puntos `:`.

2. **Bloques e Indentación:**
   - **Python** utiliza terminales de indentación. No requiere llaves, pero exige explícitamente el token `:` para marcar el inicio del bloque.
   - El resto de los lenguajes (C, C++, Java, Kotlin, Go) derivan en un `Statement` o `Block` que tradicionalmente utiliza llaves `{ }`.

3. **Sentencias de inicialización previas:**
   - **C++ y Go** tienen una característica muy poderosa y única en sus producciones: permiten una declaración/inicialización dentro del mismo if antes de la condición (`<init-statement>` y `<SimpleStmt>`). Ejemplo en Go: `if v := math.Pow(x, n); v < lim { }`.

4. **Cláusula Else opcional:**
   - Todos los lenguajes tratan la cláusula `else` como un elemento opcional (marcado con `[ ]` en notación extendida o separado en otra regla).
   - Python incluye explícitamente el token `elif` para evitar el anidamiento profundo, mientras que en lenguajes como C o Java un "else if" es sintácticamente un `else` seguido de una nueva sentencia `if`.
