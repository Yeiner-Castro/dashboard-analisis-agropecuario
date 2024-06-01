import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import calculate_correlations, calculate_comparacion_ciclo

def mostrar_objetivo_diagnostico(data):
    st.header('Objetivo Diagnóstico')
   
    st.subheader('¿Cuáles son los factores que afectan significativamente la producción y el rendimiento agrícola?')

    st.subheader('¿Cómo impactan los cambios en el área sembrada y cosechada en la producción y rendimiento?')

    sns.set(style="whitegrid")

    # Calcular las correlaciones
    correlaciones = calculate_correlations(data)

    # Visualización de las correlaciones
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlaciones, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    ax.set_title('Correlaciones entre Área Sembrada, Área Cosechada, Producción y Rendimiento')

    st.pyplot(fig)

    st.subheader('¿Existen diferencias significativas en producción y rendimiento entre cultivos de ciclo transitorio y permanentes?')

    # Calcular la comparación de producción y rendimiento entre cultivos de ciclo transitorio y permanente
    comparacion_ciclo = calculate_comparacion_ciclo(data)

    # Graficar Producción Promedio por Ciclo de Cultivo
    st.header('Producción Promedio por Ciclo de Cultivo')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(comparacion_ciclo['CICLO_DE_CULTIVO'], comparacion_ciclo['PRODUCCION'], color='skyblue')
    ax.set_title('Producción Promedio por Ciclo de Cultivo')
    ax.set_ylabel('Producción Promedio (t)')
    ax.set_xlabel('Ciclo de Cultivo')
    st.pyplot(fig)

    # Graficar Rendimiento Promedio por Ciclo de Cultivo
    st.header('Rendimiento Promedio por Ciclo de Cultivo')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(comparacion_ciclo['CICLO_DE_CULTIVO'], comparacion_ciclo['RENDIMIENTO'], color='orange')
    ax.set_title('Rendimiento Promedio por Ciclo de Cultivo')
    ax.set_ylabel('Rendimiento Promedio (t/ha)')
    ax.set_xlabel('Ciclo de Cultivo')
    st.pyplot(fig)
    