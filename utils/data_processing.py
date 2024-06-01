import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Carga los datos desde un archivo CSV.
    Retorna un DataFrame de pandas con los datos.
    
    Parameters:
    - filepath: Ruta al archivo CSV.
    """
    data = pd.read_csv(filepath)
    return data

def filter_data(data, categories=None):
    """
    Filtra los datos según las categorías especificadas.

    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    - categories: Lista de categorías para filtrar los datos. Si es None, no se aplica ningún filtro.

    Returns:
    - DataFrame de pandas con los datos filtrados.
    """
    if categories:
        data = data[data['category'].isin(categories)]
    return data

import pandas as pd

def load_data(filepath):
    """
    Carga los datos desde un archivo CSV.
    Retorna un DataFrame de pandas con los datos.
    
    Parameters:
    - filepath: Ruta al archivo CSV.
    """
    data = pd.read_csv(filepath)
    return data

def production_yield_by_department(data):
    """
    Calcula la producción total y el rendimiento promedio por departamento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - DataFrame de pandas con la producción total y el rendimiento promedio por departamento.
    """
    produccion_departamento = data.groupby('DEPARTAMENTO')['PRODUCCION'].sum()
    rendimiento_departamento = data.groupby('DEPARTAMENTO')['RENDIMIENTO'].mean()

    produccion_rendimiento_departamento = pd.DataFrame({
        'Producción Total (t)': produccion_departamento,
        'Rendimiento Promedio (t/ha)': rendimiento_departamento
    })
    
    return produccion_rendimiento_departamento

def filter_data_by_cultivo(data, cultivo):
    """
    Filtra los datos por cultivo y calcula el área sembrada y cosechada por departamento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    - cultivo: Cultivo por el cual se desea filtrar los datos.
    
    Returns:
    - area_sembrada: DataFrame de pandas con el área sembrada por departamento.
    - area_cosechada: DataFrame de pandas con el área cosechada por departamento.
    """
    filtered_data = data[data['CULTIVO'] == cultivo]
    area_sembrada = filtered_data.groupby('DEPARTAMENTO')['AREA_SEMBRADA'].sum().sort_values(ascending=False)
    area_cosechada = filtered_data.groupby('DEPARTAMENTO')['AREA_COSECHADA'].sum().sort_values(ascending=False)
    
    return area_sembrada, area_cosechada

def filter_data_by_tipo_cultivo(data, tipo_cultivo):
    """
    Filtra los datos por tipo de cultivo y calcula la producción total y el rendimiento promedio por subgrupo de cultivo.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    - tipo_cultivo: Tipo de cultivo por el cual se desea filtrar los datos.
    
    Returns:
    - produccion_total: DataFrame de pandas con la producción total por subgrupo de cultivo.
    - rendimiento_promedio: DataFrame de pandas con el rendimiento promedio por subgrupo de cultivo.
    """
    filtered_data = data[data['GRUPO_DE_CULTIVO'] == tipo_cultivo]
    produccion_total = filtered_data.groupby('SUBGRUPO_DE_CULTIVO')['PRODUCCION'].sum().sort_values(ascending=False)
    rendimiento_promedio = filtered_data.groupby('SUBGRUPO_DE_CULTIVO')['RENDIMIENTO'].mean().sort_values(ascending=False)
    
    return produccion_total, rendimiento_promedio

def calculate_tendencias(data):
    """
    Calcula las tendencias temporales en producción y rendimiento por departamento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - tendencias_departamento: DataFrame de pandas con las tendencias de producción y rendimiento por año y departamento.
    """
    data['AÑO'] = pd.to_datetime(data['AÑO'], format='%Y').dt.year
    tendencias_departamento = data.groupby(['AÑO', 'DEPARTAMENTO']).agg({
        'PRODUCCION': 'sum',
        'RENDIMIENTO': 'mean'
    }).reset_index()
    
    return tendencias_departamento

def calculate_std_produccion(data):
    """
    Calcula la desviación estándar de la producción por departamento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - std_produccion: Series de pandas con la desviación estándar de la producción por departamento.
    """
    std_produccion = data.groupby('DEPARTAMENTO')['PRODUCCION'].std()
    return std_produccion

def calculate_std_rendimiento(data):
    """
    Calcula la desviación estándar del rendimiento por departamento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - std_rendimiento: Series de pandas con la desviación estándar del rendimiento por departamento.
    """
    std_rendimiento = data.groupby('DEPARTAMENTO')['RENDIMIENTO'].std()
    return std_rendimiento

def calculate_correlations(data):
    """
    Calcula las correlaciones entre área sembrada, área cosechada, producción y rendimiento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - correlaciones: DataFrame de pandas con las correlaciones entre las variables seleccionadas.
    """
    correlaciones = data[['AREA_SEMBRADA', 'AREA_COSECHADA', 'PRODUCCION', 'RENDIMIENTO']].corr()
    return correlaciones

def calculate_comparacion_ciclo(data):
    """
    Compara la producción y el rendimiento entre cultivos de ciclo transitorio y permanente.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - comparacion_ciclo: DataFrame de pandas con la producción y el rendimiento promedio por ciclo de cultivo.
    """
    comparacion_ciclo = data.groupby('CICLO_DE_CULTIVO').agg({
        'PRODUCCION': 'mean',
        'RENDIMIENTO': 'mean'
    }).reset_index()
    return comparacion_ciclo

def calculate_variaciones_estacionales(data):
    """
    Calcula las variaciones estacionales en producción y rendimiento.
    
    Parameters:
    - data: DataFrame de pandas que contiene los datos.
    
    Returns:
    - variaciones_estacionales: DataFrame de pandas con la producción y el rendimiento promedio por período.
    """
    produccion_periodo = data.groupby('PERIODO')['PRODUCCION'].mean()
    rendimiento_periodo = data.groupby('PERIODO')['RENDIMIENTO'].mean()

    variaciones_estacionales = pd.DataFrame({
        'Producción Promedio (t)': produccion_periodo,
        'Rendimiento Promedio (t/ha)': rendimiento_periodo
    })
    
    return variaciones_estacionales

def calculate_trendline(values):
    """
    Calcula la línea de tendencia para los valores dados.
    
    Parameters:
    - values: Serie de pandas con los valores para los que se calculará la línea de tendencia.
    
    Returns:
    - trendline: Valores de la línea de tendencia.
    """
    z = np.polyfit(range(len(values)), values, 1)
    p = np.poly1d(z)
    trendline = p(range(len(values)))
    
    return trendline