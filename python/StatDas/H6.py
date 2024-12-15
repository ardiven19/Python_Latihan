import pandas as pd
from sklearn.linear_model import LinearRegression

# Mengimpor dataset
df = pd.read_csv("C:/Users/ACER/Downloads/Electric_Vehicle_Population_Data.csv")
pd.set_option('display.max_columns', None)

# Membuat data frame baru dengan nilai 0 dan 1
df['Vehicle Type Binary'] = df['Electric Vehicle Type'].apply(lambda x: 0 if x == 'Plug-in Hybrid Electric Vehicle (PHEV)' else 1)

# Menyiapkan data untuk model
X = df[['Vehicle Type Binary', 'Model Year']]
y = df['Electric Range']

# Melatih model regresi linear
regr = LinearRegression()
regr.fit(X, y)

# Memprediksi nilai
# Memprediksi nilai dengan nama fitur yang sesuai
new_data = pd.DataFrame({'Vehicle Type Binary': [1], 'Model Year': [2000]})
predicted_range = regr.predict(new_data)

print(predicted_range)
df1 = df[df['Model Year'] ==2000]
print(df1)

