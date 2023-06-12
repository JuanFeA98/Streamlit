import pandas as pd

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


col1, col2 = st.columns([1, 1])

col1.subheader('Volume')
col1.line_chart(tickerDF.Volume)

col2.subheader('Close Price')
col2.line_chart(tickerDF.Close)