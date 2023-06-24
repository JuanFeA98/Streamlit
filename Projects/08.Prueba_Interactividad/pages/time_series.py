import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

st.title('Time Series')

variable_agrup = st.selectbox(
    'Periodo', 
    ('2023_04', '2023_05')
)

df = pd.read_csv(f'./Datos/{variable_agrup}.csv')

fig = px.line(df, x="DIA", y="Valor", title='Line Chart', text='Valor')

st.plotly_chart(fig, use_container_width=True)
