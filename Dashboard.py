import pandas as pd
import streamlit as st

data_url = "data/IDP SEPTIEMBRE PRUEBA.csv"

st.title("Dashboard Retailatam 📈")
st.markdown("")

@st.cache_data
def load_data(nrows):
   data = pd.read_csv(data_url, nrows=nrows)
   return data

data= load_data(100)
st.subheader('Raw Data')
st.write(data)