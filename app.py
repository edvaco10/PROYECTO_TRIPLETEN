import pandas as pd
import plotly.express as px
import streamlit as st

ruta_archivo = r'C:\Users\edvac\OneDrive\Desktop\MY_APP_PROJECT\PROYECTO_TRIPLETEN\vehicles_us.csv'
car_data = pd.read_csv(ruta_archivo)

show_histogram = st.checkbox('Mostrar histograma')  # casilla de verificación para el histograma
show_scatter = st.checkbox('Mostrar gráfico de dispersión')  # casilla de verificación para el gráfico de dispersión

if show_histogram:  # si la casilla de verificación de histograma está marcada
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')  # escribir un mensaje
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:  # si la casilla de verificación de gráfico de dispersión está marcada
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model", y="price")  # Corregido el parámetro 'color'
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)