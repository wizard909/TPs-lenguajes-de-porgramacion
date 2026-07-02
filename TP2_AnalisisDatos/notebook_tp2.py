import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Carga de Datos (Simulando la carga desde un CSV o DataFrame de Colab)
    # Suponemos que el dataset de TIOBE tiene columnas como: 'Language', 'Ratings', 'Change', 'Paradigm'
    try:
        df = pd.read_csv('tiobe_data.csv')
    except FileNotFoundError:
        print("Aviso: No se encontró 'tiobe_data.csv'. Se creará un DataFrame de ejemplo.")
        data = {
            'Language': ['Python', 'C', 'C++', 'Java', 'C#', 'JavaScript', 'SQL', 'Go', 'Scratch', 'Fortran'],
            'Ratings': [15.16, 10.97, 10.53, 8.88, 6.73, 3.17, 1.83, 1.34, 1.10, 1.05],
            'Paradigm': ['Multiparadigm', 'Procedural', 'OO/Procedural', 'OO', 'OO', 'Multiparadigm', 'Declarative', 'Concurrent', 'Visual', 'Procedural'],
            'Year_Created': [1991, 1972, 1985, 1995, 2000, 1995, 1974, 2009, 2007, 1957]
        }
        df = pd.DataFrame(data)

    print("--- Datos Originales ---")
    print(df.head())

    # 2. Limpieza de Datos (Data Cleaning)
    print("\n--- Limpiando Datos ---")
    
    # Rellenar valores nulos (NaN) en la columna Paradigm
    if 'Paradigm' in df.columns:
        df['Paradigm'] = df['Paradigm'].fillna('Unknown')
    
    # Normalizar strings (convertir a minúsculas y quitar espacios extra)
    df['Language'] = df['Language'].str.strip()
    df['Paradigm'] = df['Paradigm'].str.strip().str.title()
    
    # Eliminar duplicados si los hubiera
    df = df.drop_duplicates()
    
    print("Datos después de la limpieza:")
    print(df.info())

    # 3. Visualización de Datos (Data Visualization)
    sns.set_theme(style="whitegrid")

    # Gráfico 1: Top Lenguajes por Rating (Popularidad)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Ratings', y='Language', data=df.sort_values('Ratings', ascending=False).head(10), palette="viridis")
    plt.title('Top 10 Lenguajes de Programación (Índice TIOBE)')
    plt.xlabel('Rating (%)')
    plt.ylabel('Lenguaje')
    plt.tight_layout()
    plt.savefig('top_lenguajes.png')
    print("\nGráfico 1 guardado como 'top_lenguajes.png'")

    # Gráfico 2: Distribución por Paradigmas
    plt.figure(figsize=(8, 8))
    paradigm_counts = df['Paradigm'].value_counts()
    plt.pie(paradigm_counts, labels=paradigm_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribución de Paradigmas en el Top 10')
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('distribucion_paradigmas.png')
    print("Gráfico 2 guardado como 'distribucion_paradigmas.png'")

if __name__ == "__main__":
    main()
