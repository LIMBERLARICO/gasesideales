import streamlit as st

R = 0.0821  # L·atm/mol·K

st.title("Calculadora de Gases Ideales: Estado Inicial vs. Final")
st.write("Basado en la ecuación general de los gases ideales: **PV = nRT**")

# Selección de la variable a calcular en el estado final
variable = st.selectbox("¿Qué variable deseas calcular en el estado final?", 
                        ["Presión (P₂)", "Volumen (V₂)", "Temperatura (T₂)", "Número de moles (n₂)"])

st.subheader("🔵 Condiciones Iniciales (Estado 1)")
P1 = st.number_input("Presión P₁ (atm)", min_value=0.0001)
V1 = st.number_input("Volumen V₁ (L)", min_value=0.0001)
T1 = st.number_input("Temperatura T₁ (K)", min_value=0.0001)
n1 = st.number_input("Número de moles n₁ (mol)", min_value=0.0001)

st.subheader("🟢 Condiciones Finales (Estado 2)")
P2 = V2 = T2 = n2 = None

# Mostrar campos según lo que se quiere calcular
if variable == "Presión (P₂)":
    V2 = st.number_input("Volumen V₂ (L)", min_value=0.0001)
    T2 = st.number_input("Temperatura T₂ (K)", min_value=0.0001)
    n2 = st.number_input("Número de moles n₂ (mol)", value=n1, min_value=0.0001)
    if st.button("Calcular Presión Final"):
        P2 = (n2 * R * T2) / V2
        st.success(f"Presión Final P₂ = {P2:.3f} atm")

elif variable == "Volumen (V₂)":
    P2 = st.number_input("Presión P₂ (atm)", min_value=0.0001)
    T2 = st.number_input("Temperatura T₂ (K)", min_value=0.0001)
    n2 = st.number_input("Número de moles n₂ (mol)", value=n1, min_value=0.0001)
    if st.button("Calcular Volumen Final"):
        V2 = (n2 * R * T2) / P2
        st.success(f"Volumen Final V₂ = {V2:.3f} L")

elif variable == "Temperatura (T₂)":
    P2 = st.number_input("Presión P₂ (atm)", min_value=0.0001)
    V2 = st.number_input("Volumen V₂ (L)", min_value=0.0001)
    n2 = st.number_input("Número de moles n₂ (mol)", value=n1, min_value=0.0001)
    if st.button("Calcular Temperatura Final"):
        T2 = (P2 * V2) / (n2 * R)
        st.success(f"Temperatura Final T₂ = {T2:.3f} K")

elif variable == "Número de moles (n₂)":
    P2 = st.number_input("Presión P₂ (atm)", min_value=0.0001)
    V2 = st.number_input("Volumen V₂ (L)", min_value=0.0001)
    T2 = st.number_input("Temperatura T₂ (K)", min_value=0.0001)
    if st.button("Calcular Número de moles Final"):
        n2 = (P2 * V2) / (R * T2)
        st.success(f"Número de moles Final n₂ = {n2:.3f} mol")

# Mostrar resumen final si todos los datos están listos
if all(v is not None for v in [P1, V1, T1, n1]) and variable.startswith("Presión") and P2 is not None:
    st.info(f"Comparación: P₁ = {P1} atm → P₂ = {P2:.3f} atm")

# Puedes replicar este bloque para V₂, T₂, n₂ si deseas más mensajes comparativos
