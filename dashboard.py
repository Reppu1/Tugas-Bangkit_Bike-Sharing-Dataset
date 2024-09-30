import pandas as pd
import requests
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# URL untuk file CSV
day_data_url = "day.csv"
hour_data_url = 'hour.csv'
main_data_url = 'main_data.csv'

# Mengunduh dan membaca data
try:
    day_data = pd.read_csv(requests.get(day_data_url).content.decode('utf-8'))
    hour_data = pd.read_csv(requests.get(hour_data_url).content.decode('utf-8'))
    main_data = pd.read_csv(requests.get(main_data_url).content.decode('utf-8'))

    # Menampilkan nama kolom untuk memeriksa
    st.write("Kolom dalam day_data:", day_data.columns.tolist())
    st.write("Data dari day_data:")
    st.dataframe(day_data.head())  # Tampilkan beberapa baris data

except Exception as e:
    st.error(f"Error loading data: {e}")

# Judul aplikasi Streamlit
st.title('Dashboard Penyewaan Sepeda')

# Sidebar untuk memilih visualisasi
st.sidebar.header('Visualisasi')
option = st.sidebar.selectbox('Pilih visualisasi:', ('Distribusi Penyewaan Sepeda', 'Jumlah Penyewaan Berdasarkan Hari', 'Jumlah Penyewaan Berdasarkan Jam'))

# Menampilkan visualisasi sesuai pilihan
if option == 'Distribusi Penyewaan Sepeda':
    st.header('Distribusi Penyewaan Sepeda')
    fig, ax = plt.subplots()
    
    # Pastikan kolom 'cnt' ada
    if 'cnt' in day_data.columns:
        sns.histplot(day_data['cnt'], bins=30, kde=True, ax=ax)
        ax.set_title('Distribusi Total Penyewaan Sepeda')
    else:
        st.error("Kolom 'cnt' tidak ditemukan dalam day_data.")
    
    st.pyplot(fig)

elif option == 'Jumlah Penyewaan Berdasarkan Hari':
    st.header('Jumlah Penyewaan Berdasarkan Hari')
    fig, ax = plt.subplots()
    sns.barplot(x='weekday', y='cnt', data=day_data, ax=ax)
    ax.set_title('Rata-rata Penyewaan Berdasarkan Hari')
    st.pyplot(fig)

elif option == 'Jumlah Penyewaan Berdasarkan Jam':
    st.header('Jumlah Penyewaan Berdasarkan Jam')
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=hour_data, ax=ax)
    ax.set_title('Jumlah Penyewaan Berdasarkan Jam')
    st.pyplot(fig)
