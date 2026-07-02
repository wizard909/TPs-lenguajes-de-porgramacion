# TP2 - Análisis de Datos de Lenguajes de Programación

**Alumno:** Facundo Cichero  
**Tema:** Procesamiento, limpieza y visualización de un dataset sobre lenguajes de programación (Índice TIOBE).

En este Trabajo Práctico, se partió de un Google Colab (`Tiobe.ipynb`) que contenía métricas históricas de popularidad de los lenguajes de programación. El objetivo fue aplicar técnicas de Data Science para transformar los datos crudos en información útil.

## 1. Limpieza de Datos (Data Cleaning)
Se aplicaron las siguientes transformaciones al DataFrame usando Pandas:
- **Tratamiento de Nulos:** Se identificaron filas con valores vacíos (NaN) en la columna de Paradigmas y se las completó con el valor por defecto `'Unknown'`.
- **Normalización de texto:** Se utilizaron expresiones regulares y funciones de string (`str.strip()`, `str.title()`) para eliminar espacios en blanco al inicio y final, y estandarizar mayúsculas y minúsculas (ej. " python " -> "Python").
- **Eliminación de duplicados:** Se usó `drop_duplicates()` para limpiar registros ingresados múltiples veces.

## 2. Análisis y Visualización (Data Visualization)
Usando las librerías `matplotlib` y `seaborn`, se generaron gráficos para facilitar el análisis:

- **Gráfico de Barras (Top Lenguajes):** Permite ver visualmente la diferencia de porcentaje de popularidad (Rating) entre los 10 lenguajes más usados del índice TIOBE. Python y C mantienen la delantera histórica.
- **Gráfico de Torta (Paradigmas):** Muestra la distribución de mercado por tipo de paradigma. Se hace evidente que el paradigma Multiparadigma (Python, JavaScript, C++) y el Orientado a Objetos puro dominan enormemente el panorama actual frente a paradigmas declarativos o lógicos puros.

## Código Fuente
El código completo de la ejecución se encuentra consolidado en el archivo `notebook_tp2.py`.
