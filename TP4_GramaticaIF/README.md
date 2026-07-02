# TP4 - Gramática de Sentencias (IF)

**Alumno:** Facundo Cichero  
**Sentencia a analizar:** `if` (Condicional)

En este trabajo se realiza el recorrido gramatical completo ("poda de árbol") desde el **axioma principal** (raíz del programa) hasta llegar a la sentencia `if` y sus terminales. Se omitieron (podaron) las ramas alternativas que no conducen al `if` para enfocarse exclusivamente en el camino de derivación de esta estructura.

---

## 1. Java
**Fuente:** Oracle Java SE 7 Language Specification

**Camino de derivación (Poda desde el axioma):**
1. `<CompilationUnit>` (Axioma)
2. `→ <TypeDeclaration>`
3. `→ <ClassDeclaration>`
4. `→ <NormalClassDeclaration>`
5. `→ <ClassBody>`
6. `→ <ClassBodyDeclaration>`
7. `→ <ClassMemberDeclaration>`
8. `→ <MethodDeclaration>`
9. `→ <MethodBody>`
10. `→ <Block>`
11. `→ <BlockStatements>`
12. `→ <BlockStatement>`
13. `→ <Statement>`
14. `→ <StatementWithoutTrailingSubstatement>`
15. `→ <IfThenStatement>` | `<IfThenElseStatement>`

**Producción Final (Terminales):**
```bnf
<IfThenStatement> ::= "if" "(" <Expression> ")" <Statement>
<IfThenElseStatement> ::= "if" "(" <Expression> ")" <Statement> "else" <Statement>
```

---

## 2. Python
**Fuente:** Python 3 Language Reference

**Camino de derivación (Poda desde el axioma):**
1. `<file>` (Axioma)
2. `→ <statements>`
3. `→ <statement>`
4. `→ <compound_stmt>`
5. `→ <if_stmt>`

**Producción Final (Terminales):**
```bnf
<if_stmt> ::= "if" <named_expression> ":" <block> <elif_stmt> 
            | "if" <named_expression> ":" <block> [<else_block>]
<elif_stmt> ::= "elif" <named_expression> ":" <block> <elif_stmt> 
              | "elif" <named_expression> ":" <block> [<else_block>]
<else_block> ::= "else" ":" <block>
```

---

## 3. Kotlin
**Fuente:** Kotlin Language Reference

**Camino de derivación (Poda desde el axioma):**
1. `<kotlinFile>` (Axioma)
2. `→ <topLevelObject>`
3. `→ <declaration>`
4. `→ <functionDeclaration>`
5. `→ <functionBody>`
6. `→ <block>`
7. `→ <statements>`
8. `→ <statement>`
9. `→ <expression>`
10. `→ <ifExpression>`

**Producción Final (Terminales):**
```bnf
<ifExpression> ::= "if" "(" <expression> ")" <controlStructureBody> [ "else" <controlStructureBody> ]
```

---

## 4. C++
**Fuente:** ISO C++ Standard Grammar

**Camino de derivación (Poda desde el axioma):**
1. `<translation-unit>` (Axioma)
2. `→ <declaration-seq>`
3. `→ <declaration>`
4. `→ <function-definition>`
5. `→ <function-body>`
6. `→ <compound-statement>`
7. `→ <statement-seq>`
8. `→ <statement>`
9. `→ <selection-statement>`

**Producción Final (Terminales):**
```bnf
<selection-statement> ::= "if" [<constexpr>] "(" [<init-statement>] <condition> ")" <statement>
                        | "if" [<constexpr>] "(" [<init-statement>] <condition> ")" <statement> "else" <statement>
```

---

## 5. Go
**Fuente:** Go Programming Language Specification

**Camino de derivación (Poda desde el axioma):**
1. `<SourceFile>` (Axioma)
2. `→ <TopLevelDecl>`
3. `→ <FunctionDecl>`
4. `→ <FunctionBody>`
5. `→ <Block>`
6. `→ <StatementList>`
7. `→ <Statement>`
8. `→ <IfStmt>`

