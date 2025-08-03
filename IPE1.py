# Use the file data.csv which contains 169 rows and 4 columns.  
# 1. Convert this file into pandas Data Frame and Display basic statistics like mean, std, quartiles, etc. for this data frame.  
# 2. Print first and last 5 rows. Also print the shape of the dataframe. 
# 3. Create a correlation table for the data frame and comment about what kind of correlation is there between Duration and Calories?  
# 4. Find whether there any null or NA values, drop all such rows if found in the data frame and print the shape of the data frame after dropping.  
# 5. Prepare a scatter matrix for the following data frame. 
# 6. Prepare a parallel coordinates for Duration v/s Pulse, Maxpulse and Calories (all 3 other columns). 
# 7. Prepare a cross-tabulation for Duration v/s Pulse. 
# 8. Do Maxpulse have any outliers? Find using function. 

import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix,parallel_coordinates
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/patelmanishv/Sem4Data/refs/heads/master/Data/data.csv')
print(df.describe())

print(df.head())
print(df.tail())
print(df.shape)

corr = df.corr()
print('Correlation Table : \n', corr)

print(df.isnull().sum())
df = df.dropna()
print(df.shape)

scatter_matrix(df, figsize=(8, 8), diagonal='kde')
plt.suptitle("Scatter Matrix")
plt.show()

parallel_coordinates(df, 'Duration', cols=['Pulse', 'Maxpulse', 'Calories'])
plt.title("Parallel Coordinates for Duration vs Pulse, Maxpulse, Calories")
plt.show()

crosstab = pd.crosstab(df['Duration'], df['Pulse'])
print('Cross-tabulation for Duration vs Pulse:\n', crosstab)

def detect_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data < lower_bound) | (data > upper_bound)]

outliers_maxpulse = detect_outliers(df['Maxpulse'])
if not outliers_maxpulse.empty:
    print("Outliers in Maxpulse:\n", outliers_maxpulse)
else:
    print("No outliers found in Maxpulse.")

    