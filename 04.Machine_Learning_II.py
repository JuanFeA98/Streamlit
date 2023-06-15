import pandas as pd
import numpy as np

import streamlit as st

st.write('''
    # **Hello World**
''')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

st.write(df)