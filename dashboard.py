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
    'Perbandingan Sewa Sepeda Antara Hari Kerja dan Akhir Pekan', 
    'Distribusi Penyewaan Sepeda di Sepanjang Hari', 
    'Penyewaan Sepeda Berdasarkan Hari dalam Seminggu'))

# Menampilkan visualisasi sesuai pilihan
if option == 'Perbandingan Sewa Sepeda Antara Hari Kerja dan Akhir Pekan':
    st.header('Penyewaan Sepeda di Hari Kerja vs Akhir Pekan')
    sns.set(style="whitegrid")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x="workingday", y="cnt", data=day_data, ax=ax)
    ax.set_title("Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("Hari Kerja (1 = Yes, 0 = No)")
    ax.set_ylabel("Total Penyewaan Sepeda")
    st.pyplot(fig)

elif option == 'Distribusi Penyewaan Sepeda di Sepanjang Hari':
    st.header('Distribusi Penyewaan Sepeda Berdasarkan Jam')
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="hr", y="cnt", data=hour_data, ci=None, ax=ax)
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)

elif option == 'Penyewaan Sepeda Berdasarkan Hari dalam Seminggu':
    st.header('Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x="weekday", y="cnt", data=day_data, ax=ax)
    ax.set_title("Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 1 = Senin, 2 = Selasa, ..., 6 = Sabtu)")
    ax.set_ylabel("Total Penyewaan Sepeda")
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
