import pandas as pd
import numpy as np

import streamlit as st

import pickle

from utils.functions import user_input_features

st.write('''
    # **Penguins prediction app**

    This app predicts the **Palmer Penguin** species.
''')

st.sidebar.header('Use input features')
st.sidebar.markdown('''
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
''')

uploaded_file = st.sidebar.file_uploader('Upload your input file', type=['csv'])

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
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded.')
    st.write(df)

load_rfc = pickle.load(open('../../Models/penguin_class.pkl', 'rb'))

prediction = load_rfc.predict(df)
prediction_proba = load_rfc.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[prediction])

# prediction_proba.columns = ['Adelie', 'Chinstrap', 'Gentoo']

st.subheader('Prediction Probability')
st.write(prediction_proba)

