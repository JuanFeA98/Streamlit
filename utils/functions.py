import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

import streamlit as st

def user_input_features():
    sepal_lenght = st.sidebar('sepal_length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar('sepal_width', 2.0, 4.4, 3.4)
    petal_lenght = st.sidebar('petal_length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar('petal_width', 0.1, 2.5, 0.2)

    data = {
        'sepal_lenght': sepal_lenght,
        'sepal_width': sepal_width,
        'petal_lenght': petal_lenght,
        'petal_width': petal_width
    }

    features = pd.DataFrame(data, index=[0])

    return features