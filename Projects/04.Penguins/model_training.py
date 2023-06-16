import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

import pickle

import warnings
warnings.filterwarnings('ignore')

# Cargamos los datos
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# Ajustamos las variables categoricas
target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

df['species'].replace({
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
}, inplace=True)

# Separamos el dataset
X = df.drop('species', axis=1).copy()
y = df[['species']].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=13, train_size=0.7)

# Entrenamos el modelo
rfc = RandomForestClassifier(random_state=13)
rfc.fit(X_train, y_train)

# Evaluamos el modelo
y_pred = rfc.predict(X_test)

print(f'Tenemos un modelo con presición del: {accuracy_score(y_pred=y_pred, y_true=y_test)}')

# Guardamos el modelo
pickle.dump(rfc, open('../../Models/penguin_class.pkl', 'wb'))