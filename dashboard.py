# Import library
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data CSV
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Menambahkan logo Dicoding
st.image("https://help.dicoding.com/wp-content/uploads/2021/01/dicoding-edit-1024x341.jpg", use_column_width=True)

# Styling agar semua teks berada di center
st.markdown(
    """
    <style>
    .center-text {
        text-align: center;
    }
    .stApp {
        background-color: #1f2a3b;
        color: #ffffff;
    }
    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi Streamlit
st.markdown('<h1 class="center-text">Dashboard Penyewaan Sepeda</h1>', unsafe_allow_html=True)

# Sidebar untuk memilih visualisasi
st.sidebar.header('Visualisasi')
option = st.sidebar.selectbox('Pilih visualisasi :', (
    'Perbandingan Sewa Sepeda Antara Hari Kerja dan Akhir Pekan', 
    'Distribusi Penyewaan Sepeda di Sepanjang Hari', 
    'Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda'))

# Menampilkan visualisasi sesuai pilihan
if option == 'Perbandingan Sewa Sepeda Antara Hari Kerja dan Akhir Pekan':
    st.markdown('<h2 class="center-text">Penyewaan Sepeda di Hari Kerja vs Akhir Pekan</h2>', unsafe_allow_html=True)
    sns.set(style="whitegrid")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x="workingday", y="cnt", data=day_data, ax=ax)
    ax.set_title("Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("Hari Kerja (1 = Yes, 0 = No)")
    ax.set_ylabel("Total Penyewaan Sepeda")
    st.pyplot(fig)
    
    st.markdown(
        """
        <div class="center-text">
        Grafik boxplot menunjukkan bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan akhir pekan. Hal ini bisa disebabkan oleh pengguna yang menggunakan sepeda sebagai sarana transportasi untuk bekerja.
        </div>
        """, 
        unsafe_allow_html=True
    )

elif option == 'Distribusi Penyewaan Sepeda di Sepanjang Hari':
    st.markdown('<h2 class="center-text">Distribusi Penyewaan Sepeda Berdasarkan Jam</h2>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="hr", y="cnt", data=hour_data, ci=None, ax=ax)
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)
    
    st.markdown(
        """
        <div class="center-text">
        Grafik line plot menunjukkan tren penyewaan sepeda per jam. Terdapat dua puncak penyewaan utama: pagi sekitar pukul 8-9 (mungkin karena orang pergi bekerja) dan sore sekitar pukul 17-18 (kemungkinan karena pulang kerja).
        </div>
        """, 
        unsafe_allow_html=True
    )

elif option == 'Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda':
    st.markdown('<h2 class="center-text">Penyewaan Sepeda Berdasarkan Hari dalam Seminggu</h2>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x="weekday", y="cnt", data=day_data, ax=ax)
    ax.set_title("Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 1 = Senin, 2 = Selasa, ..., 6 = Sabtu)")
    ax.set_ylabel("Total Penyewaan Sepeda")
    st.pyplot(fig)
    
    st.markdown(
        """
        <div class="center-text">
        Grafik boxplot menunjukkan distribusi penyewaan berdasarkan hari dalam seminggu. Hari kerja (terutama hari Senin hingga Jumat) cenderung memiliki lebih banyak penyewaan sepeda dibandingkan akhir pekan, yang menegaskan pola serupa dengan analisis hari kerja.
        </div>
        """, 
        unsafe_allow_html=True
    )

# Menambahkan nama pembuat dan copyright
st.markdown(
    """
    <footer>
        <p>Revan Azriel Langa Aditya - ML 67</p>
        <p>© Dicoding 2024</p>
    </footer>
    """, 
    unsafe_allow_html=True
)
