# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# URL dataset Iris dari UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Kolom dataset (karena file iris.data tidak punya header)
col_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Load dataset dari UCI
df = pd.read_csv(url, header=None, names=col_names)

# Pisahkan fitur dan target
X = df.iloc[:, :-1]  # fitur
y = df.iloc[:, -1]   # target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Buat model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Simpan model ke file .pkl
joblib.dump(model, "iris_model.pkl")

print("Model berhasil dibuat dan disimpan ke iris_model.pkl")
