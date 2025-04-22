import streamlit as st

st.title("Calculadora General de Gases Ideales (PV/T = constante)")
st.markdown("Usa la relación:  \n**(P₁·V₁)/T₁ = (P₂·V₂)/T₂** (n constante)")

# Selección de la variable a calcular
var_opciones = {
    "Presión inicial (P₁)": "P1",
    "Volumen inicial (V₁)": "V1",
    "Temperatura inicial (T₁)": "T1",
    "Presión final (P₂)": "P2",
    "Volumen final (V₂)": "V2",
    "Temperatura final (T₂)": "T2"
}
variable = st.selectbox("Selecciona la variable a calcular:", list(var_opciones.keys()))
calc = var_opciones[variable]

# Campos para ingresar datos conocidos
def campo_input(nombre, key, excluir):
    if key != excluir:
        return st.number_input(nombre, min_value=0.0001, key=key)
    return None

st.subheader("🔷 Ingreso de valores conocidos")
P1 = campo_input("Presión inicial P₁ (atm)", "P1", calc)
V1 = campo_input("Volumen inicial V₁ (L)", "V1", calc)
T1 = campo_input("Temperatura inicial T₁ (K)", "T1", calc)
P2 = campo_input("Presión final P₂ (atm)", "P2", calc)
V2 = campo_input("Volumen final V₂ (L)", "V2", calc)
T2 = campo_input("Temperatura final T₂ (K)", "T2", calc)

# Botón de cálculo
if st.button("Calcular"):
    try:
        if calc == "P1":
            result = (P2 * V2 * T1) / (V1 * T2)
            st.success(f"Presión inicial P₁ = {result:.3f} atm")
            P1 = result
        elif calc == "V1":
            result = (P2 * V2 * T1) / (P1 * T2)
            st.success(f"Volumen inicial V₁ = {result:.3f} L")
            V1 = result
        elif calc == "T1":
            result = (P1 * V1 * T2) / (P2 * V2)
            st.success(f"Temperatura inicial T₁ = {result:.3f} K")
            T1 = result
        elif calc == "P2":
            result = (P1 * V1 * T2) / (V2 * T1)
            st.success(f"Presión final P₂ = {result:.3f} atm")
            P2 = result
        elif calc == "V2":
            result = (P1 * V1 * T2) / (P2 * T1)
            st.success(f"Volumen final V₂ = {result:.3f} L")
            V2 = result
        elif calc == "T2":
            result = (P2 * V2 * T1) / (P1 * V1)
            st.success(f"Temperatura final T₂ = {result:.3f} K")
            T2 = result
    except:
        st.error("Verifica que todos los datos sean correctos y no sean cero.")

    # Mostrar condiciones completas
    st.subheader("📋 Condiciones completas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Inicial")
        st.write(f"P₁ = {P1:.3f} atm" if P1 else "P₁ = ?")
        st.write(f"V₁ = {V1:.3f} L" if V1 else "V₁ = ?")
        st.write(f"T₁ = {T1:.3f} K" if T1 else "T₁ = ?")
    with col2:
        st.markdown("### Final")
        st.write(f"P₂ = {P2:.3f} atm" if P2 else "P₂ = ?")
        st.write(f"V₂ = {V2:.3f} L" if V2 else "V₂ = ?")
        st.write(f"T₂ = {T2:.3f} K" if T2 else "T₂ = ?")
