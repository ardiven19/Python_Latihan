import pandas as pd
import matplotlib.pyplot as plt
import sns

df = pd.read_csv("C:/Users/ACER/Downloads/Electric_Vehicle_Population_Data.csv")
pd.set_option('display.max_columns', None)
print(df.columns)

data3 = df[df['County'] == 'King']
data2 = data3.groupby(data3['Make'])['Model Year'].mean()
data2.plot(kind='line', marker='o')
plt.show()
data4 = data3.groupby(data3['Make'])[['Model Year', 'Make']]
print(data4.head(10))
a = []
for i in(df['Make']):
    if i in a:
        continue
    a.append(i)
a.sort()
print(a)
dx = {}
for i in a:
    dx[i] = df[df['Make'] == i].size
print(dx)

df1 = df[df['Make'] == 'AUDI']
df2 = df1.groupby('County')['County'].count()
df2.plot(kind='line', marker='o')
plt.show()
print(df2)
print(df1)

print(df['Model Year'].unique())
print(df['County'].unique())
print(df['City'].unique())
print(df['State'].unique())
print(df['Model'].unique())
print(df['Electric Utility'].unique())

df3 = df.groupby('State')['State'].count()
df3.plot(kind='line', marker='o')
dfx = list(set(df['State']))
dfx.sort()

print(list(set(df['State'])))

df4 = df.groupby('Make')['Make'].count()
k = df4
print(df4)
print(k)


df5 = df1.groupby('Model Year')['Model Year'].count()
print(df5)




#Distribusi kendaraan berdasarkan Tahun Model.
#Distribusi kendaraan berdasarkan Jenis Kendaraan Listrik.
#Distribusi kendaraan berdasarkan Make (Pembuat Kendaraan).
#Rata-rata Electric Range dari berbagai Model Kendaraan.
#Distribusi kendaraan berdasarkan Eligibilitas CAFV (Clean Alternative Fuel Vehicle).
#Distribusi kendaraan berdasarkan Negara Bagian (State).
#Distribusi kendaraan berdasarkan Kota (City).
#Distribusi kendaraan berdasarkan County.
#Distribusi kendaraan berdasarkan Harga MSRP Dasar.
#Distribusi kendaraan berdasarkan Lokasi.
#Distribusi kendaraan berdasarkan Utilitas Listrik.
#Analisis keterkaitan antara Electric Range dan Base MSRP.