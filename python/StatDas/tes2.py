import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Mengimpor dataset (ganti dengan nama file dan path yang sesuai)
df = pd.read_csv("C:/Users/ACER/Downloads/Electric_Vehicle_Population_Data.csv")
pd.set_option('display.max_columns', None)

# Mengidentifikasi merek mobil terbanyak
most_common_make = df['Make'].value_counts().idxmax()
print(f"Merek mobil terbanyak adalah: {most_common_make}")

# Filter data untuk merek mobil terbanyak
most_common_make_df = df[df['Make'] == most_common_make]

# Mengidentifikasi top 10 kota dengan jumlah kendaraan terbanyak untuk merek mobil terbanyak
top_cities = most_common_make_df['City'].value_counts().head(10).index.tolist()

# Membuat grafik penyebaran kendaraan berdasarkan kota untuk merek mobil terbanyak (hanya top 10 kota)
plt.figure(figsize=(12, 6))
sns.countplot(data=most_common_make_df, x='City', order=top_cities)
plt.title(f'Penyebaran Kendaraan {most_common_make} Berdasarkan Kota (Top 10)')
plt.xlabel('Kota')
plt.ylabel('Jumlah Kendaraan')
plt.xticks(rotation=45)
plt.show()

# Filter data untuk top 3 kota teratas
top_3_cities = top_cities[:3]
top_3_cities_df = most_common_make_df[most_common_make_df['City'].isin(top_3_cities)]

# Melakukan ANOVA satu arah pada 'Electric Range' antara top 3 kota teratas
anova_result = f_oneway(*[top_3_cities_df[top_3_cities_df['City'] == city]['Electric Range'] for city in top_3_cities])

print(f"ANOVA result: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")

# Interpretasi hasil
if anova_result.pvalue < 0.05:
    print(f"Terdapat perbedaan signifikan dalam Electric Range antara {', '.join(top_3_cities)}.")
else:
    print(f"Tidak terdapat perbedaan signifikan dalam Electric Range antara {', '.join(top_3_cities)}.")
