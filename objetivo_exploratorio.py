import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import calculate_variaciones_estacionales, calculate_trendline, calculate_tendencias, calculate_std_produccion, calculate_std_rendimiento

def mostrar_objetivo_exploratorio(data):
    st.header('Objetivo Exploratorio')

    st.subheader('¿Existen patrones estacionales en la producción y el rendimiento agrícola?')
    variaciones_estacionales = calculate_variaciones_estacionales(data)

    # Graficar Producción Promedio por Período
    st.header('Producción Promedio por Período')
    fig, ax = plt.subplots(figsize=(12, 6))
    variaciones_estacionales['Producción Promedio (t)'].plot(kind='line', marker='o', color='skyblue', ax=ax)
    ax.set_title('Producción Promedio por Período')
    ax.set_ylabel('Producción Promedio (t)')
    ax.set_xlabel('Período')
    ax.set_xticks(range(len(variaciones_estacionales.index)))
    ax.set_xticklabels(variaciones_estacionales.index, rotation=90)
    st.pyplot(fig)

    # Graficar Rendimiento Promedio por Período
    fig, ax = plt.subplots(figsize=(12, 6))
    variaciones_estacionales['Rendimiento Promedio (t/ha)'].plot(kind='line', marker='o', color='orange', ax=ax)
    ax.set_title('Rendimiento Promedio por Período')
    ax.set_ylabel('Rendimiento Promedio (t/ha)')
    ax.set_xlabel('Período')
    ax.set_xticks(range(len(variaciones_estacionales.index)))
    ax.set_xticklabels(variaciones_estacionales.index, rotation=90)
    st.pyplot(fig)

    st.subheader('¿Cuáles son las tendencias de producción y rendimiento en los diferentes departamentos a lo largo de los años?')
    
    # Calcular las tendencias temporales en producción y rendimiento
    tendencias_departamento = calculate_tendencias(data)

    # Configuración de estilo de Seaborn
    sns.set(style="whitegrid")

    # Obtener la lista de departamentos únicos
    departamentos = data['DEPARTAMENTO'].unique()

    # Crear un widget de selección múltiple para filtrar por departamento
    departamento = st.multiselect('Selecciona uno o más departamentos:', departamentos, default=departamentos[0])

    # Función para actualizar la gráfica de Producción Total por Departamento
    def update_produccion(departamento):
        filtered_data = tendencias_departamento[tendencias_departamento['DEPARTAMENTO'].isin(departamento)].pivot(index='AÑO', columns='DEPARTAMENTO', values='PRODUCCION').fillna(0)
        fig, ax = plt.subplots(figsize=(14, 8))
        filtered_data.plot(kind='line', marker='o', ax=ax)
        ax.set_title('Tendencias de Producción por Año y Departamento')
        ax.set_xlabel('Año')
        ax.set_ylabel('Producción Total (t)')
        ax.grid(True)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

    # Función para actualizar la gráfica de Rendimiento Promedio por Departamento
    def update_rendimiento(departamento):
        filtered_data = tendencias_departamento[tendencias_departamento['DEPARTAMENTO'].isin(departamento)].pivot(index='AÑO', columns='DEPARTAMENTO', values='RENDIMIENTO').fillna(0)
        fig, ax = plt.subplots(figsize=(14, 8))
        filtered_data.plot(kind='line', marker='o', ax=ax)
        ax.set_title('Tendencias de Rendimiento por Año y Departamento')
        ax.set_xlabel('Año')
        ax.set_ylabel('Rendimiento Promedio (t/ha)')
        ax.grid(True)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

    # Actualizar las gráficas cuando se seleccionen nuevos departamentos
    if departamento:
        update_produccion(departamento)
        update_rendimiento(departamento)
    
    st.subheader('¿Qué regiones muestran mayores variaciones en la producción y rendimiento agrícola?')
    # Configuración de estilo de Seaborn
    sns.set(style="whitegrid")

    # Calcular la desviación estándar de la producción por departamento
    std_produccion = calculate_std_produccion(data)

    # Graficar Desviación Estándar de la Producción por Región
    st.header('Desviación Estándar de Producción por Región')
    fig, ax = plt.subplots(figsize=(14, 8))
    std_produccion.sort_values().plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Desviación Estándar de Producción por Región')
    ax.set_ylabel('Desviación Estándar de Producción (t)')
    ax.set_xlabel('Departamento')
    ax.set_xticks(range(len(std_produccion.index)))
    ax.set_xticklabels(std_produccion.index, rotation=90)
    ax.grid(True)
    st.pyplot(fig)

    # Calcular la desviación estándar del rendimiento por departamento
    std_rendimiento = calculate_std_rendimiento(data)

    # Graficar Desviación Estándar del Rendimiento por Región
    st.header('Desviación Estándar del Rendimiento por Región')
    fig, ax = plt.subplots(figsize=(14, 8))
    std_rendimiento.sort_values().plot(kind='bar', color='orange', ax=ax)
    ax.set_title('Desviación Estándar del Rendimiento por Región')
    ax.set_ylabel('Desviación Estándar del Rendimiento (t/ha)')
    ax.set_xlabel('Departamento')
    ax.set_xticks(range(len(std_rendimiento.index)))
    ax.set_xticklabels(std_rendimiento.index, rotation=90)
    ax.grid(True)
    st.pyplot(fig)
