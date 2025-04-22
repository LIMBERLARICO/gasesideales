import streamlit as st
from PIL import Image

st.image("imagen1.png", caption="", use_column_width=False)

# Constante universal de los gases (L·atm/mol·K)
R = 0.0821

st.title("Calculadora de la Ecuación de los Gases Ideales")
st.write("Ecuación: **PV = nRT**")

# Selección de la variable a calcular
opcion = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

# Mostrar campos según la variable seleccionada
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.0001)
    n = st.number_input("Número de moles (mol)", min_value=0.0001)
    T = st.number_input("Temperatura (K)", min_value=0.0001)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"Presión = {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.0001)
    n = st.number_input("Número de moles (mol)", min_value=0.0001)
    T = st.number_input("Temperatura (K)", min_value=0.0001)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"Volumen = {V:.3f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.0001)
    V = st.number_input("Volumen (L)", min_value=0.0001)
    n = st.number_input("Número de moles (mol)", min_value=0.0001)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"Temperatura = {T:.3f} K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.0001)
    V = st.number_input("Volumen (L)", min_value=0.0001)
    T = st.number_input("Temperatura (K)", min_value=0.0001)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"Número de moles = {n:.3f} mol")
