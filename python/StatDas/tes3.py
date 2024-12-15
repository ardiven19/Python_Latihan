import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Mengimpor dataset (ganti dengan nama file dan path yang sesuai)
df = pd.read_csv("C:/Users/ACER/Downloads/Electric_Vehicle_Population_Data.csv")
pd.set_option('display.max_columns', None)

# Misalkan Anda ingin membagi distrik-distrik menjadi 3 kategori berdasarkan nilai Legislative District (rendah, sedang, tinggi)
# Anda dapat menggunakan metode quartile atau binning
bins = [0, df['Legislative District'].quantile(0.33), df['Legislative District'].quantile(0.66), df['Legislative District'].max()]
labels = ['Rendah', 'Sedang', 'Tinggi']
df['District Category'] = pd.cut(df['Legislative District'], bins=bins, labels=labels, include_lowest=True)

# Hitung jumlah kendaraan listrik untuk setiap kategori Legislative District
district_category_counts = df['District Category'].value_counts()

# Visualisasi distribusi jumlah kendaraan listrik berdasarkan kategori Legislative District
plt.figure(figsize=(10, 6))
district_category_counts.plot(kind='bar', color='skyblue')
plt.title('Distribusi Kendaraan Listrik berdasarkan Kategori Distrik Legislatif')
plt.xlabel('Kategori Distrik Legislatif')
plt.ylabel('Jumlah Kendaraan Listrik')
plt.xticks(rotation=0)
plt.show()

# Lakukan uji ANOVA untuk membandingkan jumlah kendaraan listrik antara ketiga kategori distrik
# Misalnya, bandingkan antara kategori "Rendah", "Sedang", dan "Tinggi"
low_district_counts = df[df['District Category'] == 'Rendah']['Legislative District'].value_counts()
medium_district_counts = df[df['District Category'] == 'Sedang']['Legislative District'].value_counts()
high_district_counts = df[df['District Category'] == 'Tinggi']['Legislative District'].value_counts()

# Hanya lakukan uji ANOVA jika semua kelompok memiliki lebih dari 1 sampel
if len(low_district_counts) > 1 and len(medium_district_counts) > 1 and len(high_district_counts) > 1:
    f_statistic, p_value = f_oneway(low_district_counts, medium_district_counts, high_district_counts)

    print(f"F-statistic: {f_statistic}, p-value: {p_value}")

    # Interpretasi hasil
    alpha = 0.05
    if p_value < alpha:
        print("Terdapat perbedaan signifikan dalam jumlah kendaraan listrik antara ketiga kategori distrik.")
    else:
        print("Tidak terdapat perbedaan signifikan dalam jumlah kendaraan listrik antara ketiga kategori distrik.")
else:
    print("Tidak dapat melakukan uji ANOVA karena salah satu atau lebih kelompok memiliki hanya 1 sampel.")
