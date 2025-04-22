import streamlit as st

st.title("Calculadora de Gases Ideales (PV/T = constante)")
st.markdown("Basado en la relación:  \n **(P₁·V₁)/T₁ = (P₂·V₂)/T₂**")

# Elegir si se quiere calcular una variable de la condición inicial o final
condicion = st.radio("¿Qué condición deseas calcular?", ["Inicial", "Final"])

# Elegir qué variable calcular dentro de la condición elegida
if condicion == "Inicial":
    variable = st.selectbox("Selecciona la variable inicial a calcular", ["Presión (P₁)", "Volumen (V₁)", "Temperatura (T₁)"])
else:
    variable = st.selectbox("Selecciona la variable final a calcular", ["Presión (P₂)", "Volumen (V₂)", "Temperatura (T₂)"])

st.subheader("🔷 Ingreso de datos conocidos")

# Ingreso de datos según la variable seleccionada
if condicion == "Inicial":
    if variable == "Presión (P₁)":
        V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.0001)
        P2 = st.number_input("Presión final P₂ (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final V₂ (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.0001)
        if st.button("Calcular P₁"):
            P1 = (P2 * V2 * T1) / (V1 * T2)
            st.success(f"Presión inicial P₁ = {P1:.3f} atm")
            st.write(f"Condiciones finales: P₂={P2} atm, V₂={V2} L, T₂={T2} K")
    elif variable == "Volumen (V₁)":
        P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.0001)
        T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.0001)
        P2 = st.number_input("Presión final P₂ (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final V₂ (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.0001)
        if st.button("Calcular V₁"):
            V1 = (P2 * V2 * T1) / (P1 * T2)
            st.success(f"Volumen inicial V₁ = {V1:.3f} L")
    elif variable == "Temperatura (T₁)":
        P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.0001)
        V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.0001)
        P2 = st.number_input("Presión final P₂ (atm)", min_value=0.0001)
        V2 = st.number_input("Volumen final V₂ (L)", min_value=0.0001)
        T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.0001)
        if st.button("Calcular T₁"):
            T1 = (P1 * V1 * T2) / (P
