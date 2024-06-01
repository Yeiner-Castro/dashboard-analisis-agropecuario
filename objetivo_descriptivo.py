import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import production_yield_by_department, filter_data_by_cultivo, filter_data_by_tipo_cultivo

def mostrar_objetivo_descriptivo(data):

    st.subheader('¿Cuál es la producción total y el rendimiento promedio por departamento?')
    
    dept_data = production_yield_by_department(data)
    st.write(dept_data)

    # Gráfico de dispersión para comparar Producción y Rendimiento
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(dept_data['Producción Total (t)'], dept_data['Rendimiento Promedio (t/ha)'], color='green')
    ax.set_title('Comparación de Producción Total y Rendimiento Promedio por Departamento')
    ax.set_xlabel('Producción Total (t)')
    ax.set_ylabel('Rendimiento Promedio (t/ha)')

    # Agregar etiquetas a los puntos
    for i, txt in enumerate(dept_data.index):
        ax.annotate(txt, (dept_data['Producción Total (t)'][i], dept_data['Rendimiento Promedio (t/ha)'][i]), fontsize=8, alpha=0.7)

    st.pyplot(fig)
    # Configuración de estilo de Seaborn
    sns.set(style="whitegrid")

    # Crear un DataFrame ordenado por Producción Total
    produccion_total_sorted = dept_data.sort_values(by='Producción Total (t)', ascending=False)

    # Graficar Producción Total por Departamento
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='Producción Total (t)', y=produccion_total_sorted.index, data=produccion_total_sorted, palette='viridis', ax=ax)
    ax.set_title('Producción Total por Departamento')
    ax.set_xlabel('Producción Total (t)')
    ax.set_ylabel('Departamento')

    st.pyplot(fig)

    # Crear un DataFrame ordenado por Rendimiento Promedio
    rendimiento_promedio_sorted = dept_data.sort_values(by='Rendimiento Promedio (t/ha)', ascending=False)

    # Graficar Rendimiento Promedio por Departamento
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='Rendimiento Promedio (t/ha)', y=rendimiento_promedio_sorted.index, data=rendimiento_promedio_sorted, palette='viridis', ax=ax)
    ax.set_title('Rendimiento Promedio por Departamento')
    ax.set_xlabel('Rendimiento Promedio (t/ha)')
    ax.set_ylabel('Departamento')

    st.pyplot(fig)

    st.subheader('¿Qué cultivos tienen la mayor área sembrada y cosechada por región?')

    # Obtener la lista de cultivos únicos
    cultivos = data['CULTIVO'].unique()

    # Crear un widget de selección para filtrar por cultivo
    cultivo = st.selectbox('Selecciona un cultivo:', cultivos, key='cultivo_area')

    # Función para actualizar la gráfica de Área Sembrada por Cultivo
    def update_area_sembrada(area_sembrada, cultivo):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=area_sembrada.values, y=area_sembrada.index, palette='viridis', ax=ax)
        ax.set_title(f'Área Sembrada por Departamento para el Cultivo: {cultivo}')
        ax.set_xlabel('Área Sembrada (ha)')
        ax.set_ylabel('Departamento')
        st.pyplot(fig)

    # Función para actualizar la gráfica de Área Cosechada por Cultivo
    def update_area_cosechada(area_cosechada, cultivo):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=area_cosechada.values, y=area_cosechada.index, palette='coolwarm', ax=ax)
        ax.set_title(f'Área Cosechada por Departamento para el Cultivo: {cultivo}')
        ax.set_xlabel('Área Cosechada (ha)')
        ax.set_ylabel('Departamento')
        st.pyplot(fig)

    # Actualizar las gráficas cuando se seleccione un nuevo cultivo
    if cultivo:
        area_sembrada, area_cosechada = filter_data_by_cultivo(data, cultivo)
        update_area_sembrada(area_sembrada, cultivo)
        update_area_cosechada(area_cosechada, cultivo)

    st.subheader('¿Cómo varía la producción y el rendimiento según el tipo de cultivo?')
    # Obtener la lista de tipos de cultivo únicos
    tipos_cultivo = data['GRUPO_DE_CULTIVO'].unique()

    # Crear un widget de selección para filtrar por tipo de cultivo
    tipo_cultivo = st.selectbox('Selecciona un tipo de cultivo:', tipos_cultivo, key='tipo_cultivo')

    # Función para actualizar la gráfica de Producción Total por Tipo de Cultivo
    def update_produccion_total(produccion_total, tipo_cultivo):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=produccion_total.values, y=produccion_total.index, palette='viridis', ax=ax)
        ax.set_title(f'Producción Total por Subgrupo de Cultivo: {tipo_cultivo}')
        ax.set_xlabel('Producción Total (t)')
        ax.set_ylabel('Subgrupo de Cultivo')
        st.pyplot(fig)

    # Función para actualizar la gráfica de Rendimiento Promedio por Tipo de Cultivo
    def update_rendimiento_promedio(rendimiento_promedio, tipo_cultivo):
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=rendimiento_promedio.values, y=rendimiento_promedio.index, palette='coolwarm', ax=ax)
        ax.set_title(f'Rendimiento Promedio por Subgrupo de Cultivo: {tipo_cultivo}')
        ax.set_xlabel('Rendimiento Promedio (t/ha)')
        ax.set_ylabel('Subgrupo de Cultivo')
        st.pyplot(fig)

    # Actualizar las gráficas cuando se seleccione un nuevo tipo de cultivo
    if tipo_cultivo:
        produccion_total, rendimiento_promedio = filter_data_by_tipo_cultivo(data, tipo_cultivo)
        update_produccion_total(produccion_total, tipo_cultivo)
        update_rendimiento_promedio(rendimiento_promedio, tipo_cultivo)
