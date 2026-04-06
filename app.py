import pandas as pd
import plotly.express as px
import streamlit as st

# encabezado
st.header("Dashboard de vehículos en venta")

# leer datos
df = pd.read_csv('vehicles_us.csv')

# mostrar datos
st.write(df.head())

# botón histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma del odómetro")

    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# botón scatter
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Relación precio vs odómetro")

    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)

build_hist = st.checkbox("Mostrar histograma")

if build_hist:
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)
