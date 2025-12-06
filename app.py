# app.py
import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("iris_model.pkl")

# Judul aplikasi
st.title("🌸 Iris Flower Classification App")
st.write("Aplikasi ini memprediksi jenis bunga Iris berdasarkan parameter ukuran bunga.")

# Input fitur
sepal_length = st.number_input("Panjang Sepal (cm)", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Lebar Sepal (cm)", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Panjang Kelopak (cm)", min_value=0.0, max_value=10.0, value=4.0)
petal_width = st.number_input("Lebar Kelopak (cm)", min_value=0.0, max_value=10.0, value=1.2)

# Tombol prediksi
if st.button("Prediksi"):
    fitur = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediksi = model.predict(fitur)[0]

    st.success(f"🌼 Jenis bunga Iris: **{prediksi.capitalize()}**")

    # Probabilitas prediksi
    prob = model.predict_proba(fitur)[0]
    st.subheader("Probabilitas Prediksi:")
    for label, p in zip(model.classes_, prob):
        st.write(f"- {label.capitalize()}: {p*100:.2f}%")
