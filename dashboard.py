import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Menambahkan logo perusahaan
st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

# Load the data 
day_data = pd.read_csv('day_data.csv')
hour_data = pd.read_csv('hour_data.csv')

# Merge day_data and hour_data (if applicable)
main_data = pd.merge(day_data, hour_data, on='dteday', how='inner')

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
