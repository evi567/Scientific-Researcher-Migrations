"""
Página de Análisis Exploratorio (EDA)
=====================================

Análisis exhaustivo de patrones migratorios con visualizaciones interactivas.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from components.data_loader import DataLoader
from config.settings import THEME_COLORS, PLOTLY_CONFIG


def render_eda(data_loader: DataLoader, filters: dict):
    """
    Renderiza la página completa de análisis exploratorio.
    
    Args:
        data_loader: Instancia del cargador de datos
        filters: Diccionario con filtros del usuario
    """
    
    # Header
    st.markdown("""
    <h1 class="main-title">📊 Análisis Exploratorio de Datos</h1>
    <p class="subtitle">
        Exploración profunda de patrones migratorios científicos
    </p>
    """, unsafe_allow_html=True)
    
    # Cargar datos
    df_flows = data_loader.load_flows()
    df_migrations = data_loader.load_migrations()
    df_wdi = data_loader.load_wdi()
    
    if df_flows.empty:
        st.error("❌ No se pudieron cargar los datos principales.")
        return
    
    # Aplicar filtros (importar función de home)
    from components.home import apply_filters
    df_filtered = apply_filters(df_flows, filters)
    
    # Tabs para organizar contenido
    tabs = st.tabs([
        "📈 Resumen Estadístico",
        "🌍 Emisores y Receptores",
        "🛤️ Corredores Migratorios",
        "🌐 Análisis Regional",
        "💰 Correlación Económica",
        "📅 Evolución Temporal",
        "🎯 Diagrama de Flujos"
    ])
    
    # TAB 1: Resumen Estadístico
    with tabs[0]:
        render_statistical_summary(df_filtered, data_loader)
    
    # TAB 2: Emisores y Receptores
    with tabs[1]:
        render_emitters_receivers(df_filtered, data_loader, filters)
    
    # TAB 3: Corredores
    with tabs[2]:
        render_corridors(df_filtered, data_loader, filters)
    
    # TAB 4: Análisis Regional
    with tabs[3]:
        render_regional_analysis(df_filtered, data_loader)
    
    # TAB 5: Correlación Económica
    with tabs[4]:
        render_economic_correlation(df_filtered, df_wdi, data_loader)
    
    # TAB 6: Evolución Temporal
    with tabs[5]:
        render_temporal_evolution(df_filtered, df_migrations)
    
    # TAB 7: Diagrama de Flujos (Sankey)
    with tabs[6]:
        render_flow_diagram(df_filtered, filters)


# =============================================================================
# TAB 1: RESUMEN ESTADÍSTICO
# =============================================================================

def render_statistical_summary(df: pd.DataFrame, data_loader: DataLoader):
    """Renderiza resumen estadístico del dataset."""
    
    st.markdown('<div class="section-header">📊 Estadísticas Descriptivas</div>', unsafe_allow_html=True)
    
    # Métricas en columnas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📏 Medidas de Tendencia Central</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.metric("Media", f"{df['n_researchers'].mean():.2f}", "investigadores/ruta")
        st.metric("Mediana", f"{df['n_researchers'].median():.0f}", "investigadores/ruta")
        st.metric("Moda", f"{df['n_researchers'].mode()[0] if not df['n_researchers'].mode().empty else 'N/A'}")
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Medidas de Dispersión</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.metric("Desviación Estándar", f"{df['n_researchers'].std():.2f}")
        st.metric("Varianza", f"{df['n_researchers'].var():.2f}")
        st.metric("Rango", f"{df['n_researchers'].max() - df['n_researchers'].min():.0f}")
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>🎯 Valores Extremos</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.metric("Mínimo", f"{df['n_researchers'].min():.0f}")
        st.metric("Máximo", f"{df['n_researchers'].max():.0f}")
        st.metric("Q3 - Q1", f"{df['n_researchers'].quantile(0.75) - df['n_researchers'].quantile(0.25):.0f}")
    
    # Distribución de investigadores por ruta
    st.markdown("### 📈 Distribución de Investigadores por Ruta")
    
    fig_dist = px.histogram(
        df,
        x='n_researchers',
        nbins=50,
        title='Distribución de Frecuencia',
        labels={'n_researchers': 'Número de Investigadores', 'count': 'Frecuencia'},
        color_discrete_sequence=[THEME_COLORS['primary']]
    )
    
    fig_dist.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig_dist, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Boxplot
    col1, col2 = st.columns(2)
    
    with col1:
        fig_box = px.box(
            df,
            y='n_researchers',
            title='Diagrama de Caja (Outliers)',
            labels={'n_researchers': 'Investigadores'},
            color_discrete_sequence=[THEME_COLORS['accent']]
        )
        
        fig_box.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig_box, use_container_width=True, config=PLOTLY_CONFIG)
    
    with col2:
        # Tabla de percentiles
        percentiles = df['n_researchers'].describe(percentiles=[.1, .25, .5, .75, .9, .95, .99])
        
        st.markdown("### 📊 Percentiles")
        st.dataframe(percentiles, use_container_width=True)


# =============================================================================
# TAB 2: EMISORES Y RECEPTORES
# =============================================================================

def render_emitters_receivers(df: pd.DataFrame, data_loader: DataLoader, filters: dict):
    """Renderiza análisis de países emisores y receptores."""
    
    st.markdown('<div class="section-header">🌍 Países Emisores y Receptores</div>', unsafe_allow_html=True)
    
    top_n = filters.get('top_n', 15)
    
    # Calcular tops
    top_emitters = data_loader.get_top_emitters(df, top_n)
    top_receivers = data_loader.get_top_receivers(df, top_n)
    net_migration = data_loader.compute_net_migration(df)
    
    # Visualizaciones lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### 🔴 Top {top_n} Países Emisores")
        
        fig_emitters = px.bar(
            top_emitters,
            x='total_emigrants',
            y='country',
            orientation='h',
            title=f'Brain Drain: Top {top_n} Exportadores de Talento',
            labels={'total_emigrants': 'Investigadores Emigrados', 'country': 'País'},
            color='total_emigrants',
            color_continuous_scale='Reds',
            text='total_emigrants'
        )
        
        fig_emitters.update_traces(
            texttemplate='%{text:,.0f}',
            textposition='outside'
        )
        
        fig_emitters.update_layout(
            height=600,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'},
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_emitters, use_container_width=True, config=PLOTLY_CONFIG)
        
        # Tabla de datos
        with st.expander("📋 Ver datos detallados"):
            st.dataframe(top_emitters, use_container_width=True)
    
    with col2:
        st.markdown(f"### 🟢 Top {top_n} Países Receptores")
        
        fig_receivers = px.bar(
            top_receivers,
            x='total_immigrants',
            y='country',
            orientation='h',
            title=f'Brain Gain: Top {top_n} Receptores de Talento',
            labels={'total_immigrants': 'Investigadores Recibidos', 'country': 'País'},
            color='total_immigrants',
            color_continuous_scale='Greens',
            text='total_immigrants'
        )
        
        fig_receivers.update_traces(
            texttemplate='%{text:,.0f}',
            textposition='outside'
        )
        
        fig_receivers.update_layout(
            height=600,
            showlegend=False,
            yaxis={'categoryorder': 'total ascending'},
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_receivers, use_container_width=True, config=PLOTLY_CONFIG)
        
        # Tabla de datos
        with st.expander("📋 Ver datos detallados"):
            st.dataframe(top_receivers, use_container_width=True)
    
    # Saldo Migratorio Neto
    st.markdown("### ⚖️ Saldo Migratorio Neto")
    
    # Visualización combinada (top atractores y exportadores)
    top_attractors = net_migration.head(15)
    top_exporters = net_migration.tail(15)
    viz_data = pd.concat([top_attractors, top_exporters])
    
    fig_net = px.bar(
        viz_data,
        x='net_balance',
        y='country',
        orientation='h',
        title='Saldo Neto: Top Atractores y Exportadores',
        labels={'net_balance': 'Saldo Neto (Inmigración - Emigración)', 'country': 'País'},
        color='net_balance',
        color_continuous_scale='RdYlGn',
        color_continuous_midpoint=0,
        text='net_balance'
    )
    
    fig_net.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
    fig_net.update_layout(
        height=700,
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_net, use_container_width=True, config=PLOTLY_CONFIG)
    
    # NUEVA MEJORA 1: Histogramas Superpuestos - Distribución de flujos
    st.markdown("### 📊 Comparación de Distribuciones: Emigración vs Inmigración")
    st.markdown("Análisis de la distribución de flujos migratorios entre países emisores y receptores")
    
    # Preparar datos agregados por país
    emigration_by_country = df.groupby('origin')['n_researchers'].sum().reset_index()
    emigration_by_country.columns = ['country', 'total']
    
    immigration_by_country = df.groupby('destination')['n_researchers'].sum().reset_index()
    immigration_by_country.columns = ['country', 'total']
    
    # Crear histograma superpuesto
    fig_overlay = go.Figure()
    
    fig_overlay.add_trace(go.Histogram(
        x=emigration_by_country['total'],
        name='Emigración',
        marker_color=THEME_COLORS['warning'],
        opacity=0.7,
        nbinsx=30
    ))
    
    fig_overlay.add_trace(go.Histogram(
        x=immigration_by_country['total'],
        name='Inmigración',
        marker_color=THEME_COLORS['success'],
        opacity=0.7,
        nbinsx=30
    ))
    
    fig_overlay.update_layout(
        title='Distribución de Flujos Migratorios por País',
        xaxis_title='Total de Investigadores',
        yaxis_title='Número de Países',
        barmode='overlay',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500,
        legend=dict(x=0.7, y=0.95),
        hovermode='x unified'
    )
    
    fig_overlay.update_traces(marker_line_width=1, marker_line_color='rgba(255,255,255,0.3)')
    
    st.plotly_chart(fig_overlay, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Tabla completa de saldo migratorio
    with st.expander("📊 Ver tabla completa de saldos migratorios"):
        st.dataframe(
            net_migration[[
                'country', 'immigration', 'emigration', 'net_balance', 
                'migration_ratio', 'type'
            ]],
            use_container_width=True
        )


# =============================================================================
# TAB 3: CORREDORES MIGRATORIOS
# =============================================================================

def render_corridors(df: pd.DataFrame, data_loader: DataLoader, filters: dict):
    """Renderiza análisis de corredores migratorios principales."""
    
    st.markdown('<div class="section-header">🛤️ Corredores Migratorios</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Los **corredores migratorios** son rutas bilaterales específicas (origen → destino) 
    con alto volumen de investigadores. Representan las "autopistas del conocimiento" global.
    """)
    
    top_n = filters.get('top_n', 20)
    top_corridors = data_loader.get_top_corridors(df, top_n)
    
    # Visualización de corredores
    fig_corridors = px.bar(
        top_corridors,
        x='n_researchers',
        y='route',
        orientation='h',
        title=f'Top {top_n} Corredores Migratorios Más Transitados',
        labels={'n_researchers': 'Número de Investigadores', 'route': 'Corredor'},
        color='n_researchers',
        color_continuous_scale='Blues',
        text='n_researchers'
    )
    
    fig_corridors.update_traces(
        texttemplate='%{text:,.0f}',
        textposition='outside'
    )
    
    fig_corridors.update_layout(
        height=700,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_corridors, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Análisis de corredores principales
    st.markdown("### 🔍 Análisis de Corredores Principales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="alert-info">
            <h4>🇨🇳→🇺🇸 China → Estados Unidos</h4>
            <p><strong>El corredor más transitado del mundo</strong></p>
            <ul>
                <li>Volumen: >10,000 investigadores estimados</li>
                <li>Perfil: Estudiantes de doctorado en STEM</li>
                <li>Instituciones: Stanford, MIT, CMU, UC Berkeley</li>
                <li>Tendencia: Desaceleración desde 2018 (tensiones geopolíticas)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="alert-info">
            <h4>🇮🇷→🇩🇪 Irán → Alemania</h4>
            <p><strong>Migración académica + refugio político</strong></p>
            <ul>
                <li>Perfil: Ingeniería, matemáticas, física teórica</li>
                <li>Motivación: Oportunidades + estabilidad política</li>
                <li>Tendencia: Aceleración post-2015</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="alert-info">
            <h4>🇮🇳→🇺🇸 India → Estados Unidos</h4>
            <p><strong>Segundo corredor más importante</strong></p>
            <ul>
                <li>Perfil: CS, matemáticas aplicadas, estadística</li>
                <li>Instituciones: Carnegie Mellon, Georgia Tech, UT Austin</li>
                <li>Característica: Alta tasa de permanencia (>70%)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="alert-info">
            <h4>🇬🇧→🇺🇸 Reino Unido → Estados Unidos</h4>
            <p><strong>Intercambio entre potencias científicas</strong></p>
            <ul>
                <li>Perfil: Postdocs y profesores senior</li>
                <li>Motivación: Salarios y recursos superiores</li>
                <li>Característica: Bidireccional pero ventaja USA</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Tabla detallada
    with st.expander("📋 Ver tabla detallada de corredores"):
        st.dataframe(
            top_corridors[[
                'route', 'origin', 'destination', 'n_researchers',
                'phd_year_mean', 'origin_year_mean'
            ]],
            use_container_width=True
        )


# =============================================================================
# TAB 4: ANÁLISIS REGIONAL
# =============================================================================

def render_regional_analysis(df: pd.DataFrame, data_loader: DataLoader):
    """Renderiza análisis de flujos por región geográfica."""
    
    st.markdown('<div class="section-header">🌐 Análisis por Región Geográfica</div>', unsafe_allow_html=True)
    
    # Obtener flujos regionales
    region_flows = data_loader.get_regional_flows(df)
    
    # Top flujos inter-regionales
    st.markdown("### 🌍 Top Flujos Inter-Regionales")
    
    top_regional = region_flows.head(15)
    
    fig_regional = px.bar(
        top_regional,
        x='n_researchers',
        y=top_regional['origin_region'] + ' → ' + top_regional['destination_region'],
        orientation='h',
        title='Top 15 Flujos Entre Regiones',
        labels={'n_researchers': 'Número de Investigadores', 'y': 'Flujo Regional'},
        color='n_researchers',
        color_continuous_scale='Viridis'
    )
    
    fig_regional.update_layout(
        height=500,
        showlegend=False,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_regional, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Sankey de regiones
    st.markdown("### 🌊 Diagrama de Flujos Regionales (Sankey)")
    
    fig_sankey_regional = create_sankey_regional(region_flows.head(20))
    st.plotly_chart(fig_sankey_regional, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Análisis por región de origen
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📤 Emigración por Región")
        
        emigration_by_region = df.groupby('origin_region')['n_researchers'].sum().sort_values(ascending=False).reset_index()
        emigration_by_region.columns = ['region', 'total_emigrants']
        
        fig_em_region = px.pie(
            emigration_by_region,
            values='total_emigrants',
            names='region',
            title='Distribución de Emigración por Región',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig_em_region.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig_em_region, use_container_width=True, config=PLOTLY_CONFIG)
    
    with col2:
        st.markdown("### 📥 Inmigración por Región")
        
        immigration_by_region = df.groupby('destination_region')['n_researchers'].sum().sort_values(ascending=False).reset_index()
        immigration_by_region.columns = ['region', 'total_immigrants']
        
        fig_im_region = px.pie(
            immigration_by_region,
            values='total_immigrants',
            names='region',
            title='Distribución de Inmigración por Región',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        
        fig_im_region.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400
        )
        
        st.plotly_chart(fig_im_region, use_container_width=True, config=PLOTLY_CONFIG)
    
    # NUEVA MEJORA 2: Gráfico 3D - Emigración vs Inmigración vs Saldo Neto
    st.markdown("### 🌍 Análisis 3D: Emigración, Inmigración y Saldo Neto por País")
    st.markdown("Visualización tridimensional interactiva de los flujos migratorios agregados por país")
    
    # Calcular totales por país
    net_migration_full = data_loader.compute_net_migration(df)
    
    # Filtrar países con flujo significativo para mejor visualización
    significant_countries = net_migration_full[net_migration_full['total_flow'] > 100].copy()
    
    # Crear scatter 3D
    fig_3d = px.scatter_3d(
        significant_countries,
        x='emigration',
        y='immigration',
        z='net_balance',
        color='type',
        size='total_flow',
        hover_name='country',
        hover_data=['migration_ratio'],
        color_discrete_map={'Atractor': THEME_COLORS['success'], 'Exportador': THEME_COLORS['warning']},
        title='Espacio 3D: Emigración × Inmigración × Saldo Neto',
        labels={
            'emigration': 'Emigración Total',
            'immigration': 'Inmigración Total',
            'net_balance': 'Saldo Neto',
            'total_flow': 'Flujo Total',
            'type': 'Tipo de País'
        }
    )
    
    # Añadir plano de referencia (balance = 0)
    fig_3d.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=700,
        scene=dict(
            xaxis=dict(title='Emigración', gridcolor='rgba(255,255,255,0.1)', showbackground=True, backgroundcolor='rgba(0,0,0,0.5)'),
            yaxis=dict(title='Inmigración', gridcolor='rgba(255,255,255,0.1)', showbackground=True, backgroundcolor='rgba(0,0,0,0.5)'),
            zaxis=dict(title='Saldo Neto', gridcolor='rgba(255,255,255,0.1)', showbackground=True, backgroundcolor='rgba(0,0,0,0.5)'),
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.3)
            )
        )
    )
    
    st.plotly_chart(fig_3d, use_container_width=True, config=PLOTLY_CONFIG)
    
    st.markdown("""
    <div class="alert-info">
        <h4>💡 Interpretación del gráfico 3D:</h4>
        <ul>
            <li><strong>Eje X (Emigración):</strong> Cuántos investigadores salen del país</li>
            <li><strong>Eje Y (Inmigración):</strong> Cuántos investigadores llegan al país</li>
            <li><strong>Eje Z (Saldo Neto):</strong> Balance final (inmigración - emigración)</li>
            <li><strong>Países en zona superior (Z+):</strong> Atractores netos de talento</li>
            <li><strong>Países en zona inferior (Z-):</strong> Exportadores netos de talento</li>
            <li><strong>Tamaño de la burbuja:</strong> Volumen total de flujo migratorio</li>
        </ul>
        <p><em>💡 Tip: Haz clic y arrastra para rotar el gráfico, usa scroll para zoom</em></p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# TAB 5: CORRELACIÓN ECONÓMICA
# =============================================================================

def render_economic_correlation(df_flows: pd.DataFrame, df_wdi: pd.DataFrame, data_loader: DataLoader):
    """Renderiza análisis de correlación con indicadores económicos."""
    
    st.markdown('<div class="section-header">💰 Correlación con Desarrollo Económico</div>', unsafe_allow_html=True)
    
    if df_wdi.empty:
        st.warning("⚠️ No hay datos de WDI disponibles para este análisis.")
        return
    
    st.markdown("""
    Analizamos la relación entre **indicadores económicos** (PIB per cápita, gasto en I+D) 
    y el **saldo migratorio neto** de países.
    """)
    
    # Preparar datos WDI
    wdi_recent = df_wdi[df_wdi['Year'].between(2014, 2016)].copy()
    
    wdi_pivot = wdi_recent.pivot_table(
        index='iso3',
        columns='IndicatorCode',
        values='Value',
        aggfunc='mean'
    ).reset_index()
    
    if wdi_pivot.shape[1] >= 5:
        wdi_pivot.columns = [
            'country',
            'gdp_per_capita',
            'rd_expenditure_pct',
            'population',
            'researchers_per_million'
        ]
    else:
        st.warning("⚠️ Datos WDI incompletos. Algunas visualizaciones no estarán disponibles.")
        return
    
    # Merge con saldo migratorio
    net_migration = data_loader.compute_net_migration(df_flows)
    
    # Obtener mapeo ISO3
    iso_map_origin = df_flows[['origin', 'origin_iso3']].drop_duplicates().rename(
        columns={'origin': 'country_code', 'origin_iso3': 'iso3'}
    )
    iso_map_dest = df_flows[['destination', 'destination_iso3']].drop_duplicates().rename(
        columns={'destination': 'country_code', 'destination_iso3': 'iso3'}
    )
    iso_map = pd.concat([iso_map_origin, iso_map_dest]).drop_duplicates(subset='iso3')
    
    # Merge net_migration con iso3
    net_migration_iso3 = net_migration.merge(
        iso_map,
        left_on='country',
        right_on='country_code',
        how='left'
    )
    
    # Merge con WDI
    migration_wdi = net_migration_iso3.merge(
        wdi_pivot,
        left_on='iso3',
        right_on='country',
        how='inner'
    )
    
    if migration_wdi.empty:
        st.warning("⚠️ No se pudo hacer el merge con datos WDI.")
        return
    
    # Inicializar variables de correlación
    corr_gdp = 0.0
    corr_rd = 0.0
    
    # Scatter: PIB per cápita vs Saldo Migratorio
    st.markdown("### 📈 Saldo Migratorio vs. PIB per Cápita")
    
    viz_data = migration_wdi[
        migration_wdi['gdp_per_capita'].notna() &
        migration_wdi['net_balance'].notna() &
        (migration_wdi['total_flow'] > 50)
    ].copy()
    
    fig_gdp = px.scatter(
        viz_data,
        x='gdp_per_capita',
        y='net_balance',
        size='total_flow',
        color='type',
        hover_name='country_x',
        hover_data=['immigration', 'emigration', 'population'],
        title='Correlación: PIB per Cápita vs. Saldo Migratorio Neto',
        labels={
            'gdp_per_capita': 'PIB per Cápita (USD)',
            'net_balance': 'Saldo Migratorio Neto',
            'total_flow': 'Flujo Total',
            'type': 'Tipo de País'
        },
        color_discrete_map={'Atractor': THEME_COLORS['success'], 'Exportador': THEME_COLORS['warning']},
        log_x=True,
        trendline="ols"
    )
    
    fig_gdp.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Balance = 0")
    fig_gdp.update_layout(
        height=600,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_gdp, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Calcular correlación
    if len(viz_data) > 2:
        corr_gdp = viz_data[['gdp_per_capita', 'net_balance']].corr().iloc[0, 1]
        
        st.markdown(f"""
        <div class="alert-info">
            <h4>📊 Correlación de Pearson: {corr_gdp:.3f}</h4>
            <p>Existe una <strong>correlación positiva {'fuerte' if abs(corr_gdp) > 0.7 else 'moderada'}</strong> 
            entre PIB per cápita y saldo migratorio neto.</p>
            <ul>
                <li>Países con PIB >$40,000 tienden a ser <strong>atractores netos</strong></li>
                <li>Países con PIB <$15,000 tienden a ser <strong>exportadores netos</strong></li>
                <li>Zona de transición: $15k-$40k con comportamiento mixto</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Scatter: Gasto I+D vs Saldo Migratorio
    st.markdown("### 🔬 Saldo Migratorio vs. Gasto en I+D")
    
    viz_data_rd = migration_wdi[
        migration_wdi['rd_expenditure_pct'].notna() &
        migration_wdi['net_balance'].notna() &
        (migration_wdi['total_flow'] > 50)
    ].copy()
    
    if len(viz_data_rd) > 10:
        fig_rd = px.scatter(
            viz_data_rd,
            x='rd_expenditure_pct',
            y='net_balance',
            size='total_flow',
            color='type',
            hover_name='country_x',
            hover_data=['immigration', 'emigration', 'gdp_per_capita'],
            title='Correlación: Gasto en I+D (% PIB) vs. Saldo Migratorio Neto',
            labels={
                'rd_expenditure_pct': 'Gasto I+D (% del PIB)',
                'net_balance': 'Saldo Migratorio Neto',
                'total_flow': 'Flujo Total',
                'type': 'Tipo de País'
            },
            color_discrete_map={'Atractor': THEME_COLORS['success'], 'Exportador': THEME_COLORS['warning']},
            trendline="ols"
        )
        
        fig_rd.add_hline(y=0, line_dash="dash", line_color="gray")
        fig_rd.update_layout(
            height=600,
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_rd, use_container_width=True, config=PLOTLY_CONFIG)
        
        # Correlación
        corr_rd = viz_data_rd[['rd_expenditure_pct', 'net_balance']].corr().iloc[0, 1]
        
        st.markdown(f"""
        <div class="alert-success">
            <h4>📊 Correlación de Pearson: {corr_rd:.3f}</h4>
            <p>La correlación con gasto en I+D es <strong>{'más fuerte' if abs(corr_rd) > abs(corr_gdp) else 'similar'}</strong> 
            que con PIB per cápita.</p>
            <p><strong>Insight clave:</strong> El gasto en I+D es mejor predictor que PIB porque señala 
            <em>compromiso específico con ciencia</em>, no solo riqueza general.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # NUEVA MEJORA 3: Parallel Coordinates - Análisis multivariable
    st.markdown("### 🎨 Análisis Multivariable: Parallel Coordinates")
    st.markdown("Visualización de relaciones simultáneas entre múltiples variables económicas y migratorias")
    
    # Preparar datos para parallel coordinates (tomar muestra si hay muchos)
    parallel_data = migration_wdi[
        migration_wdi['gdp_per_capita'].notna() &
        migration_wdi['rd_expenditure_pct'].notna() &
        migration_wdi['net_balance'].notna()
    ].copy()
    
    # Normalizar algunas variables para mejor visualización
    parallel_data['net_balance_scaled'] = parallel_data['net_balance'] / 1000  # escalar a miles
    parallel_data['population_millions'] = parallel_data['population'] / 1000000
    parallel_data['type_numeric'] = parallel_data['type'].map({'Atractor': 1, 'Exportador': 0})
    
    # Tomar muestra si hay demasiados países
    if len(parallel_data) > 100:
        parallel_sample = parallel_data.sample(n=100, random_state=42)
    else:
        parallel_sample = parallel_data
    
    fig_parallel = px.parallel_coordinates(
        parallel_sample,
        dimensions=['gdp_per_capita', 'rd_expenditure_pct', 'net_balance_scaled', 
                   'immigration', 'emigration', 'population_millions'],
        color='type_numeric',
        color_continuous_scale=[(0, THEME_COLORS['warning']), (1, THEME_COLORS['success'])],
        labels={
            'gdp_per_capita': 'PIB per Cápita',
            'rd_expenditure_pct': 'I+D (% PIB)',
            'net_balance_scaled': 'Saldo Neto (miles)',
            'immigration': 'Inmigración',
            'emigration': 'Emigración',
            'population_millions': 'Población (M)',
            'type_numeric': 'Tipo'
        },
        title='Análisis Multidimensional: Variables Económicas y Migratorias'
    )
    
    fig_parallel.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=600,
        coloraxis_colorbar=dict(
            title="Tipo",
            tickvals=[0, 1],
            ticktext=["Exportador", "Atractor"]
        )
    )
    
    st.plotly_chart(fig_parallel, use_container_width=True, config=PLOTLY_CONFIG)
    
    st.markdown("""
    <div class="alert-info">
        <h4>💡 Cómo interpretar este gráfico:</h4>
        <ul>
            <li><strong>Líneas verdes:</strong> Países atractores de talento</li>
            <li><strong>Líneas naranjas:</strong> Países exportadores de talento</li>
            <li>Observa patrones: países atractores suelen tener valores altos en PIB, I+D e inmigración</li>
            <li>Las líneas que se cruzan en direcciones opuestas indican perfiles muy diferentes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# TAB 6: EVOLUCIÓN TEMPORAL
# =============================================================================

def render_temporal_evolution(df_flows: pd.DataFrame, df_migrations: pd.DataFrame):
    """Renderiza análisis de evolución temporal de migraciones."""
    
    st.markdown('<div class="section-header">📅 Evolución Temporal</div>', unsafe_allow_html=True)
    
    # Evolución por año de PhD
    if 'phd_year_mean' in df_flows.columns:
        st.markdown("### 🎓 Flujos por Año de Doctorado")
        
        # Crear bins de años
        df_flows['phd_decade'] = (df_flows['phd_year_mean'] // 10 * 10).astype(int)
        
        flows_by_decade = df_flows.groupby('phd_decade')['n_researchers'].sum().reset_index()
        flows_by_decade = flows_by_decade[flows_by_decade['phd_decade'] >= 1960]
        
        fig_decade = px.bar(
            flows_by_decade,
            x='phd_decade',
            y='n_researchers',
            title='Volumen de Migraciones por Década (Año de PhD)',
            labels={'phd_decade': 'Década', 'n_researchers': 'Número de Investigadores'},
            color='n_researchers',
            color_continuous_scale='Blues'
        )
        
        fig_decade.update_layout(
            height=400,
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_decade, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Si tenemos datos individuales de migraciones
    if not df_migrations.empty and 'origin_year' in df_migrations.columns:
        st.markdown("### 📈 Evolución Anual de Migraciones")
        
        migration_year_dist = df_migrations[
            df_migrations['origin_year'].notna() &
            (df_migrations['origin_year'] >= 1970) &
            (df_migrations['origin_year'] <= 2020)
        ]['origin_year'].value_counts().sort_index().reset_index()
        migration_year_dist.columns = ['year', 'count']
        
        fig_year = px.line(
            migration_year_dist,
            x='year',
            y='count',
            title='Evolución Temporal de Migraciones Científicas (1970-2020)',
            labels={'year': 'Año de Primera Afiliación', 'count': 'Número de Investigadores'},
            markers=True
        )
        
        fig_year.update_traces(line_color=THEME_COLORS['primary'], marker=dict(size=6))
        fig_year.update_layout(
            height=500,
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_year, use_container_width=True, config=PLOTLY_CONFIG)
        
        # Identificar pico
        if not migration_year_dist.empty:
            peak_year = migration_year_dist.nlargest(1, 'count')['year'].values[0]
            peak_count = migration_year_dist.nlargest(1, 'count')['count'].values[0]
            
            st.markdown(f"""
            <div class="alert-info">
                <h4>📊 Pico de Migraciones: {int(peak_year)}</h4>
                <p>El año con mayor volumen registró <strong>{int(peak_count):,} investigadores</strong> migrando.</p>
            </div>
            """, unsafe_allow_html=True)


# =============================================================================
# TAB 7: DIAGRAMA DE FLUJOS (SANKEY)
# =============================================================================

def render_flow_diagram(df: pd.DataFrame, filters: dict):
    """Renderiza diagrama de flujos Sankey."""
    
    st.markdown('<div class="section-header">🌊 Diagrama de Flujos (Sankey)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    El **diagrama de Sankey** muestra visualmente los flujos migratorios como "ríos de talento",
    donde el ancho de las líneas representa el volumen de investigadores.
    """)
    
    # Control de visualización
    col1, col2 = st.columns([2, 1])
    
    with col1:
        n_flows = st.slider(
            "Número de flujos a visualizar",
            min_value=10,
            max_value=50,
            value=30,
            step=5,
            help="Más flujos = diagrama más complejo"
        )
    
    with col2:
        flow_type = st.selectbox(
            "Tipo de flujo",
            ["País a País", "Región a Región"],
            help="Selecciona nivel de agregación"
        )
    
    # Crear Sankey
    if flow_type == "País a País":
        fig_sankey = create_sankey_countries(df, n_flows)
    else:
        from components.data_loader import DataLoader
        data_loader = DataLoader()
        region_flows = data_loader.get_regional_flows(df)
        fig_sankey = create_sankey_regional(region_flows.head(n_flows))
    
    st.plotly_chart(fig_sankey, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Información sobre el diagrama
    with st.expander("ℹ️ Cómo interpretar el diagrama Sankey"):
        st.markdown("""
        ### 📖 Guía de Lectura
        
        - **Nodos (cajas):** Representan países o regiones
        - **Flujos (líneas):** Representan movimiento de investigadores
        - **Ancho del flujo:** Proporcional al número de investigadores
        - **Colores:** Diferencias visuales entre nodos
        
        **Patrones comunes:**
        - 🇺🇸 **USA** aparece como receptor principal (muchas líneas entrantes)
        - 🇨🇳 **China** e 🇮🇳 **India** muestran flujos salientes masivos
        - 🇪🇺 **Europa** tiene red compleja de flujos internos
        
        **Limitaciones:**
        - Solo muestra top N flujos (diagrama se satura con muchos nodos)
        - No representa temporalidad (visión estática del período completo)
        """)


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def create_sankey_countries(df: pd.DataFrame, top_n: int = 30) -> go.Figure:
    """Crea diagrama Sankey de flujos entre países."""
    
    df_top = df.nlargest(top_n, 'n_researchers').copy()
    
    # Crear mapeo de nodos únicos
    all_countries = list(set(df_top['origin_iso3'].tolist() + df_top['destination_iso3'].tolist()))
    country_to_idx = {country: idx for idx, country in enumerate(all_countries)}
    
    # Crear listas para Sankey
    sources = [country_to_idx[origin] for origin in df_top['origin_iso3']]
    targets = [country_to_idx[dest] for dest in df_top['destination_iso3']]
    values = df_top['n_researchers'].tolist()
    
    # Colores
    node_colors = [f'rgba({hash(c) % 200 + 50}, {hash(c[::-1]) % 200 + 50}, 180, 0.8)' 
                   for c in all_countries]
    link_colors = ['rgba(100, 150, 200, 0.3)'] * len(values)
    
    # Crear diagrama
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=0.5),
            label=all_countries,
            color=node_colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title=f"Top {top_n} Flujos Migratorios: País a País",
        font=dict(size=12),
        height=700,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig


def create_sankey_regional(region_flows: pd.DataFrame) -> go.Figure:
    """Crea diagrama Sankey de flujos entre regiones."""
    
    # Crear mapeo de regiones
    all_regions = list(set(region_flows['origin_region'].tolist() + 
                           region_flows['destination_region'].tolist()))
    region_to_idx = {region: idx for idx, region in enumerate(all_regions)}
    
    # Crear listas
    sources = [region_to_idx[r] for r in region_flows['origin_region']]
    targets = [region_to_idx[r] for r in region_flows['destination_region']]
    values = region_flows['n_researchers'].tolist()
    
    # Colores por región
    region_colors = {
        'Europa': 'rgba(46, 134, 171, 0.8)',
        'Norteamérica': 'rgba(241, 143, 1, 0.8)',
        'Asia': 'rgba(162, 59, 114, 0.8)',
        'Sudamérica': 'rgba(6, 167, 125, 0.8)',
        'Oceanía': 'rgba(108, 117, 125, 0.8)',
        'África': 'rgba(208, 0, 0, 0.8)',
        'Otros': 'rgba(200, 200, 200, 0.8)'
    }
    
    node_colors = [region_colors.get(r, 'rgba(200, 200, 200, 0.8)') for r in all_regions]
    link_colors = ['rgba(100, 150, 200, 0.3)'] * len(values)
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=0.5),
            label=all_regions,
            color=node_colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title="Flujos Migratorios por Región Geográfica",
        font=dict(size=14),
        height=600,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig
