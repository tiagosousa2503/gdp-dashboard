import streamlit as st

# --- Funções de cálculo ---

def calcular_tributos_atuais(valor, pis=0.0165, cofins=0.076, icms=0.12, ipi=0.10):
    return {
        "PIS": valor * pis,
        "COFINS": valor * cofins,
        "ICMS": valor * icms,
        "IPI": valor * ipi
    }

def calcular_tributos_reforma(valor, cbs=0.0925, ibs=0.14, seletivo=0.10):
    return {
        "CBS": valor * cbs,
        "IBS": valor * ibs,
        "IMPOSTO SELETIVO": valor * seletivo
    }

# --- Interface Streamlit ---

st.set_page_config(page_title="Simulador Reforma Tributária", layout="centered")

st.title("📊 Simulador Reforma Tributária")
st.markdown("Compare a carga tributária atual com a proposta pela Reforma.")

# Entrada do usuário
valor_operacao = st.number_input("💰 Valor da Operação (R$)", min_value=0.0, step=100.0, value=1000.0)

# Alíquotas customizáveis (opcional)
with st.expander("⚙️ Configurar Alíquotas (opcional)"):
    col1, col2 = st.columns(2)
    with col1:
        pis = st.number_input("PIS (%)", value=1.65) / 100
        cofins = st.number_input("COFINS (%)", value=7.6) / 100
        icms = st.number_input("ICMS (%)", value=12.0) / 100
        ipi = st.number_input("IPI (%)", value=10.0) / 100
    with col2:
        cbs = st.number_input("CBS (%)", value=9.25) / 100
        ibs = st.number_input("IBS (%)", value=14.0) / 100
        seletivo = st.number_input("Imposto Seletivo (%)", value=10.0) / 100

# Botão de simulação
if st.button("📈 Simular"):
    tributos_atuais = calcular_tributos_atuais(valor_operacao, pis, cofins, icms, ipi)
    tributos_reforma = calcular_tributos_reforma(valor_operacao, cbs, ibs, seletivo)

    total_atual = sum(tributos_atuais.values())
    total_reforma = sum(tributos_reforma.values())
    diferenca = total_reforma - total_atual
    variacao = (diferenca / valor_operacao) * 100 if valor_operacao else 0

    st.subheader("🧾 Tributação Atual")
    for tributo, valor in tributos_atuais.items():
        st.write(f"{tributo}: R$ {valor:,.2f}")
    st.write(f"**Total Atual:** R$ {total_atual:,.2f}")

    st.subheader("🏛️ Tributação com Reforma")
    for tributo, valor in tributos_reforma.items():
        st.write(f"{tributo}: R$ {valor:,.2f}")
    st.write(f"**Total Reforma:** R$ {total_reforma:,.2f}")

    st.subheader("📊 Comparativo")
    st.write(f"**Diferença:** R$ {diferenca:,.2f}")
    st.write(f"**Variação da Carga Tributária:** {variacao:.2f}%")

    if variacao > 0:
        st.warning("⚠️ A carga tributária aumentou.")
    elif variacao < 0:
        st.success("✅ A carga tributária reduziu.")
    else:
        st.info("➖ A carga tributária permaneceu igual.")

