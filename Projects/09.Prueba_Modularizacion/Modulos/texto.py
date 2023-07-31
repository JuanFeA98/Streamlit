import pandas as pd
import numpy as np

import plotly.express as px

import streamlit as st

df = px.data.iris() # iris is a pandas DataFrame


def componente_1():
    
    variable_x = st.selectbox(
        'Variable X', 
        ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        )

    variable_y = st.selectbox(
        'Variable Y', 
        ('sepal_width', 'sepal_length', 'petal_length', 'petal_width')
        )
    fig = px.scatter(df, x=f"{variable_x}", y=f"{variable_y}", color='species')

    return(
        st.text('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae urna libero. 
            loremvel eros euismod mollis. Donec eu bibendum risus, ut imperdiet enim.
        '''), 
        
        st.plotly_chart(fig, use_container_width=True)
    )    