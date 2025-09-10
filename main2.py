import pandas as pd
import streamlit as st

url = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='latin-1')

st.dataframe(df)

# crea lista de columnas de interes
seleccion_columnas = ['FECHA_HECHOS', 'DELITO','ETAPA','FISCAL_ASIGNADO', 'DEPARTAMENTO','MUNICIPIO_HECHOS']
#ACTUALIZO DATAFRAME CON LAS COLUMNAS DE INTERES, ORDENASD POR FECHA Y RESETEO EL INDICE
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)


#convierto la columna fecha hechos a formato fecha
df['FECHA_HECHOS']= pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

# EXTRAIGO SOLO LA FECHA (SIN HORA)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

st.dataframe(df)

#CALCULO DE MUNICIPIOS QUE TIENEN MAS DELITOS, el value_ count cuanta cuantas veces se repite un dato

max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0]
#max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
st.write(f"Municipio TOP Delitos: {max_municipio}")

st.write(max_municipio)

# construir la pagina
st.set_page_config(page_title="Tablero de control delitos fiscaliaaaa", layout="centered")
st.header("Tablero de control Delitos fiscalia")
#st.markdown(f"<center><h2>Tablero de control delitos fiscaliaaaaaa")
st.dataframe(df)