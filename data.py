# Langkah 1: Mengimpor pustaka yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Langkah 2: Memuat dataset
file_path = 'yenny.csv'  # Nama file CSV yang baru saja Anda buat
data = pd.read_csv(file_path)

# Langkah 3: Melihat informasi dasar tentang dataset
print("Informasi Dasar Dataset:")
print(data.info())
print("\nDeskripsi Statistik:")
print(data.describe())

# Langkah 4: Mengecek nilai yang hilang
print("\nCek Nilai yang Hilang:")
print(data.isnull().sum())

# Langkah 5: Melihat beberapa baris pertama dataset
print("\nBeberapa Baris Pertama Dataset:")
print(data.head())

# Langkah 6: Eksplorasi Data Awal
# Distribusi dari setiap kolom numerik
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 4))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribusi {column}')
    plt.xlabel(column)
    plt.ylabel('Frekuensi')
    plt.show()

# Heatmap korelasi antar variabel numerik
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap Korelasi')
plt.show()

# Plotting beberapa relasi antar kolom (scatter plot)
# Ganti 'col1' dan 'col2' dengan nama kolom yang ingin dianalisis
col1 = 'Age'
col2 = 'Salary'
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data[col1], y=data[col2])
plt.title(f'Scatter Plot antara {col1} dan {col2}')
plt.xlabel(col1)
plt.ylabel(col2)
plt.show()

# Boxplot untuk melihat distribusi dan outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=data.select_dtypes(include=['float64', 'int64']))
plt.title('Boxplot Distribusi Kolom Numerik')
plt.xticks(rotation=90)
plt.show()
