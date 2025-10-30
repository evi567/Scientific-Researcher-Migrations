"""
Panel de Inteligencia: Migración Científica Global
==================================================

Aplicación Streamlit para visualizar y analizar patrones de migración 
de investigadores científicos a nivel mundial.

Autor: Análisis de Movilidad Científica
Fecha: Octubre 2025
"""

import streamlit as st
from pathlib import Path
import sys

# Añadir el directorio de componentes al path
sys.path.insert(0, str(Path(__file__).parent))

# Importar componentes modulares
from components.data_loader import DataLoader
from components.sidebar import render_sidebar
from components.home import render_home
from components.eda import render_eda
from components.conclusions import render_conclusions
from components.ml import render_ml
from config.settings import PAGE_CONFIG, THEME_COLORS


# =============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# =============================================================================

def setup_page():
    """Configura la página inicial de Streamlit con tema personalizado."""
    st.set_page_config(**PAGE_CONFIG)
    
    # CSS personalizado para mejorar UX/UI
    st.markdown(f"""
    <style>
        /* Paleta de colores principal */
        :root {{
            --primary-color: {THEME_COLORS['primary']};
            --secondary-color: {THEME_COLORS['secondary']};
            --accent-color: {THEME_COLORS['accent']};
            --success-color: {THEME_COLORS['success']};
            --warning-color: {THEME_COLORS['warning']};
            --background-color: #0E1117;
            --card-background: #1E2128;
        }}
        
        /* Estilo de tarjetas */
        .metric-card {{
            background: var(--card-background);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 4px solid var(--primary-color);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }}
        
        .metric-card h3, .metric-card h4, .metric-card p, .metric-card li, .metric-card ul {{
            color: #E8E8E8;
        }}
        
        .metric-card strong, .metric-card em {{
            color: #FAFAFA;
        }}
        
        /* Títulos principales */
        .main-title {{
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            text-align: center;
        }}
        
        .subtitle {{
            font-size: 1.2rem;
            color: #B0B3B8;
            text-align: center;
            margin-bottom: 2rem;
        }}
        
        /* Secciones */
        .section-header {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white !important;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin: 2rem 0 1rem 0;
            font-size: 1.5rem;
            font-weight: 600;
        }}
        
        /* Sidebar personalizado */
        .css-1d391kg {{
            background-color: var(--card-background);
        }}
        
        /* Botones */
        .stButton>button {{
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        
        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }}
        
        /* Métricas */
        [data-testid="stMetricValue"] {{
            font-size: 2rem;
            font-weight: 700;
        }}
        
        /* Gráficos Plotly */
        .js-plotly-plot {{
            border-radius: 10px;
            overflow: hidden;
        }}
        
        /* NO aplicar estilos globales a elementos nativos de Streamlit */
        
        /* Tablas */
        .dataframe {{
            border-radius: 8px;
            overflow: hidden;
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 2rem;
            color: #6C757D;
            border-top: 1px solid #2E3338;
            margin-top: 3rem;
        }}
    </style>
    """, unsafe_allow_html=True)


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """Función principal que orquesta la aplicación Streamlit."""
    
    # Configurar página
    setup_page()
    
    # Inicializar cargador de datos (con caché)
    data_loader = DataLoader()
    
    # Renderizar sidebar y obtener configuración de usuario
    filters = render_sidebar(data_loader)
    
    # Navegación basada en selección del usuario
    page = filters.get('page', 'Inicio')
    
    # Renderizar página seleccionada
    if page == "Inicio":
        render_home(data_loader, filters)
    
    elif page == "Análisis Exploratorio (EDA)":
        render_eda(data_loader, filters)
    
    elif page == "Conclusiones":
        render_conclusions(data_loader, filters)
    
    elif page == "Machine Learning":
        render_ml(data_loader, filters)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>🌍 <strong>Panel de Inteligencia: Migración Científica Global</strong></p>
        <p>Datos: ORCID + World Development Indicators (Banco Mundial) | Análisis: 2000-2016</p>
        <p style="font-size: 0.9rem; color: #6C757D;">
            Desarrollado con ❤️ usando Streamlit, Plotly y Python
        </p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    main()
