import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/patelmanishv/Sem4Data/refs/heads/master/Data/Fish.csv')

# 🔧 Fix: Convert categorical 'Species' to numeric using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Set target and features
y = df['Weight']
x = df.drop(columns=['Weight'])

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Mean Squared Error:", mse)
print("✅ R2 Score:", r2)

# Predict new value (adjust columns for shape match)
custom_input = pd.DataFrame([[20, 20, 30, 12, 5] + [0]*(len(x.columns)-5)], columns=x.columns)
custom_pred = model.predict(custom_input)

print("🔮 Predicted Weight:", custom_pred[0])
