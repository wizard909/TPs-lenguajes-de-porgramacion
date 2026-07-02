import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import squarify

def main():
    print("========================================")
    print("TP2: Análisis Exploratorio de Datos (EDA)")
    print("========================================\n")

    # ---------------------------------------------------------
    # 1. CARGA DE DATOS
    # ---------------------------------------------------------
    file_path = r'C:\Users\Wizardonimu\Documents\🎓Lenguajes de programacion\4. lenguajes de prigramacion\tiobe_index_feb_2026.csv'
    
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Datos cargados correctamente! Filas y columnas: {df.shape}")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo CSV en:\n{file_path}")
        return

    # ---------------------------------------------------------
    # 2. PERFILADO Y LIMPIEZA DE DATOS
    # ---------------------------------------------------------
    print("\n--- Analizando nulos iniciales ---")
    print(df.isnull().sum())
    
    print("\n--- Limpieza de Datos ---")
    # Normalización de categorías a minúsculas
    df['Paradigm'] = df['Paradigm'].str.lower()
    df['Typing'] = df['Typing'].str.lower()
    
    # Eliminación de duplicados
    df = df.drop_duplicates()
    
    # Imputación de nulos
    df = df.fillna('N/A')
    
    # Remplazo de categorías inconsistentes
    df['Paradigm'] = df['Paradigm'].replace({'visual':'multi-paradigm'})
    
    print("✅ Limpieza completada. Datos limpios:")
    print(df.info())

    # ---------------------------------------------------------
    # 3. ANÁLISIS EXPLORATORIO DE DATOS (EDA) Y VISUALIZACIONES
    # ---------------------------------------------------------
    sns.set_theme(style="whitegrid")

    # Gráfico 1: Torta Clásico (Top 5 vs Otros)
    top_5 = df.head(5)
    otros_rating = df['Rating_Pct'][5:].sum()
    nombres = list(top_5['Language']) + ['Otros']
    ratings = list(top_5['Rating_Pct']) + [otros_rating]

    plt.figure(figsize=(8, 8))
    plt.pie(ratings, labels=nombres, autopct='%1.1f%%', startangle=140, 
            colors=sns.color_palette('pastel'), explode=[0.05]*6)
    plt.title('Cuota de Mercado: Top 5 Lenguajes vs Otros', fontsize=14, fontweight='bold')
    plt.savefig('grafico1_cuota_mercado.png')
    plt.close()

    # Gráfico 2: Torta Interactivo (Plotly HTML estático para guardar, en Colab es fig.show())
    typing_counts = df['Typing'].value_counts().reset_index()
    typing_counts.columns = ['Typing', 'Count']
    fig_typing = px.pie(typing_counts, values='Count', names='Typing',
                 title='Distribución por Sistema de Tipado (Estático vs Dinámico)',
                 color_discrete_sequence=px.colors.sequential.RdBu)
    fig_typing.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05, 0, 0])
    fig_typing.write_html('grafico2_tipado_interactivo.html')

    # Gráfico 3: Casos de Uso Principales
    usos_separados = df['Primary_Use'].str.split(',').explode().str.strip()
    usos_counts = usos_separados.value_counts().head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=usos_counts.values, y=usos_counts.index, hue=usos_counts.index, palette='viridis', legend=False)
    plt.title('Top 10 Industrias / Casos de Uso Principales', fontsize=14, fontweight='bold')
    plt.xlabel('Cantidad de Lenguajes que lo soportan')
    plt.ylabel('Área de Uso')
    plt.tight_layout()
    plt.savefig('grafico3_casos_uso.png')
    plt.close()

    # Gráfico 4: Popularidad vs Año de Creación
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='Year_Created', y='Rating_Pct', hue='Typing', s=120, palette='Set1', alpha=0.8)
    for i in range(df.shape[0]):
        if df['Rating_Pct'].iloc[i] > 2.0:
            plt.text(df['Year_Created'].iloc[i] + 1, df['Rating_Pct'].iloc[i], df['Language'].iloc[i], fontsize=10)
    plt.title('Popularidad (Rating) vs Año de Creación', fontsize=14, fontweight='bold')
    plt.xlabel('Año de Creación')
    plt.ylabel('Rating (%)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('grafico4_scatter_popularidad_anio.png')
    plt.close()

    # Gráfico 5: Tendencia de Mercado (Pie Subidas vs Bajadas)
    status_counts = df['Status'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(status_counts, labels=['Subieron de popularidad (↑)', 'Bajaron de popularidad (↓)'],
            autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff9999'], explode=[0.05, 0])
    plt.title('Tendencia del Mercado (Subidas vs Bajadas)', fontsize=14, fontweight='bold')
    plt.savefig('grafico5_tendencia_status.png')
    plt.close()

    print("✅ Gráficos guardados en el directorio local.")

    # ---------------------------------------------------------
    # 4. INSIGHTS (Conocimientos de valor)
    # ---------------------------------------------------------
    top_growth = df.sort_values("Change_Pct", ascending=False).head(5)
    top_decline = df.sort_values("Change_Pct").head(5)

    print("\n========================================")
    print("INSIGHTS FINALES")
    print("========================================")
    print("\n🚀 Lenguajes con mayor crecimiento:")
    print(top_growth[['Language','Change_Pct']].to_string(index=False))

    print("\n📉 Lenguajes con mayor caída:")
    print(top_decline[['Language','Change_Pct']].to_string(index=False))


if __name__ == "__main__":
    main()
