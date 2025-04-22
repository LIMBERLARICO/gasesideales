import streamlit as st

st.title("Calculadora de Gases Ideales (PV/T = constante)")
st.markdown("Usa la relación **P·V / T = constante**, válida si el número de moles no cambia.")

# Selección de tipo de variable a calcular
tipo = st.radio("¿Qué tipo de condición deseas calcular?", ["Inicial", "Final"])
variables = {
    "Inicial": ["Presión inicial (P₁)", "Volumen inicial (V₁)", "Temperatura inicial (T₁)"],
    "Final": ["Presión final (P₂)", "Volumen final (V₂)", "Temperatura final (T₂)"]
}
var_a_calcular = st.selectbox("¿Qué variable deseas calcular?", variables[tipo])

st.subheader("🔷 Datos conocidos")

# Entradas según tipo y variable a calcular
if tipo == "Inicial":
    if var_a_calcular == "Presión inicial (P₁)":
        V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)
        P2 = st.number_input("Presión final (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
        if st.button("Calcular P₁"):
            P1 = (P2 * V2 * T1) / (V1 * T2)
            st.success(f"Presión inicial P₁ = {P1:.3f} atm")

    elif var_a_calcular == "Volumen inicial (V₁)":
        P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)
        P2 = st.number_input("Presión final (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
        if st.button("Calcular V₁"):
            V1 = (P2 * V2 * T1) / (P1 * T2)
            st.success(f"Volumen inicial V₁ = {V1:.3f} L")

    elif var_a_calcular == "Temperatura inicial (T₁)":
        P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
        V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
        P2 = st.number_input("Presión final (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
        if st.button("Calcular T₁"):
            T1 = (P1 * V1 * T2) / (P2 * V2)
            st.success(f"Temperatura inicial T₁ = {T1:.3f} K")

elif tipo == "Final":
    if var_a_calcular == "Presión final (P₂)":
        P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
        V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)
        V2 = st.number_input("Volumen final (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
        if st.button("Calcular P₂"):
            P2 = (P1 * V1 * T2) / (V2 * T1)
            st.success(f"Presión final P₂ = {P2:.3f} atm")

    elif var_a_calcular == "Volumen final (V₂)":
        P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
        V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)
        P2 = st.number_input("Presión final (atm)", min_value=0.0001)
        T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
        if st.button("Calcular V₂"):
            V2 = (P1 * V1 * T2) / (P2 * T1)
            st.success(f"Volumen final V₂ = {V2:.3f} L")

    elif var_a_calcular == "Temperatura final (T₂)":
        P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
        V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)
        P2 = st.number_input("Presión final (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final (L)", min_value=0.0001)
        if st.button("Calcular T₂"):
            T2 = (P2 * V2 * T1) / (P1 * V1)
            st.success(f"Temperatura final T₂ = {T2:.3f} K")
