"""
Sidebar: Navegación y Filtros
==============================

Componente de sidebar con menú de navegación y filtros interactivos.
"""

import streamlit as st
from typing import Dict
from components.data_loader import DataLoader
from config.settings import ABOUT_TEXT, YEAR_MIN, YEAR_MAX, TOP_N_DEFAULT


def render_sidebar(data_loader: DataLoader) -> Dict:
    """
    Renderiza el sidebar con navegación y filtros.
    
    Args:
        data_loader: Instancia del cargador de datos
        
    Returns:
        Diccionario con filtros seleccionados por el usuario
    """
    
    with st.sidebar:
        # Logo y título
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='font-size: 2rem;'>🌍🔬</h1>
            <h2 style='font-size: 1.3rem; margin: 0;'>Migración Científica</h2>
            <p style='color: #6C757D; font-size: 0.9rem;'>Panel de Inteligencia</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # =================================================================
        # NAVEGACIÓN PRINCIPAL
        # =================================================================
        
        st.markdown("### 📑 Navegación")
        
        page = st.radio(
            "Selecciona una sección:",
            [
                "Inicio",
                "Análisis Exploratorio (EDA)",
                "Conclusiones",
                "Machine Learning"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # =================================================================
        # FILTROS INTERACTIVOS
        # =================================================================
        
        st.markdown("### 🎛️ Filtros")
        
        # Cargar datos para opciones de filtro
        df_flows = data_loader.load_flows()
        
        if not df_flows.empty:
            
            # Filtro: Regiones
            st.markdown("**🌍 Regiones**")
            
            all_regions = sorted(df_flows['origin_region'].unique())
            
            selected_origin_regions = st.multiselect(
                "Regiones de Origen",
                options=all_regions,
                default=all_regions,
                help="Filtra por región de origen de investigadores"
            )
            
            selected_dest_regions = st.multiselect(
                "Regiones de Destino",
                options=all_regions,
                default=all_regions,
                help="Filtra por región de destino de investigadores"
            )
            
            # Filtro: Rango de años
            st.markdown("**📅 Período Temporal**")
            
            year_range = st.slider(
                "Rango de años de doctorado",
                min_value=int(df_flows['phd_year_min'].min()) if 'phd_year_min' in df_flows.columns else YEAR_MIN,
                max_value=int(df_flows['phd_year_max'].max()) if 'phd_year_max' in df_flows.columns else YEAR_MAX,
                value=(1990, 2016),
                help="Filtra flujos por año de obtención del doctorado"
            )
            
            # Filtro: Flujo mínimo
            st.markdown("**🔢 Volumen de Flujo**")
            
            min_researchers = st.number_input(
                "Mínimo de investigadores por ruta",
                min_value=1,
                max_value=100,
                value=5,
                step=1,
                help="Muestra solo rutas con al menos N investigadores"
            )
            
            # Filtro: Top N
            st.markdown("**🏆 Top Rankings**")
            
            top_n = st.slider(
                "Número de países en rankings",
                min_value=5,
                max_value=30,
                value=TOP_N_DEFAULT,
                step=5,
                help="Cantidad de países a mostrar en visualizaciones top"
            )
            
        else:
            st.warning("⚠️ No hay datos disponibles para filtros")
            selected_origin_regions = []
            selected_dest_regions = []
            year_range = (1990, 2016)
            min_researchers = 5
            top_n = TOP_N_DEFAULT
        
        st.markdown("---")
        
        # =================================================================
        # INFORMACIÓN Y AYUDA
        # =================================================================
        
        with st.expander("ℹ️ Acerca de este panel"):
            st.markdown(ABOUT_TEXT)
        
        with st.expander("📊 Estado de datos"):
            if not df_flows.empty:
                stats = data_loader.get_summary_stats(df_flows)
                st.markdown(f"""
                **Datasets cargados:**
                - ✅ Flujos migratorios: {stats['total_routes']:,} rutas
                - ✅ Total investigadores: {stats['total_researchers']:,}
                - ✅ Países origen: {stats['unique_origins']}
                - ✅ Países destino: {stats['unique_destinations']}
                """)
            else:
                st.error("❌ No se pudieron cargar los datos")
        
        # Footer del sidebar
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; font-size: 0.8rem; color: #6C757D;'>
            <p>Versión 1.0.0</p>
            <p>Datos: 2000-2016</p>
        </div>
        """, unsafe_allow_html=True)
    
    # =================================================================
    # RETORNAR CONFIGURACIÓN DE FILTROS
    # =================================================================
    
    return {
        'page': page,
        'origin_regions': selected_origin_regions,
        'dest_regions': selected_dest_regions,
        'year_range': year_range,
        'min_researchers': min_researchers,
        'top_n': top_n
    }
