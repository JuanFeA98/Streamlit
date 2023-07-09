import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

st.title('Churn Dataset!')

import os

df = pd.read_csv('./Datos/Churn.csv', sep=';')

variables_agrupacion = st.multiselect(
    'Variables de agrupación: ',
    ['CANAL', 'REGIONAL'],
    ['CANAL'])

color = st.selectbox(
    'Color', 
    variables_agrupacion
    )

df_resumen = df.groupby(variables_agrupacion).agg({
    'OPENING': 'sum',
    'ENDING': 'sum',
    'CHURN': 'sum'
}).reset_index()

df_resumen['%Churn_Rate'] = df_resumen.apply(lambda x: round(x['CHURN']/((x['OPENING'] + x['ENDING'])/2)*100, 2), axis=1)
df_resumen['%Churn_Share'] = df_resumen['CHURN'].apply(lambda x: round(x/df_resumen['CHURN'].sum()*100, 2))

fig = px.scatter(
    df_resumen, 
    x=f"%Churn_Rate", 
    y=f"%Churn_Share",
    color=color
    # text=f'{variables_agrupacion}',
    # hover_data=[variables_agrupacion, 'ENDING', 'CHURN']
)

st.plotly_chart(fig, use_container_width=True)
