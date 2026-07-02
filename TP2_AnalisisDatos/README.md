# TP2 - Análisis de Datos de Lenguajes de Programación

**Alumno:** Facundo Cichero  
**Tema:** Ciencia de Datos con dataset Lenguajes de Programación (Índice TIOBE).

El objetivo de este Trabajo Práctico es explorar y visualizar los datos para responder preguntas clave y presentar insights de valor sobre el mercado de lenguajes de programación. Se partió de un entorno Google Colab, analizando el índice TIOBE.

**Enlace original al Colab (Base de trabajo):** [Ver en Google Colab](https://colab.research.google.com/drive/1j54L5F5twaPsUoUTJdBf0BqJ5qHUozp3?hl=es-es#scrollTo=g9I12k8L_pFr)

---

## 1. Perfilado y Limpieza de Datos
Antes de graficar, se analizaron inconsistencias en el dataset y se aplicaron las siguientes transformaciones con `pandas`:

1. **Detección de Nulos y Duplicados:** Se utilizó `isnull().sum()` para contar campos vacíos (ej. `Typing` tenía valores faltantes) y se rellenaron con `'N/A'` mediante `fillna()`. Se eliminaron posibles filas duplicadas con `drop_duplicates()`.
2. **Normalización Categórica:** Para evitar inconsistencias (ej. "Object-Oriented" vs "object-oriented"), se pasaron todas las categorías de las columnas `Paradigm` y `Typing` a minúsculas usando `str.lower()`.
3. **Reagrupamiento:** Se mapeó el paradigma `'visual'` hacia `'multi-paradigm'` para no distorsionar la distribución en los gráficos de torta.

---

## 2. Análisis Exploratorio (EDA) y Visualizaciones
Con los datos limpios, se utilizó `matplotlib`, `seaborn` y `plotly.express` para responder preguntas:

- **¿Quién domina el mercado? (Pie Chart Clásico):** Un gráfico agrupando el Top 5 de lenguajes frente al resto ("Otros"). Se visibiliza el dominio enorme de Python, C, C++, Java y C#.
- **¿Tipado estático o dinámico? (Plotly Interactivo):** La distribución indica que, aunque Python es dinámico, el 64% de los lenguajes principales utilizan tipado estático, dándole robustez a la industria empresarial.
- **¿Para qué se usan? (Barplot):** Haciendo un barrido (`explode`) de la columna de usos múltiples (`Primary_Use`), se observa que el Desarrollo Web, Systems (Sistemas/SO) y Enterprise (Empresarial) son las 3 industrias que más lenguajes demandan.
- **¿Importa la edad? (Scatterplot):** Al cruzar el *Año de Creación* con el *Rating*, vemos que lenguajes clásicos (C de 1972) se codean con lenguajes "nuevos" pero muy dominantes como Java (1995) o C# (2000).

---

## 3. Insights (Conclusiones de Valor)
Gracias a la columna de variación (`Change_Pct`), se identificaron dos tendencias importantísimas:

🚀 **Lenguajes con mayor crecimiento:**
1. **Python** (+1.85%)
2. Perl (+0.90%)
3. R (+0.80%)

📉 **Lenguajes con mayor caída:**
1. **C** (-5.41%)
2. Java (-3.38%)
3. C++ (-1.72%)

*Código fuente completo disponible en `notebook_tp2.py`.*
