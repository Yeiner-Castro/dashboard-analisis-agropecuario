import streamlit as st
from utils import load_data, filter_data
from objetivo_descriptivo import mostrar_objetivo_descriptivo
from objetivo_exploratorio import mostrar_objetivo_exploratorio
from objetivo_diagnostico import mostrar_objetivo_diagnostico

# Título general
st.title('Dashboard Interactivo de Análisis Agrícola')

# Cargar datos
file_path = 'Datos_Formateados_Analisis_Agropecuario.csv'
data = load_data(file_path)

# Crear el menú de selección
menu = st.sidebar.selectbox('Selecciona el Objetivo', ['Objetivo Descriptivo', 'Objetivo Exploratorio', 'Objetivo Diagnóstico'])

if menu == 'Objetivo Descriptivo':
    mostrar_objetivo_descriptivo(data)

elif menu == 'Objetivo Exploratorio':
    mostrar_objetivo_exploratorio(data)

elif menu == 'Objetivo Diagnóstico':
    mostrar_objetivo_diagnostico(data)

