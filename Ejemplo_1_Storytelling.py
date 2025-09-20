# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 22:00:48 2025

@author: cesar
"""

# ==================================================
# Streamlit + PyNarrative Storytelling
# ==================================================

import streamlit as st
import pandas as pd
import pynarrative as pn

st.set_page_config(page_title="Storytelling Retail", layout="wide")

# ===========================
# 1. Cargar archivo
# ===========================
st.title("📊 Storytelling de Retail con PyNarrative")

uploaded_file = st.file_uploader("📂 Sube tu archivo Excel o CSV", type=["csv", "xlsx"])

if uploaded_file:
    # Leer datos
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ Archivo cargado correctamente")
    st.dataframe(df.head())

    # ===========================
    # 2. Selección de historia
    # ===========================
    opcion = st.radio(
        "Elige la historia que quieres visualizar:",
        ["📈 Ventas", "💰 Utilidades", "👥 Clientes"]
    )

    # ===========================
    # 3. Crear historias
    # ===========================

    if "Year" not in df.columns:
        st.error("⚠️ Tu archivo debe tener una columna 'Year'.")
    else:
        if opcion == "📈 Ventas":
            story = (
                pn.Story(df, width=700, height=400)
                  .mark_line(color="steelblue")
                  .encode(x="Year:O", y="Sales:Q")
                  .add_title("Tendencia de Ventas", "Evolución anual", title_color="#2c3e50")
                  .add_context("Las ventas reflejan el desempeño anual del retail", position="top")
            )

        elif opcion == "💰 Utilidades":
            story = (
                pn.Story(df, width=700, height=400)
                  .mark_bar(color="orange")
                  .encode(x="Year:O", y="Profit:Q")
                  .add_title("Utilidad por Año", "Margen de ganancia", title_color="#8e44ad")
                  .add_context("Las utilidades están influenciadas por costos e inversión en campañas", position="top")
            )

        elif opcion == "👥 Clientes":
            story = (
                pn.Story(df, width=700, height=400)
                  .mark_area(color="green", opacity=0.5)
                  .encode(x="Year:O", y="Customers:Q")
                  .add_title("Evolución de Clientes", "2018-2023", title_color="#16a085")
                  .add_context("El número de clientes muestra fidelización y atracción de nuevos compradores", position="top")
            )

        # ===========================
        # 4. Renderizar historia
        # ===========================
        #st.components.v1.html(story.render().html(), height=500, scrolling=True)
        st.altair_chart(story.render(), use_container_width=True)

else:
    st.info("📥 Sube un archivo para comenzar.")







# cd "C:\Users\Sala_\Downloads"
# py -m streamlit run Ejemplo_1_Storytelling.py

