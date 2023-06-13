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
