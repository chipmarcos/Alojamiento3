import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Ruta del archivo en local
LOCAL_PATH = r"C:\Users\Marcos\Desktop\PROG2\integridad.xlsx"

@st.cache_data
def cargar_datos():
    return pd.read_excel(LOCAL_PATH)

df = cargar_datos()

# Crear filtros
st.title("Dashboard de Integridad Académica")

universidades = df["Universidad"].unique()
universidad_sel = st.selectbox("Selecciona una Universidad", universidades)

# Filtrar por Universidad
df_filtrado = df[df["Universidad"] == universidad_sel]

# Mostrar segundo filtro solo si se seleccionó una Universidad
if not df_filtrado.empty:
    licenciaturas = df_filtrado["Licenciatura"].unique()
    licenciatura_sel = st.selectbox("Selecciona una Licenciatura", licenciaturas)
    
    df_filtrado = df_filtrado[df_filtrado["Licenciatura"] == licenciatura_sel]
    
    # Gráfico de barras
    if not df_filtrado.empty:
        st.subheader("Integridad Académica")
        fig, ax = plt.subplots(figsize=(8, 4))
        df_filtrado["Integridad Académica"].value_counts().plot(kind='bar', color='skyblue', ax=ax)
        ax.set_xlabel("Nivel de Integridad Académica")
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
