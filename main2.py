import pandas as pd
import streamlit as st

url = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.xlsx'
df = pd.read_csv(url, sep=';', encoding='utf-8')

st.dataframe(df)

# crea lista de columnas de interes
seleccion_columnas = ['FECHA_HECHOS'. 'DELITO', 'ETAPA','FISCAL_ASIGNADO', 'DEPARTAMENTO','MUNICIO_HECHOS']
#ACTUALIZO DATAFRAME CON LAS COLUMNAS DE INTERES, ORDENASD POR FECHA Y RESETEO EL INDICE
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

st.dataframe(df)