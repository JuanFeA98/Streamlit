import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

# Hello world
st.title('Hello World!')

st.text('Actualizando contenido...')

# Gráfico base
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# Markdown
st.markdown('''

### **Titulo**

Probando **Markdown**

- Item 1
- Item 2

1. Prueba 1
2. Prueba 2

''')

# Código
st.code('''
import pandas as pd

df = pd.DataFrame({
    A: [1, 2],
    B: [3, 4]
})

print(df)
''')

# Dataframes
df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})


st.dataframe(df)

# Metricas
st.metric("Metrica 1", 1000, -200)

# Matplotlib chart
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    st.pyplot(fig)

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)