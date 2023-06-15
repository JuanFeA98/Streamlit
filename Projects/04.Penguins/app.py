import pandas as pd
import numpy as np

import streamlit as st

import pickle

st.write('''
    # **Penguins prediction app**

    This app predicts the **Palmer Penguin** species.
''')

st.sidebar.header('Use input features')
st.sidebar.markdown('''

    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)

''')