**Producción Final (Terminales):**
```bnf
<IfStmt> ::= "if" [ <SimpleStmt> ";" ] <Expression> <Block> [ "else" ( <IfStmt> | <Block> ) ]
```

---

## 6. C
**Fuente:** The syntax of C in Backus-Naur form

**Camino de derivación (Poda desde el axioma):**
1. `<translation-unit>` (Axioma)
2. `→ <external-declaration>`
3. `→ <function-definition>`
4. `→ <compound-statement>`
5. `→ <block-item-list>`
6. `→ <block-item>`
7. `→ <statement>`
8. `→ <selection-statement>`

**Producción Final (Terminales):**
```bnf
<selection-statement> ::= "if" "(" <expression> ")" <statement>
                        | "if" "(" <expression> ")" <statement> "else" <statement>
```

---

## Comparativa y Análisis Sintáctico

A partir del análisis de la bajada desde el axioma hasta las terminales, identificamos lo siguiente:

1. **Profundidad del Árbol (Axioma a Sentencia):**
   - Lenguajes puramente orientados a objetos como **Java** requieren un nivel de anidamiento profundo (Axioma -> Declaración de Clase -> Cuerpo de Clase -> Método -> Bloque -> Sentencia) porque el `if` no puede existir fuera del bloque de un método dentro de una clase.
   - Lenguajes como **Python o Go** permiten una bajada mucho más rápida y directa desde el archivo fuente al bloque de código.

2. **Paréntesis en la condición:** 
   - **Java, C, C++ y Kotlin** exigen obligatoriamente que la expresión a evaluar esté encerrada entre paréntesis `( )`.
   - **Python y Go** omiten los paréntesis, haciendo la sintaxis más limpia. 

3. **Bloques e Indentación:**
   - **Python** utiliza terminales de indentación y exige el token `:` para marcar el inicio del bloque.
   - El resto de los lenguajes (C, C++, Java, Kotlin, Go) derivan en un `Statement` o `Block` que tradicionalmente utiliza llaves `{ }`.

4. **Sentencias de inicialización previas:**
   - **C++ y Go** permiten una declaración/inicialización dentro del mismo `if` antes de la condición (`<init-statement>` y `<SimpleStmt>`).

---

## Tabla Comparativa de Gramáticas del IF

Esta tabla compara, de un vistazo, cómo cada lenguaje expresa formalmente la sentencia condicional.

| Característica | Java | Python | Kotlin | C++ | Go | C |
|---|---|---|---|---|---|---|
| **Axioma** | `<CompilationUnit>` | `<file>` | `<kotlinFile>` | `<translation-unit>` | `<SourceFile>` | `<translation-unit>` |
| **Pasos hasta el IF** | 15 | 5 | 10 | 9 | 8 | 8 |
| **Condición entre `( )`** | ✔️ Obligatorio | ❌ No | ✔️ Obligatorio | ✔️ Obligatorio | ❌ No | ✔️ Obligatorio |
| **Marcador de bloque** | `{ }` | `:` + indentación | `{ }` | `{ }` | `{ }` | `{ }` |
| **Permite `if-else`** | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| **Permite `elif/else if`** | `else if` anidado | `elif` nativo | `else if` anidado | `else if` anidado | `else if` anidado | `else if` anidado |
| **Inicialización en cabecera** | ❌ No | ❌ No | ❌ No | ✔️ `init-statement` | ✔️ `SimpleStmt` | ❌ No |
| **if como expresión** | ❌ Sentencia | ❌ Sentencia | ✔️ Expresión | ❌ Sentencia | ❌ Sentencia | ❌ Sentencia |
| **Terminal más cercana al axioma** | `<IfThenStatement>` | `<if_stmt>` | `<ifExpression>` | `<selection-statement>` | `<IfStmt>` | `<selection-statement>` |

