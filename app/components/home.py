"""
Página de Inicio
================

Vista principal con resumen ejecutivo y métricas clave.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from components.data_loader import DataLoader
from config.settings import THEME_COLORS, PLOTLY_CONFIG, DATA_INFO_TEXT


def render_home(data_loader: DataLoader, filters: dict):
    """
    Renderiza la página de inicio con overview del análisis.
    
    Args:
        data_loader: Instancia del cargador de datos
        filters: Diccionario con filtros del usuario
    """
    
    # Header principal
    st.markdown("""
    <h1 class="main-title">🌍 La Gran Migración del Conocimiento</h1>
    <p class="subtitle">
        Análisis de Patrones de Movilidad Científica Global (2000-2016)
    </p>
    """, unsafe_allow_html=True)
    
    # Cargar datos
    df_flows = data_loader.load_flows()
    
    if df_flows.empty:
        st.error("❌ No se pudieron cargar los datos. Verifica la ruta de los archivos.")
        return
    
    # Aplicar filtros
    df_filtered = apply_filters(df_flows, filters)
    
    # =================================================================
    # SECCIÓN 1: MÉTRICAS CLAVE
    # =================================================================
    
    st.markdown('<div class="section-header">📊 Métricas Globales</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_researchers = int(df_filtered['n_researchers'].sum())
        st.metric(
            label="🔬 Total Investigadores",
            value=f"{total_researchers:,}",
            delta="Migrantes identificados",
            help="Número total de investigadores que han migrado entre países"
        )
    
    with col2:
        total_routes = len(df_filtered)
        st.metric(
            label="🛤️ Corredores Migratorios",
            value=f"{total_routes:,}",
            delta="Rutas bilaterales",
            help="Número de corredores únicos (País A → País B). Un corredor es una ruta específica de migración entre dos países, ej: China → USA"
        )
    
    with col3:
        unique_countries = df_filtered['origin'].nunique() + df_filtered['destination'].nunique()
        unique_countries = len(set(df_filtered['origin'].unique()) | set(df_filtered['destination'].unique()))
        st.metric(
            label="🌎 Países Involucrados",
            value=unique_countries,
            delta="En todo el mundo",
            help="Número de países participando en flujos migratorios"
        )
    
    with col4:
        avg_per_route = df_filtered['n_researchers'].mean()
        st.metric(
            label="📈 Promedio por Corredor",
            value=f"{avg_per_route:.1f}",
            delta="Investigadores",
            help="Número promedio de investigadores que transitan cada corredor migratorio"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =================================================================
    # SECCIÓN 2: VISUALIZACIÓN DE MAPA MUNDIAL
    # =================================================================
    
    st.markdown('<div class="section-header">🗺️ Mapa Mundial de Flujos</div>', unsafe_allow_html=True)
    
    # Calcular saldo migratorio neto
    net_migration = data_loader.compute_net_migration(df_filtered)
    
    # Agregar ISO3 para el mapa
    # Crear mapeo desde flows
    iso_map_origin = df_filtered[['origin', 'origin_iso3']].drop_duplicates().rename(
        columns={'origin': 'country', 'origin_iso3': 'iso3'}
    )
    iso_map_dest = df_filtered[['destination', 'destination_iso3']].drop_duplicates().rename(
        columns={'destination': 'country', 'destination_iso3': 'iso3'}
    )
    iso_map = pd.concat([iso_map_origin, iso_map_dest]).drop_duplicates(subset='country')
    
    map_data = net_migration.merge(iso_map, on='country', how='left')
    
    # Crear mapa coroplético
    fig_map = px.choropleth(
        map_data,
        locations='iso3',
        color='net_balance',
        hover_name='country',
        hover_data={
            'immigration': ':,',
            'emigration': ':,',
            'net_balance': ':,',
            'iso3': False
        },
        title='Saldo Migratorio Neto por País',
        color_continuous_scale='RdYlGn',
        color_continuous_midpoint=0,
        labels={
            'net_balance': 'Saldo Neto',
            'immigration': 'Inmigración',
            'emigration': 'Emigración'
        }
    )
    
    fig_map.update_geos(
        showcountries=True, 
        countrycolor="rgba(255,255,255,0.1)",
        bgcolor='rgba(0,0,0,0)'
    )
    
    fig_map.update_layout(
        height=500,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    st.plotly_chart(fig_map, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Interpretación
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="alert-success">
            <strong>🟢 Verde: Países Atractores</strong><br>
            Reciben más investigadores de los que pierden (Brain Gain)
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="alert-warning">
            <strong>🔴 Rojo: Países Exportadores</strong><br>
            Pierden más investigadores de los que reciben (Brain Drain)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =================================================================
    # SECCIÓN 3: TOP ATRACTORES Y EXPORTADORES
    # =================================================================
    
    st.markdown('<div class="section-header">🏆 Rankings Globales</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🟢 Top Países Atractores")
        
        top_attractors = net_migration.head(10)
        
        fig_attractors = px.bar(
            top_attractors,
            x='net_balance',
            y='country',
            orientation='h',
            title='Top 10 Receptores de Talento (Brain Gain)',
            labels={'net_balance': 'Saldo Neto', 'country': 'País'},
            color='net_balance',
            color_continuous_scale='Greens'
        )
        
        fig_attractors.update_traces(
            texttemplate='%{x:,.0f}',
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Saldo Neto: %{x:,.0f}<extra></extra>'
        )
        
        fig_attractors.update_layout(
            height=400,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'},
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_attractors, use_container_width=True, config=PLOTLY_CONFIG)
    
    with col2:
        st.markdown("### 🔴 Top Países Exportadores")
        
        top_exporters = net_migration.tail(10).sort_values('net_balance')
        
        fig_exporters = px.bar(
            top_exporters,
            x='net_balance',
            y='country',
            orientation='h',
            title='Top 10 Exportadores de Talento (Brain Drain)',
            labels={'net_balance': 'Saldo Neto', 'country': 'País'},
            color='net_balance',
            color_continuous_scale='Reds'
        )
        
        fig_exporters.update_traces(
            texttemplate='%{x:,.0f}',
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Saldo Neto: %{x:,.0f}<extra></extra>'
        )
        
        fig_exporters.update_layout(
            height=400,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'},
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_exporters, use_container_width=True, config=PLOTLY_CONFIG)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =================================================================
    # SECCIÓN 4: PRINCIPALES HALLAZGOS
    # =================================================================
    
    st.markdown('<div class="section-header">💡 Principales Hallazgos</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🇺🇸 Estados Unidos: El Coloso del Talento</h3>
            <p>Domina como <strong>receptor absoluto</strong> de talento científico global, 
            con saldo neto de +15,000 a +20,000 investigadores.</p>
            <ul>
                <li>💰 Inversión masiva: ~$550B anuales en I+D</li>
                <li>🏛️ Universidades élite: MIT, Stanford, Harvard</li>
                <li>🌐 Silicon Valley y ecosistemas de innovación</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h3>🇨🇳 China: La Paradoja del Dragón</h3>
            <p><strong>Mayor exportador</strong> pero con estrategia de reversión exitosa.</p>
            <ul>
                <li>📤 Decenas de miles emigran (principalmente a USA)</li>
                <li>📥 Programas agresivos de retorno funcionando</li>
                <li>🔄 De "fuga" a "circulación" de cerebros</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🛤️ Autopistas del Conocimiento</h3>
            <p>Existen <strong>corredores principales</strong> bien definidos:</p>
            <ul>
                <li>🇨🇳→🇺🇸 El corredor más transitado (>10k investigadores)</li>
                <li>🇮🇳→🇺🇸 Segundo flujo más importante</li>
                <li>🇮🇷→🇩🇪 Migración académica + refugio político</li>
                <li>🇬🇧→🇺🇸 Intercambio entre potencias</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h3>💰 El Dinero Importa</h3>
            <p><strong>Correlación fuerte</strong> entre economía y atracción:</p>
            <ul>
                <li>📈 PIB per cápita ↔ Saldo migratorio: +0.65 a +0.75</li>
                <li>🔬 Gasto I+D (% PIB) ↔ Atracción: +0.70 a +0.80</li>
                <li>🎓 Densidad de investigadores auto-refuerza</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =================================================================
    # SECCIÓN 5: FUENTES DE DATOS
    # =================================================================
    
    with st.expander("📊 Información sobre Fuentes de Datos"):
        st.markdown(DATA_INFO_TEXT)


def apply_filters(df: 'pd.DataFrame', filters: dict) -> 'pd.DataFrame':
    """
    Aplica filtros del usuario al DataFrame.
    
    Args:
        df: DataFrame de flujos migratorios
        filters: Diccionario con filtros seleccionados
        
    Returns:
        DataFrame filtrado
    """
    df_filtered = df.copy()
    
    # Filtro por regiones de origen
    if filters.get('origin_regions'):
        df_filtered = df_filtered[df_filtered['origin_region'].isin(filters['origin_regions'])]
    
    # Filtro por regiones de destino
    if filters.get('dest_regions'):
        df_filtered = df_filtered[df_filtered['destination_region'].isin(filters['dest_regions'])]
    
    # Filtro por rango de años
    if 'year_range' in filters and 'phd_year_mean' in df_filtered.columns:
        year_min, year_max = filters['year_range']
        df_filtered = df_filtered[
            (df_filtered['phd_year_mean'] >= year_min) &
            (df_filtered['phd_year_mean'] <= year_max)
        ]
    
    # Filtro por flujo mínimo
    if 'min_researchers' in filters:
        df_filtered = df_filtered[df_filtered['n_researchers'] >= filters['min_researchers']]
    
    return df_filtered
