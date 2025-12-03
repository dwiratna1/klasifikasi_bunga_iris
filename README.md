# 🌸 Aplikasi Klasifikasi Bunga Iris

Aplikasi ini merupakan Sistem Pendukung Keputusan (SPK) berbasis web yang menggunakan metode **Klasifikasi** untuk memprediksi jenis bunga Iris berdasarkan parameter ukuran bunga.

Metode yang digunakan: **Machine Learning - Classification (K-Nearest Neighbors / Random Forest / Logistic Regression)**  
Dataset: **Iris Dataset (UCI Machine Learning Repository)**  
Aplikasi Web: **Streamlit**

---

## 🚀 Fitur Aplikasi

- Input 4 parameter utama bunga:
  - Panjang Kelopak (Sepal Length)
  - Lebar Kelopak (Sepal Width)
  - Panjang Mahkota (Petal Length)
  - Lebar Mahkota (Petal Width)
- Melakukan prediksi jenis bunga:
  - *Iris Setosa*
  - *Iris Versicolor*
  - *Iris Virginica*
- Menampilkan hasil prediksi secara langsung.
- Dapat diakses sebagai aplikasi web melalui **Streamlit Cloud**.

---

## 📊 Dataset

Dataset yang digunakan berasal dari:
https://archive.ics.uci.edu/dataset/53/iris

Dataset berisi:
- 150 data bunga
- 4 fitur numerik
- 3 kelas atau jenis bunga

---

## 🧠 Metode Klasifikasi

Model Machine Learning yang digunakan:
- K-Nearest Neighbor (KNN) **atau sesuai model kamu**
- Dataset dibagi menjadi train dan test
- Model dilatih, kemudian disimpan dalam file `iris_model.pkl`
- Model dipanggil oleh aplikasi Streamlit untuk prediksi realtime

---

## 🗂️ Struktur Folder

