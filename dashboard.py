import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data CSV
day_data = pd.read_csv('/mnt/data/day.csv')
hour_data = pd.read_csv('/mnt/data/hour.csv')

# Menambahkan logo Dicoding
st.image("https://help.dicoding.com/wp-content/uploads/2021/01/dicoding-edit-1024x341.jpg", use_column_width=True)

# Judul aplikasi Streamlit
st.title('Dashboard Penyewaan Sepeda')

# Menambahkan nama dan copyright
st.markdown("### Revan Azriel Langa Aditya")
st.markdown("© Dicoding 2024")

# Sidebar untuk memilih visualisasi
st.sidebar.header('Visualisasi')
option = st.sidebar.selectbox('Pilih visualisasi:', (
    'Distribusi Penyewaan Sepeda Sepanjang Hari', 
    'Perbedaan Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan', 
    'Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda'))

# Menampilkan visualisasi sesuai pilihan
if option == 'Distribusi Penyewaan Sepeda Sepanjang Hari':
    st.header('Distribusi Penyewaan Sepeda Sepanjang Hari')
    fig, ax = plt.subplots()
    
    # Memastikan kolom 'cnt' ada
    if 'cnt' in hour_data.columns:
        sns.histplot(hour_data['cnt'], bins=30, kde=True, ax=ax, color='cyan')
        ax.set_title('Distribusi Total Penyewaan Sepeda Sepanjang Hari')
    else:
        st.error("Kolom 'cnt' tidak ditemukan dalam hour_data.")
    
    st.pyplot(fig)

elif option == 'Perbedaan Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan':
    st.header('Perbedaan Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan')
    
    # Mengkategorikan data berdasarkan hari kerja dan akhir pekan
    day_data['is_weekend'] = day_data['weekday'].apply(lambda x: 'Akhir Pekan' if x in [0, 6] else 'Hari Kerja')
    
    fig, ax = plt.subplots()
    sns.barplot(x='is_weekend', y='cnt', data=day_data, ax=ax, palette='dark')
    ax.set_title('Rata-rata Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan')
    st.pyplot(fig)

elif option == 'Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda':
    st.header('Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda')
    
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt', hue='weekday', data=hour_data, palette='coolwarm', ax=ax)
    ax.set_title('Jumlah Penyewaan Berdasarkan Hari dalam Seminggu dan Jam')
    st.pyplot(fig)

# Menambahkan warna background dashboard
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1f2a3b;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
