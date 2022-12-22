import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('Customer_Behaviour.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Perilaku Pelanggan')

col1, col2 = st.columns(2)

with col1:
    User_ID = st.text_input('Input Nilai User ID')

with col2:
    Gender = st.text_input('Input Nilai Gender')

with col1:
    Age = st.text_input(' Input Nilai Age')

with col2:
    EstimatedSalary = st.text_input('Input Nilai Estimated Salary')

# code untuk prediksi
    pelanggan_diagnosis = ''

# membuat tombol
if st.button('Mulai'):
    pelanggan_prediction = model.predict(
        [[User_ID, Gender, Age, EstimatedSalary]])

    if (pelanggan_prediction[0] == 1):
        pelanggan_diagnosis = 'Pelanggan Membeli Produk'
    else:
        pelanggan_diagnosis = 'Pelanggan Tidak Membeli Produk'

st.success(pelanggan_diagnosis)
