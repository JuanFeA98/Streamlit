import pandas as pd
import numpy as np

import streamlit as st
import plotly.express as px

st.title('Hello World!')

df = px.data.iris() # iris is a pandas DataFrame
print(df.columns)

variable_x = st.sidebar.selectbox('Variable X', ('sepal_length', 'sepal_width', 'petal_length', 'petal_width'))
variable_y = st.sidebar.selectbox('Variable Y', ('sepal_length', 'sepal_width', 'petal_length', 'petal_width'))

fig = px.scatter(df, x=f"{variable_x}", y=f"{variable_y}")

st.plotly_chart(fig, use_container_width=True)