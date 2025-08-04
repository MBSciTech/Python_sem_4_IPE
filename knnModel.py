import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report

df = pd.read_csv("https://raw.githubusercontent.com/patelmanishv/Sem4Data/refs/heads/master/Data/Churn.csv")
df.TotalCharges=df.TotalCharges.fillna(df.TotalCharges.mean())

categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',  'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',  'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',  'PaperlessBilling', 'PaymentMethod']
df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
X = df.drop(['customerID', 'Churn',"Unnamed: 0"], axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

