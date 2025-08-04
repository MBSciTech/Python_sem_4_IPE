#Polynomial Regressiom

import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/patelmanishv/Sem4Data/refs/heads/master/Data/Fish.csv')
df = pd.get_dummies(df, drop_first=True)
x = df.drop(columns=['Weight'])
y = df['Weight']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

degree=3
poly = PolynomialFeatures(degree=degree)
x_poly_train = poly.fit_transform(x_train)
x_poly_test = poly.transform(x_test)

model = LinearRegression()
model.fit(x_poly_train, y_train)

y_pred = model.predict(x_poly_test)
print( y_pred)

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print("✅ Mean Squared Error:", mse)
print("✅ R2 Score:", r2)

print("🔮 Predicted Weight for custom input:", model.predict(poly.transform([[20, 20, 30, 12, 5] + [0]*(len(x.columns)-5)])))