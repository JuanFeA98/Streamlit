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

# Mostramos la estructura necesaria del archivo
st.sidebar.markdown('''
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
''')

# SideBar
# Componente para cargar archivos en formato csv
uploaded_file = st.sidebar.file_uploader('Upload your input file', type=['csv'])

# Si no se carga un archivo se utilizan los features de los inputs
if uploaded_file is not None:
    # Leemos el archivo cargado
    input_df = pd.read_csv(uploaded_file)
else:
    # Configuramos los inputs para que queden en el formato necesario para el modelo
    input_df = user_input_features()

# Mostramos los datos del registro que queremos predecir
if uploaded_file is None:
    st.write('Data from inputs:')
    st.write(input_df)
else:
    st.write('Data uploaded:')
    st.write(input_df)

# Cargamos nuestro modelo entrenado
load_rfc = pickle.load(open('../../Models/penguin_class.pkl', 'rb'))

# Realizamos las predicciones
prediction = load_rfc.predict(input_df)
prediction_proba = pd.DataFrame(load_rfc.predict_proba(input_df))
prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']

# Mostramos los resultados
col1, col2 = st.columns([1, 1])

# Probabilidad para cada categoria
col1.subheader('Prediction Probability')
col1.write(prediction_proba)
col2.subheader('Prediction')

# Valor de la predicción
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
col2.write(penguins_species[prediction])