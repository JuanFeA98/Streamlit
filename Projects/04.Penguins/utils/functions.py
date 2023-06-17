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
        'bill_length_mm': bill_length_mm, 
        'bill_depth_mm': bill_depth_mm, 
        'flipper_length_mm': flipper_length_mm, 
        'body_mass_g': body_mass_g,
        'sex_female': False,
        'sex_male': False,
        'island_Biscoe': False,
        'island_Dream': False, 
        'island_Torgersen': False
    }

    if sex == 'female':
        data['sex_female'] = True
    elif sex=='male':
        data['sex_male'] = True

    if island == 'Biscoe':
        data['island_Biscoe'] = True
    elif island == 'Dream':
        data['island_Dream'] = True
    elif island == 'Torgersen':
        data['island_Torgersen'] = True

    features = pd.DataFrame(data, index=[0])
    return features