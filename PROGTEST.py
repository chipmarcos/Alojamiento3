import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URL del archivo en GitHub
GITHUB_URL = "https://raw.githubusercontent.com/chipmarcos/Alojamiento3/main/integridad.csv"

@st.cache_data
def cargar_datos():
    return pd.read_csv(GITHUB_URL)

df = cargar_datos()

# Crear filtros de forma progresiva
st.title("Dashboard de Integridad Académica")

# Primer filtro: Universidad
universidades = df["Universidad"].unique()
universidad_sel = st.selectbox("Selecciona una Universidad", ["Selecciona una opción"] + list(universidades))

if universidad_sel != "Selecciona una opción":
    df_filtrado = df[df["Universidad"] == universidad_sel]
    
    # Segundo filtro: Licenciatura
    licenciaturas = df_filtrado["Licenciatura"].unique()
    licenciatura_sel = st.selectbox("Selecciona una Licenciatura", ["Selecciona una opción"] + list(licenciaturas))
    
    if licenciatura_sel != "Selecciona una opción":
        df_filtrado = df_filtrado[df_filtrado["Licenciatura"] == licenciatura_sel]
        
        # Mostrar gráfico solo si hay datos filtrados
        if not df_filtrado.empty:
            st.subheader("Integridad Académica")
            fig, ax = plt.subplots(figsize=(8, 4))
            df_filtrado["Integridad Académica"].value_counts().plot(kind='bar', color='skyblue', ax=ax)
            ax.set_xlabel("Nivel de Integridad Académica")
            ax.set_ylabel("Frecuencia")
            st.pyplot(fig)
