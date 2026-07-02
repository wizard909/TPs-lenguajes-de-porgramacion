import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    # 1. Carga de Datos
    # Se usa el archivo local tiobe_index_feb_2026.csv
    file_path = r'C:\Users\Wizardonimu\Documents\🎓Lenguajes de programacion\4. lenguajes de prigramacion\tiobe_index_feb_2026.csv'
    
    try:
        df = pd.read_csv(file_path)
        print(f"Datos cargados exitosamente. ({len(df)} registros encontrados)")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo CSV en la ruta especificada:\n{file_path}")
        return

    print("\n--- Datos Originales (Primeras 5 filas) ---")
    print(df.head())

    # 2. Limpieza de Datos (Data Cleaning)
    print("\n--- Limpiando Datos ---")
    
    # Rellenar valores nulos (NaN) en la columna Paradigm
    if 'Paradigm' in df.columns:
        df['Paradigm'] = df['Paradigm'].fillna('Unknown')
    
    # Normalizar strings (convertir a mayúsculas iniciales y quitar espacios extra)
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
    # Nos aseguramos de ordenar numéricamente por Rating_Pct
    top_10 = df.sort_values('Rating_Pct', ascending=False).head(10)
    sns.barplot(x='Rating_Pct', y='Language', data=top_10, palette="viridis")
    plt.title('Top 10 Lenguajes de Programación (Índice TIOBE)')
    plt.xlabel('Rating (%)')
    plt.ylabel('Lenguaje')
    plt.tight_layout()
    plt.savefig('top_lenguajes.png')
    print("\nGráfico 1 guardado como 'top_lenguajes.png'")

    # Gráfico 2: Distribución por Paradigmas en el dataset completo
    plt.figure(figsize=(8, 8))
    paradigm_counts = df['Paradigm'].value_counts()
    
    # Usamos colores pasteles
    plt.pie(paradigm_counts, labels=paradigm_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribución de Paradigmas')
    plt.axis('equal') # Equal aspect ratio
    plt.savefig('distribucion_paradigmas.png')
    print("Gráfico 2 guardado como 'distribucion_paradigmas.png'")

if __name__ == "__main__":
    main()
