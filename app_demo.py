import streamlit as st
import pandas as pd
import time
import re

# --- CONFIGURACIÓN CORPORATIVA ---
st.set_page_config(page_title="OmniLogistics OS | Demo", page_icon="🌐", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .titulo-principal { color: #ffffff; font-family: 'Arial Black', sans-serif; font-size: 28px; border-bottom: 3px solid #d4af37; padding-bottom: 10px; margin-bottom: 20px; text-transform: uppercase; }
    .kpi-card { background-color: #1a1c23; border-left: 5px solid #d4af37; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .kpi-title { color: #a0aec0; font-size: 12px; text-transform: uppercase; font-weight: bold; margin-bottom: 5px; }
    .kpi-value { color: #ffffff; font-size: 28px; font-weight: 900; margin: 0; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE EXTRACCIÓN DE DATOS ---
@st.cache_data(ttl=60)
def leer_google_sheet_publico(url):
    try:
        # Extraer el ID del documento de la URL
        match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
        if not match: return None, None, None
        doc_id = match.group(1)
        
        # Construir URLs de exportación CSV para las 3 pestañas (gid 0, 1 y 2 por defecto)
        url_catalogo = f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid=0"
        url_inventario = f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv&gid=1110052733" # Reemplazaremos los gid dinámicamente si falla
        
        # Leemos directo con Pandas
        df_catalogo = pd.read_csv(url_catalogo)
        
        # Para el inventario y operaciones, forzamos lectura de las primeras hojas
        xls = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format=xlsx")
        hojas = xls.sheet_names
        df_inv = pd.read_excel(xls, sheet_name=hojas[1]) if len(hojas) > 1 else pd.DataFrame()
        df_oper = pd.read_excel(xls, sheet_name=hojas[2]) if len(hojas) > 2 else pd.DataFrame()
        
        return df_catalogo, df_inv, df_oper
    except Exception as e:
        return None, None, None

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("## 🌐 OmniLogistics OS")
    st.caption("Arquitectura B2B de Alto Rendimiento")
    st.markdown("---")
    menu = st.radio("Módulos Operativos:", [
        "📊 1. Command Center (Dashboard)",
        "⚙️ 2. Motor de Costos (Smart Split)",
        "🛡️ 3. Auditoría en la Nube"
    ])
    st.markdown("---")
    url_input = st.text_input("🔗 Conectar Base de Datos:", placeholder="Pega la URL de tu Google Sheet aquí...")

# --- MÓDULO 1: COMMAND CENTER ---
if menu == "📊 1. Command Center (Dashboard)":
    st.markdown("<div class='titulo-principal'>Centro de Mando Logístico</div>", unsafe_allow_html=True)
    
    if not url_input:
        st.info("👈 Pega el enlace de tu Google Sheet público en la barra lateral para sincronizar el sistema.")
    else:
        with st.spinner("Extrayendo datos de la bóveda..."):
            df_cat, df_inv, df_op = leer_google_sheet_publico(url_input)
            
            if df_cat is not None:
                st.success("✅ Conexión establecida. Datos sincronizados en tiempo real.")
                
                # Cálculos rápidos para KPIs
                total_lotes = len(df_inv) if not df_inv.empty else 0
                total_mat = len(df_cat) if not df_cat.empty else 0
                cant_total = df_inv['CANTIDAD_DISPONIBLE'].sum() if not df_inv.empty and 'CANTIDAD_DISPONIBLE' in df_inv.columns else 0
                
                c1, c2, c3, c4 = st.columns(4)
                c1.markdown(f"<div class='kpi-card'><div class='kpi-title'>Materiales Activos</div><p class='kpi-value'>{total_mat}</p></div>", unsafe_allow_html=True)
                c2.markdown(f"<div class='kpi-card' style='border-left-color: #28a745;'><div class='kpi-title'>Lotes en Bodega</div><p class='kpi-value'>{total_lotes}</p></div>", unsafe_allow_html=True)
                c3.markdown(f"<div class='kpi-card' style='border-left-color: #17a2b8;'><div class='kpi-title'>Volumen Total</div><p class='kpi-value'>{cant_total:,.2f}</p></div>", unsafe_allow_html=True)
                c4.markdown(f"<div class='kpi-card' style='border-left-color: #dc3545;'><div class='kpi-title'>Alertas de Vencimiento</div><p class='kpi-value'>0</p></div>", unsafe_allow_html=True)
                
                st.markdown("### 📦 Inventario Global Sincronizado")
                if not df_inv.empty:
                    st.dataframe(df_inv, use_container_width=True, hide_index=True)
                else:
                    st.warning("No se encontraron datos de inventario.")
            else:
                st.error("🚨 Error de conexión. Verifica que el enlace sea correcto y que el archivo tenga permisos de 'Cualquier persona con el enlace'.")

elif menu == "⚙️ 2. Motor de Costos (Smart Split)":
    st.markdown("<div class='titulo-principal'>Motor de Prorrateo Dinámico</div>", unsafe_allow_html=True)
    st.warning("🚧 Módulo en construcción. Conecta los datos en el Dashboard primero.")

elif menu == "🛡️ 3. Auditoría en la Nube":
    st.markdown("<div class='titulo-principal'>Auditoría y Sincronización</div>", unsafe_allow_html=True)
    st.warning("🚧 Módulo en construcción. Conecta los datos en el Dashboard primero.")
