import pandas as pd
import streamlit as st

data_url = ("IDP SEPTIEMBRE PRUEBA.csv")

st.title("Dashboard Retailatam 📈")
st.markdown("")

@st.cache_data
def load_data(nrows):
   data = pd.read_csv(data_url, nrows=nrows)
   #data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
   #lowercase = lambda x: str(x).lower()
   #data.rename(lowercase, axis='columns', inplace=True)
   #data.rename(columns={'crash_date_crash_time': "date/time"}, inplace=True)
   return data

data= load_data(100000)
st.subheader('Raw Data')
st.write(data)