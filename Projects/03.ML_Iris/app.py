import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

import streamlit as st

from utils.functions import user_input_features

st.write('''
    ## **Prediction App - Iris Flower**
    This app predicts the flower type
''')

st.sidebar.header('Use Input Parameters')

df = user_input_features()

st.subheader('User Input Parameter')
st.write(df)

# Model

# Data Preparation
iris = datasets.load_iris()

X = iris.data
y = iris.target

# Training model
clf = RandomForestClassifier(random_state=13)
clf.fit(X, y)

# Prediction 
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(
    pd.DataFrame(
        [i.capitalize() for i in iris.target_names], 
        columns=['Category']
    ).transpose()
)

col1, col2 = st.columns([1,1])

col1.subheader('Prediction')
col1.write(
    pd.DataFrame({
        'Specie': iris.target_names[prediction][0].capitalize(),
        'Label': [prediction][0]
    })
)

col2.subheader('Prediction Probability')
col2.write(
    pd.DataFrame(
        prediction_proba, 
        columns=[i.capitalize() for i in iris.target_names]
    )
)