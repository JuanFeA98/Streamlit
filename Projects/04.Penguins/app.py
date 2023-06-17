import pandas as pd
import numpy as np

import streamlit as st

import pickle

from utils.functions import user_input_features

# Header
st.write('''
    # **Penguins prediction app**

    This app predicts the **Palmer Penguin** species.
''')

st.sidebar.header('Use input features')
st.sidebar.markdown('''
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
''')

# SideBar
# Componente para cargar archivos en formato csv
uploaded_file = st.sidebar.file_uploader('Upload your input file', type=['csv'])

# Si no se carga un archivo se utilizan los features de los inputs
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = user_input_features()

penguins_raw = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])

df = pd.concat([input_df, penguins], axis=0)

encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)

    del df[col]

df = df[:1]

if uploaded_file is None:
    st.write('Data from inputs:')
    st.write(df)
else:
    st.write('Data uploaded:')
    st.write(df)

load_rfc = pickle.load(open('../../Models/penguin_class.pkl', 'rb'))

prediction = load_rfc.predict(df)
prediction_proba = pd.DataFrame(load_rfc.predict_proba(df))

col1, col2 = st.columns([1, 1])

prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']

col1.subheader('Prediction Probability')
col1.write(prediction_proba)
col2.subheader('Prediction')

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
col2.write(penguins_species[prediction])