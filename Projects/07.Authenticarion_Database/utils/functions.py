import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

def initialize_firebase():
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    ref = db.reference()

    return ref

def call_data():

    db = firestore.client()

    config = db.collection('credentials').document('jmart').get()
    config = config.to_dict()

    return config