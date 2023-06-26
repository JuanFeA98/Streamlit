import pandas as pd
import numpy as np

import streamlit as st
import streamlit_authenticator as stauth

import requests

url = 'https://auth_demo-1-k6090383.deta.app/credentials/jmart'

response = requests.get(url)
print(response.json()['credentials'])


# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )
