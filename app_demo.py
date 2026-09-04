import streamlit as st
import pandas as pd
import time

# --- CONFIGURACIÓN CORPORATIVA ---
st.set_page_config(page_title="OmniLogistics OS | Demo", page_icon="🌐", layout="wide")

# CSS Inyectado para estética Premium (Dark Mode B2B)
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .titulo-principal { color: #ffffff; font-family: 'Arial Black', sans-serif; font-size: 32px; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; }
    .kpi-card { background-color: #1a1c23; border-left: 5px solid #d4af37; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .kpi-title { color: #a0aec0; font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 5px; }
    .kpi-value { color: #ffffff; font-size: 28px; font-weight: 900; margin: 0; }
    .stSidebar { background-color: #11141a; }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (MENÚ DE VENTAS) ---
with st.sidebar:
    st.markdown("## 🌐 OmniLogistics OS")
    st.caption("Arquitectura B2B de Alto Rendimiento")
    st.markdown("---")
    menu = st.radio("Módulos Operativos:", [
        "📊 1. Command Center (Dashboard)",
        "⚙️ 2. Motor de Costos (Smart Split)",
        "🛡️ 3. Auditoría en la Nube (Modo Dios)"
    ])
    st.markdown("---")
    st.info("💡 **Modo Demo:** Conectado a Google Cloud en tiempo real.")

# --- MÓDULO 1: COMMAND CENTER ---
if menu == "📊 1. Command Center (Dashboard)":
    st.markdown("<div class='titulo-principal'>📊 Centro de Mando Logístico</div>", unsafe_allow_html=True)
    
    st.write("Visión general de la operación sincronizada en tiempo real con Google Workspace.")
    
    # KPIs Simulados para impacto visual
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown("<div class='kpi-card'><div class='kpi-title'>Valor Inventario</div><p class='kpi-value'>$1.2M</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='kpi-card' style='border-left-color: #28a745;'><div class='kpi-title'>Lotes Activos</div><p class='kpi-value'>342</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='kpi-card' style='border-left-color: #dc3545;'><div class='kpi-title'>Alertas de Vencimiento</div><p class='kpi-value'>3</p></div>", unsafe_allow_html=True)
    c4.markdown("<div class='kpi-card' style='border-left-color: #17a2b8;'><div class='kpi-title'>Precisión de Datos</div><p class='kpi-value'>100%</p></div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Placeholder para la conexión a Drive
    st.markdown("### 📡 Conexión a Base de Datos (Google Sheets)")
    url_input = st.text_input("🔗 URL de la Bóveda de Datos (Solo Lectura):", placeholder="Pega aquí el enlace de tu Google Sheet...")
    
    if url_input:
        with st.spinner("Conectando con servidores de Google..."):
            time.sleep(1.5) # Simulación de carga
            st.success("✅ ¡Conexión establecida con éxito! En el próximo paso inyectaremos los datos aquí.")

elif menu == "⚙️ 2. Motor de Costos (Smart Split)":
    st.markdown("<div class='titulo-principal'>⚙️ Motor de Prorrateo Dinámico</div>", unsafe_allow_html=True)
    st.warning("🚧 Módulo en construcción. Aquí demostraremos tu lógica matemática.")

elif menu == "🛡️ 3. Auditoría en la Nube (Modo Dios)":
    st.markdown("<div class='titulo-principal'>🛡️ Auditoría y Sincronización Bidireccional</div>", unsafe_allow_html=True)
    st.warning("🚧 Módulo en construcción. Aquí instalaremos la tabla editable que inyecta datos a Drive.")
