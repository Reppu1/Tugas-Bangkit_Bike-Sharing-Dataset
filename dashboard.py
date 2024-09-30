import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data 
day_data_url = 'https://raw.githubusercontent.com/Reppu1/Tugas-Bangkit_Bike-Sharing-Dataset/main/day.csv'
hour_data_url = 'https://raw.githubusercontent.com/Reppu1/Tugas-Bangkit_Bike-Sharing-Dataset/main/hour.csv'
main_data_url = 'https://raw.githubusercontent.com/Reppu1/Tugas-Bangkit_Bike-Sharing-Dataset/main/main_data.csv'

# Mengunduh dan membaca data
day_data = pd.read_csv(requests.get(day_data_url).content.decode('utf-8'))
hour_data = pd.read_csv(requests.get(hour_data_url).content.decode('utf-8'))
main_data = pd.read_csv(requests.get(main_data_url).content.decode('utf-8'))

# Title of the dashboard
st.title('Dashboard Penyewaan Sepeda')

# Sidebar for selecting visualization options
st.sidebar.header('Visualisasi')
option = st.sidebar.selectbox('Pilih visualisasi:', ('Distribusi Penyewaan Sepeda', 'Jumlah Penyewaan Berdasarkan Hari', 'Jumlah Penyewaan Berdasarkan Jam'))

# Show the selected visualization
if option == 'Distribusi Penyewaan Sepeda':
    st.header('Distribusi Penyewaan Sepeda')
    fig, ax = plt.subplots()
    sns.histplot(main_data['cnt'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribusi Total Penyewaan Sepeda')
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

# Additional metrics or filters
st.sidebar.subheader('Filter Data')
weekday = st.sidebar.multiselect('Pilih Hari dalam Seminggu:', main_data['weekday'].unique(), default=main_data['weekday'].unique())
filtered_data = main_data[main_data['weekday'].isin(weekday)]

st.dataframe(filtered_data.head())  # Show filtered data as a table

# Menambahkan copyright di bagian bawah
st.caption('Copyright © Dicoding 2024')
