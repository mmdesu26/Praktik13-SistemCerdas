import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Muat dataset
df_mobil = pd.read_csv("HargaMobil.csv")

# Pilih fitur (X) dan variabel target (y)
X = df_mobil[['highwaympg', 'curbweight', 'horsepower']]
y = df_mobil['price']

# Bagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat dan latih model regresi linear
model_regresi = LinearRegression()
model_regresi.fit(X_train, y_train)

# Simpan model yang telah dilatih ke file pickle
filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))

