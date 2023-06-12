import pandas as pd
import numpy as np

import streamlit as st

import yfinance as yf

st.write('''
    ## **Simple :red[Stock Price] App**
''')

tickerSymbol = 'GOOGL'

st.write(f'''
    {tickerSymbol}         
''')

try:
    tickerDF = pd.read_csv('./Data/yahoo_finance.csv')
except:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    tickerDF.to_csv('./Data/yahoo_finance.csv', index=False)

# First Row
col1, col2 = st.columns([1, 1])

col1.subheader('Volume')
col1.line_chart(tickerDF.Volume)

col2.subheader('Close Price')
col2.line_chart(tickerDF.Close)

# Second Row
st.write('''
    #### **Gross Composition**
''')
col1, col2, col3 = st.columns([1,0.5,4])

chart_data = pd.DataFrame(
    np.random.randn(1, 2),
    columns=["Good Quality", "Bad Quality"])

col1.bar_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Good Quality', 'Bad Quality']
)

col3.line_chart(chart_data)

# Third Row
st.write('''
    #### **Churn Composition**
''')
col1, col2, col3 = st.columns([4,0.5,1])

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Good Quality', 'Bad Quality']
)
col1.line_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(1, 2),
    columns=["Good Quality", "Bad Quality"])

col3.bar_chart(chart_data)