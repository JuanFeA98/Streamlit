import streamlit_authenticator as stauth

import firebase_admin 
from firebase_admin import credentials, firestore

# Conectamos con nuestra app en firebase
cred = credentials.Certificate('./serviceAccountKey.json')

# Agregamos la contraseña para nuestro usuario
password = input('Introduce la contraseña: ')

# Creamos nuestra constraseña cifrada
hashed_password = stauth.Hasher([f'{password}']).generate()

user_info = {
    'credentials':{
        'usernames': {
            'jmart':{
                'email': 'juan@gmail.com', 
                'name': 'juan',
                'password': f'{hashed_password[0]}'
            }
        }
    },
    'cookie':{
        'expiry_days': 30,
        'key': 'random_signature_key',
        'name': 'random_cookie_name'
    },
    'preauthorized':{
        'emails':{
            'melsby@gmail.com'
        }
    }
}

firebase_admin.initialize_app(cred)
db = firestore.client()

username = list(user_info['credentials']['usernames'].keys())[0]

db.collection('credentials').document(username).set(user_info)