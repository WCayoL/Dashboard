import pandas as pd
import streamlit as st

data_url = "data/IDP_SEPTIEMBRE_PRUEBA.csv"

st.title("Dashboard Retailatam 📈")
st.markdown("")

@st.cache_data
def load_data():
   data = pd.read_csv(data_url, delimiter=';')
   return data

data= load_data()
st.subheader('Raw Data')
st.write(data)