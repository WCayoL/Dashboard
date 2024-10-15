import pandas as pd
import streamlit as st

data_url = "data/IDP_SEPTIEMBRE_PRUEBA.csv"

st.title("Dashboard Retailatam 📈")
st.markdown("ssssssssssssss")

@st.cache_data
def load_data():
   data = pd.read_csv(data_url, delimiter=';')
   return data

"""# Calcular las medidas necesarias
def calcular_kpi(data):
    total_by_planogramm = data[data['sku_status'] == 'by_planogramm'].shape[0]
    total_not_exposed = data[data['sku_status'] == 'not_exposed'].shape[0]
    total_shelf_error = data[data['sku_status'] == 'shelf_error'].shape[0]
    total_sku_position_error = data[data['sku_status'] == 'sku_position_error'].shape[0]

    # Calcular el KPI
    kpi_cumplimiento = total_by_planogramm / (total_by_planogramm + total_not_exposed + total_shelf_error + total_sku_position_error) * 100
    return kpi_cumplimiento"""




data= load_data()
#st.subheader('Raw Data')
#st.write(data)

"""kpi = calcular_kpi(data)
# Mostrar el KPI
st.metric(label='KPI de Cumplimiento', value=f'{kpi:.2f}%', delta='-')"""