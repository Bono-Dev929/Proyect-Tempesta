import streamlit as st
from src.service import procesar_clima
import time
import datetime 


st.set_page_config(page_title="Tempesta - LuLabs", page_icon="⛈️")

st.title("⛈️ Tempesta")
st.subheader("Radar Meteorológico Global by LuLabs")

ciudad_usuario = st.text_input("Ingresa una ciudad (Ej: Tokio, Madrid, Adrogué):", "Jose Marmol, AR")

if st.button("Buscar Clima"):
    with st.spinner("Conectando con el satélite meteorológico... 🛰️"):
        time.sleep(0.8) 
        resultado = procesar_clima(ciudad_usuario)
        
    st.divider() 
    
    if "error" in resultado:
        st.warning(f"⚠️ {resultado['error']}")
    else:
        st.success(f"Datos obtenidos de la estación en: {resultado['ciudad']}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Temperatura", f"{resultado['temperatura']} °C")
            st.metric("Sensacion Termica", f"{resultado['Sensacion Termica']}")
            st.metric("Condición", resultado['descripcion'].title())
            
        with col2:
            st.metric("Humedad", f"{resultado['humedad']} %")
            st.metric("Nubosidad", f"{resultado['nubosidad']} %")
            
        with col3:
            st.metric("Presión", f"{resultado['presion_hpa']} hPa")
            st.metric("Viento", f"{resultado['viento_vel']} m/s")

def renderizar_footer_lucorp():
    
    anio_actual = datetime.datetime.now().year
    
   
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)
    
   
    footer_css = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0B132B; /* Color de fondo de tu tema */
        color: #FFFFFF;
        text-align: center;
        padding: 10px 0;
        font-family: sans-serif;
        border-top: 1px solid #1C2541; /* Línea separadora sutil */
        z-index: 999;
    }
    .footer a {
        color: #00A8E8; /* Tu primaryColor */
        text-decoration: none;
        margin: 0 15px;
        font-size: 20px;
        transition: color 0.3s ease;
    }
    .footer a:hover {
        color: #FFFFFF;
    }
    .footer p {
        margin: 5px 0 0 0;
        font-size: 14px;
        color: #FFFFFF;
    }
    /* Padding para que el contenido principal no se pise con el footer */
    .main .block-container {
        padding-bottom: 70px;
    }
    </style>
    """
    st.markdown(footer_css, unsafe_allow_html=True)
    
    footer_html = f"""
    <div class="footer">
        <div class="social-icons">
            <a href="https://www.linkedin.com/in/lucas-bono/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/Bono-Dev929" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
        </div>
        <p>© {anio_actual} <strong>LuLabs</strong> | Desarrollando ecosistemas tecnológicos.</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


renderizar_footer_lucorp()
