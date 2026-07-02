# TP5 - Gramáticas del Lenguaje BRA

**Alumno:** Facundo Cichero  
**Lenguaje a analizar:** BRA

En este trabajo práctico se formalizan las reglas sintácticas del lenguaje `BRA` (presentado por la cátedra) en los tres principales formatos de especificación de gramáticas: BNF, EBNF y ABNF.

## Características de BRA extraídas de la fuente
- Bloque principal delimitado por `começo` y `final`.
- Sentencia de Asignación: `<ID> ::= <Expresión>;`
- Sentencias de I/O: `ler(lista de IDs);` y `escrever(lista de Expresiones);`
- Expresiones: Soportan `+`, `-`, constantes enteras, identificadores y paréntesis.
- Cierre de sentencias siempre con `;`.

---

## 1. Backus-Naur Form (BNF Original)
El formato original es el más estricto, no permite cuantificadores (como `*` o `+`) ni opcionalidad pura, obligando a usar recursividad explícita para las listas.

```bnf
<programa>         ::= "começo" <lista-sentencias> "final"
<lista-sentencias> ::= <sentencia> | <sentencia> <lista-sentencias>
<sentencia>        ::= <asignacion> | <entrada> | <salida>
<asignacion>       ::= <id> "::=" <expresion> ";"
<entrada>          ::= "ler" "(" <lista-id> ")" ";"
<salida>           ::= "escrever" "(" <lista-expr> ")" ";"
<lista-id>         ::= <id> | <id> "," <lista-id>
<lista-expr>       ::= <expresion> | <expresion> "," <lista-expr>
<expresion>        ::= <termino> | <expresion> "+" <termino> | <expresion> "-" <termino>
<termino>          ::= <id> | <constante> | "(" <expresion> ")"
<id>               ::= <letra> | <letra> <resto-id>
<resto-id>         ::= <caracter-valido> | <caracter-valido> <resto-id>
<constante>        ::= <digito> | <digito> <constante>
```

---

## 2. Extended Backus-Naur Form (EBNF)
Añade llaves `{ }` para indicar cero o más repeticiones (clausura de Kleene) y corchetes `[ ]` para opcionalidad, eliminando la necesidad de recursión para las listas.

```ebnf
Programa      = "começo", Sentencia, { Sentencia }, "final" ;
Sentencia     = Asignacion | Entrada | Salida ;
Asignacion    = ID, "::=", Expresion, ";" ;
Entrada       = "ler", "(", ID, { ",", ID }, ")", ";" ;
Salida        = "escrever", "(", Expresion, { ",", Expresion }, ")", ";" ;
Expresion     = Termino, { ("+" | "-"), Termino } ;
Termino       = ID | Constante | "(", Expresion, ")" ;
ID            = Letra, { Letra | Digito | "_" } ;
Constante     = Digito, { Digito } ;
```

---

## 3. Augmented Backus-Naur Form (ABNF)
Muy utilizado en estándares de Internet (RFCs). Usa repeticiones numéricas como `1*` (una o más veces) o `*3` (hasta 3 veces) y el símbolo `/` para alternativas.

```abnf
programa      = "começo" 1*sentencia "final"
sentencia     = asignacion / entrada / salida
asignacion    = id "::=" expresion ";"
entrada       = "ler" "(" id *( "," id ) ")" ";"
salida        = "escrever" "(" expresion *( "," expresion ) ")" ";"
expresion     = termino *( ("+" / "-") termino )
termino       = id / constante / "(" expresion ")"
; El ID de BRA tiene max 4 caracteres (1 letra inicial + hasta 3 validos)
id            = ALPHA *3(ALPHA / DIGIT / "_") 
constante     = 1*DIGIT
```

---

## Tabla 61C: Comparativa de Metasímbolos

| Operación / Significado | BNF Original | EBNF | ABNF |
|-------------------------|--------------|------|------|
| **Definición** | `::=` | `=` | `=` |
| **Alternativa (Opciones)** | `\|` | `\|` | `/` |
| **Concatenación** | (espacio en blanco) | `,` | (espacio en blanco) |
| **No Terminales** | `<nombre>` | `Nombre` | `nombre` |
| **Terminales** | `"texto"` | `"texto"` o `'texto'` | `"texto"` o `%xHEX` |
| **Opcionalidad (0 o 1 vez)**| *No soportado* (recursión) | `[ ]` | `[ ]` |
| **Repetición (0 o N veces)**| *No soportado* (recursión) | `{ }` | `*` |
| **Terminador de regla** | (salto de línea) | `;` | (salto de línea) |
