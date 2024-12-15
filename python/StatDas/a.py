import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chisquare

# Mengimpor dataset (ganti dengan nama file dan path yang sesuai)
data = pd.read_csv("C:/Users/ACER/OneDrive/문서/Struktur Data/Buku1.csv")
le2 = pd.read_csv("C:/Users/ACER/Downloads/LEG 2.csv")
le3 = pd.read_csv("C:/Users/ACER/Downloads/LEG3.csv")
le4 = pd.read_csv("C:/Users/ACER/Downloads/LEG4.csv")
a = data[["id", "nama"]].values.tolist()

c = []
print(a)