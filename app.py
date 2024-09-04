import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('D:/Desktop/MiProyecto/repositorio_proyecto_tt/vehicles_us.csv')

st.header('Cuadro de Mandos de Anuncios de Coches')

# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

# Cuando el botón se presiona
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma para la columna 'odometer'
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el histograma usando Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Cuando el botón se presiona
if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión usando Streamlit
    st.plotly_chart(fig, use_container_width=True)

