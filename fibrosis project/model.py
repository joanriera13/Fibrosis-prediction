import openpyxl

import os

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import warnings
warnings.filterwarnings('ignore')

dd = pd.read_excel("FibroPredCODIFICADA2.xlsx")
columns = dd.columns

dd['Pathology pattern'] = dd['Pathology pattern'].replace({0: 'No','Granulomatosis':'No'})

x = dd[['TOBACCO','Age at diagnosis','Pathology pattern','FamilialvsSporadic','Binary diagnosis','Comorbidities','Genetic mutation studied in patient','Radiological Pattern', 'FVC (%) at diagnosis','DLCO (%) at diagnosis']]
y = dd['Progressive disease']
dd_var = dd[['TOBACCO','Age at diagnosis','Pathology pattern','Final diagnosis','FamilialvsSporadic','Binary diagnosis','Comorbidities','Genetic mutation studied in patient','Radiological Pattern', 'FVC (%) at diagnosis','DLCO (%) at diagnosis','Progressive disease']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)


from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
for col in X_train.columns:
    if X_train[col].dtype == 'object':  # Verifica si la columna es categórica
        X_train[col] = encoder.fit_transform(X_train[col])
        X_val[col] = encoder.transform(X_val[col])

nan_columns = X_train.isnull().any()

# Feim KNN
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)
y_val_pred = knn.predict(X_val)

def prediccion(vars):
    new_samples = pd.DataFrame({
    'TOBACCO': [vars[0]],
    'Age at diagnosis': [vars[1]],
    'Pathology pattern': [vars[2]],
    'FamilialvsSporadic': [vars[3]],
    'Binary diagnosis': [vars[4]],
    'Comorbidities': [vars[5]],
    'Genetic mutation studied in patient': [vars[6]],
    'Radiological Pattern': [vars[7]],
    'FVC (%) at diagnosis': [vars[8]],
    'DLCO (%) at diagnosis': [vars[9]]})
    for col in new_samples.columns:
        if new_samples[col].dtype == 'object':  # Verifica si la columna es categórica
            new_samples[col] = encoder.fit_transform(new_samples[col])

    pred = knn.predict(new_samples)
    return pred[0]
