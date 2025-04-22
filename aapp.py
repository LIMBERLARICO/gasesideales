import streamlit as st

st.title("Calculadora de Gases Ideales (sin cambio de moles)")
st.markdown("Usamos la fórmula: **P·V / T = constante** (n constante)")

# Selección de variable a calcular en la condición final
opcion = st.selectbox("¿Qué variable final deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)"])

st.subheader("Condiciones Iniciales")
P1 = st.number_input("Presión inicial (atm)", min_value=0.0001)
V1 = st.number_input("Volumen inicial (L)", min_value=0.0001)
T1 = st.number_input("Temperatura inicial (K)", min_value=0.0001)

st.subheader("Condiciones Finales")

if opcion == "Presión (P)":
    V2 = st.number_input("Volumen final (L)", min_value=0.0001)
    T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
    if st.button("Calcular Presión final"):
        P2 = (P1 * V1 * T2) / (T1 * V2)
        st.success(f"Presión final = {P2:.3f} atm")

elif opcion == "Volumen (V)":
    P2 = st.number_input("Presión final (atm)", min_value=0.0001)
    T2 = st.number_input("Temperatura final (K)", min_value=0.0001)
    if st.button("Calcular Volumen final"):
        V2 = (P1 * V1 * T2) / (T1 * P2)
        st.success(f"Volumen final = {V2:.3f} L")

elif opcion == "Temperatura (T)":
    P2 = st.number_input("Presión final (atm)", min_value=0.0001)
    V2 = st.number_input("Volumen final (L)", min_value=0.0001)
    if st.button("Calcular Temperatura final"):
        T2 = (T1 * P2 * V2) / (P1 * V1)
        st.success(f"Temperatura final = {T2:.3f} K")

# Mostrar resumen
st.subheader("Resumen de Condiciones")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Inicial")
    st.write(f"Presión: {P1} atm")
    st.write(f"Volumen: {V1} L")
    st.write(f"Temperatura: {T1} K")

with col2:
    st.markdown("### Final")
    if opcion != "Presión (P)":
        st.write(f"Presión: {P2} atm")
    if opcion != "Volumen (V)":
        st.write(f"Volumen: {V2} L")
    if opcion != "Temperatura (T)":
        st.write(f"Temperatura: {T2} K")
