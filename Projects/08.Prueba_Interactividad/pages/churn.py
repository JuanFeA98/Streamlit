import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

st.title('Churn Dataset!')

import os

df = pd.read_csv('./Datos/Churn.csv', sep=';')

variable_agrup = st.sidebar.selectbox(
    'Variable de Agrupación', 
    ('CANAL', 'REGIONAL')
)

df_resumen = df.groupby(f'{variable_agrup}')[['ENDING','OPENING','CHURN']].sum().reset_index()
df_resumen['CHURN_RATE'] = df_resumen.apply(lambda x: round(x['CHURN']/((x['ENDING'] + x['OPENING'])/2), 2), axis=1)
df_resumen['CHURN_SHARE'] = df_resumen['CHURN'].apply(lambda x: round(x/df_resumen['CHURN'].sum(), 2))

# st.write(df_resumen)

fig = px.scatter(
    df_resumen, 
    x=f"CHURN_RATE", 
    y=f"CHURN_SHARE",
    # text=f'{variable_agrup}',
    hover_data=[f'{variable_agrup}', 'ENDING', 'CHURN']
)

st.plotly_chart(fig, use_container_width=True)
