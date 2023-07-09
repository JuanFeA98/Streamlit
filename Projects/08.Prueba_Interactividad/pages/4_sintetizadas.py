import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

import itertools

st.title('Bases sintetizadas!')

variables_agrupacion = st.multiselect(
    'Variables de agrupación: ',
    ['rangoRec', 'rangoAnt', 'segmentacion'],
    ['rangoRec', 'rangoAnt'])

va = list(variables_agrupacion)
elementos = ' '.join("_").join(va)

resultados = [list(i) for i in list(itertools.permutations(va, len(va)))]

for i in resultados:
    formateo = ' '.join("_").join(i)
    print(formateo)
    try:
        df_agrupado = pd.read_csv(f'./Datos/Sintetizados/{formateo}.csv')
        break
    except:
        pass

# st.write(f'{list(variables_agrupacion).extend(['A', 'B'])}')

fig = px.scatter(
    df_agrupado, 
    x='SHARE', 
    y='RATE',
    color='segmentacion'
    # text=f'{variables_agrupacion[0]}',
    # hover_data=[variables_agrupacion]
)

st.plotly_chart(fig, use_container_width=True)
