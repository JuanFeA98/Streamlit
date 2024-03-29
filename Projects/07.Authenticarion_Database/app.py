import pandas as pd
import numpy as np

import streamlit as st
import streamlit_authenticator as stauth

import requests

url = 'https://auth_demo-1-k6090383.deta.app/credentials/jmart'
response = requests.get(url)

config = response.json()
config = config['message']

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')