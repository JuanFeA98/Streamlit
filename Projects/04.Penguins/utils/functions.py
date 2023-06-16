import pandas as pd
import numpy as np

import streamlit as st

def user_input_features():
    island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.sidebar.slider('Bill length (mm)', 172, 231, 201)
    body_mass_g = st.sidebar.slider('Body mass (g)', 2700, 6300, 4207)

    data = {
        'island': island, 
        'sex': sex, 
        'bill_length_mm': bill_length_mm, 
        'bill_depth_mm': bill_depth_mm, 
        'flipper_length_mm': flipper_length_mm, 
        'body_mass_g': body_mass_g 
    }

    features = pd.DataFrame(data, index=[0])
    return features