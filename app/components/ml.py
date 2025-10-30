"""
Página de Machine Learning
==========================

Módulo para análisis predictivo y modelado avanzado.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from components.data_loader import DataLoader
from config.settings import THEME_COLORS, PLOTLY_CONFIG


def render_ml(data_loader: DataLoader, filters: dict):
    """
    Renderiza la página de Machine Learning.
    
    Args:
        data_loader: Instancia del cargador de datos
        filters: Diccionario con filtros del usuario
    """
    
    # Header
    st.markdown("""
    <h1 class="main-title">🤖 Machine Learning</h1>
    <p class="subtitle">
        Análisis Predictivo y Modelado Avanzado
    </p>
    """, unsafe_allow_html=True)
    
    # Info sobre disponibilidad de datos
    st.info("""
📊 **Estado de Datos para Machine Learning**

Esta sección aplica técnicas de ML sobre los datos de migración científica disponibles.

**✅ Datos disponibles:**
- **Flujos migratorios:** 4,249 rutas bilaterales entre países
- **Variables:** Inmigración, emigración, saldo neto, volumen total
- **Cobertura:** Investigadores con PhD 2000-2016

**⚠️ Limitaciones actuales:**
- Los **indicadores económicos** (PIB, I+D) del World Bank requieren procesamiento adicional para ser integrados en estos análisis.
- Por ahora, los modelos se enfocan en **patrones migratorios puros** sin variables económicas.

**🎯 Análisis disponibles:** Clustering de países por similitud migratoria, análisis de correlaciones entre variables migratorias, y estadísticas descriptivas avanzadas.
    """)
    
    # =================================================================
    # TABS DE ANÁLISIS ML
    # =================================================================
    
    st.markdown('<div class="section-header">🔬 Análisis de Machine Learning</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Correlaciones",
        "🎯 Clustering",
        "� Distribuciones"
    ])
    
    with tab1:
        render_correlation_demo(data_loader)
    
    with tab2:
        render_clustering_demo(data_loader)
    
    with tab3:
        render_prediction_demo(data_loader)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =================================================================
    # FRAMEWORK FUTURO
    # =================================================================
    
    st.markdown('<div class="section-header">🚀 Framework para Desarrollo Futuro</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 Series Temporales Avanzadas
        
        **Modelos a implementar:**
        - **ARIMA/SARIMA**: Capturar tendencias y estacionalidad
        - **Prophet (Facebook)**: Predicciones robustas con eventos especiales
        - **LSTM (Deep Learning)**: Redes neuronales para patrones complejos
        
        **Aplicaciones:**
        - Predicción de flujos 2020-2030
        - Identificación de puntos de inflexión
        - Análisis de impacto de eventos (COVID-19, Brexit, políticas)
        - Escenarios probabilísticos (mejor/peor caso)
        
        ---
        
        ### 🧠 Modelos Ensemble Avanzados
        
        **Random Forest y Gradient Boosting:**
        - **XGBoost/LightGBM**: Predicción de corredores emergentes
        - **Feature importance**: Variables más influyentes
        - **SHAP values**: Explicabilidad de predicciones
        
        **Casos de uso:**
        - Clasificar países en riesgo de brain drain
        - Predecir éxito de políticas de retorno
        - Identificar factores críticos por región
        """)
    
    with col2:
        st.markdown("""
        ### 🔬 Clustering Avanzado
        
        **Técnicas adicionales:**
        - **DBSCAN**: Detección de outliers y clusters de forma arbitraria
        - **Hierarchical Clustering**: Dendrogramas para jerarquías
        - **t-SNE/UMAP**: Visualización de alta dimensionalidad
        - **Gaussian Mixture Models**: Clustering probabilístico
        
        **Análisis:**
        - Segmentación por disciplina científica
        - Evolución temporal de clusters
        - Identificación de países en transición
        
        ---
        
        ### 🎯 Inferencia Causal
        
        **Métodos causales:**
        - **Propensity Score Matching**: Efecto de políticas específicas
        - **Difference-in-Differences**: Impacto de intervenciones
        - **Synthetic Control**: Comparación con países contrafactuales
        - **Instrumental Variables**: Variables instrumentales
        
        **Preguntas a responder:**
        - ¿Incrementar I+D causa atracción de talento?
        - ¿Efecto real del Brexit en flujos UK?
        - ¿ROI de programas de repatriación?
        """)

    
    # =================================================================
    # ROADMAP
    # =================================================================
    
    st.markdown('<div class="section-header">🗺️ Roadmap de Desarrollo</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Fases de Implementación
    
    #### **Fase 1: Fundamentos (Q1 2026)** ✅ Próximo
    - [ ] Ingeniería de características avanzada
    - [ ] Matriz de correlación interactiva
    - [ ] Análisis de componentes principales (PCA)
    - [ ] Clustering K-Means básico
    
    #### **Fase 2: Modelos Predictivos (Q2 2026)**
    - [ ] Series temporales con Prophet
    - [ ] Regresión múltiple con validación cruzada
    - [ ] Escenarios "what-if" interactivos
    - [ ] Dashboard de predicciones
    
    #### **Fase 3: ML Avanzado (Q3 2026)**
    - [ ] Random Forest y XGBoost
    - [ ] Redes neuronales (TensorFlow/PyTorch)
    - [ ] AutoML con TPOT o AutoKeras
    - [ ] Explicabilidad con SHAP
    
    #### **Fase 4: Inferencia Causal (Q4 2026)**
    - [ ] Propensity Score Matching
    - [ ] Difference-in-Differences
    - [ ] Synthetic Control Methods
    - [ ] Reportes de impacto de políticas
    """)
    
    # Feedback
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander("💬 Sugerencias para esta sección"):
        st.markdown("""
        ### ¿Qué análisis ML te gustaría ver?
        
        Déjanos saber qué modelos o análisis serían más útiles:
        - Predicciones específicas
        - Nuevas variables a considerar
        - Tipos de visualizaciones
        - Casos de uso particulares
        
        **Contacto:** [Tu email o GitHub]
        """)


# =============================================================================
# DEMOS INTERACTIVAS
# =============================================================================

def render_correlation_demo(data_loader: DataLoader):
    """Análisis de correlación entre variables migratorias."""
    
    st.markdown("### 📊 Análisis de Correlaciones Migratorias")
    
    st.markdown("""
    Explora las relaciones entre variables migratorias: inmigración, emigración, 
    saldo neto y flujo total de investigadores entre países.
    """)
    
    # Cargar datos
    df_flows = data_loader.load_flows()
    
    if df_flows.empty:
        st.warning("No hay datos disponibles.")
        return
    
    # Usar datos de migración agregados por país
    correlation_data = data_loader.compute_net_migration(df_flows)
    
    # Seleccionar columnas numéricas para correlación
    numeric_cols = correlation_data.select_dtypes(include=[np.number]).columns.tolist()
    
    # Eliminar columnas con demasiados NaN
    valid_cols = [col for col in numeric_cols 
                  if correlation_data[col].notna().sum() > len(correlation_data) * 0.3]
    
    if len(valid_cols) < 2:
        st.warning(f"⚠️ Datos insuficientes para análisis de correlación. Solo {len(valid_cols)} columna(s) numéricas válidas encontradas.")
        st.info(f"Columnas disponibles: {', '.join(correlation_data.columns.tolist()[:10])}")
        
        # Mostrar al menos las estadísticas básicas de migración
        if not correlation_data.empty:
            st.markdown("### 📊 Estadísticas Básicas de Migración")
            basic_cols = ['immigration', 'emigration', 'net_balance', 'total_flow']
            available_basic = [col for col in basic_cols if col in correlation_data.columns]
            
            if available_basic:
                st.dataframe(
                    correlation_data[available_basic].describe(),
                    use_container_width=True
                )
        return
    
    # Calcular matriz de correlación
    corr_matrix = correlation_data[valid_cols].corr()
    
    # Crear heatmap
    fig = px.imshow(
        corr_matrix,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        zmin=-1,
        zmax=1,
        title='Matriz de Correlación de Pearson',
        labels=dict(color="Correlación")
    )
    
    fig.update_layout(
        height=600,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Encontrar correlaciones más fuertes
    st.markdown("### 🔍 Correlaciones Más Fuertes")
    
    # Crear dataframe de correlaciones
    corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            corr_pairs.append({
                'Variable 1': corr_matrix.columns[i],
                'Variable 2': corr_matrix.columns[j],
                'Correlación': corr_matrix.iloc[i, j]
            })
    
    corr_df = pd.DataFrame(corr_pairs)
    corr_df['Abs_Corr'] = corr_df['Correlación'].abs()
    corr_df = corr_df.sort_values('Abs_Corr', ascending=False)
    
    # Mostrar top correlaciones
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔴 Correlaciones Positivas Más Fuertes:**")
        top_positive = corr_df[corr_df['Correlación'] > 0].head(5)
        for _, row in top_positive.iterrows():
            st.markdown(f"- **{row['Variable 1']}** ↔ **{row['Variable 2']}**: {row['Correlación']:.3f}")
    
    with col2:
        st.markdown("**🔵 Correlaciones Negativas Más Fuertes:**")
        top_negative = corr_df[corr_df['Correlación'] < 0].head(5)
        for _, row in top_negative.iterrows():
            st.markdown(f"- **{row['Variable 1']}** ↔ **{row['Variable 2']}**: {row['Correlación']:.3f}")
    
    # Interpretación
    st.markdown("""
    <div class="alert-info">
        <p><strong>💡 Interpretación:</strong></p>
        <ul>
            <li><strong>+1.0:</strong> Correlación positiva perfecta</li>
            <li><strong>+0.7 a +1.0:</strong> Correlación positiva fuerte</li>
            <li><strong>+0.3 a +0.7:</strong> Correlación positiva moderada</li>
            <li><strong>-0.3 a +0.3:</strong> Correlación débil</li>
            <li><strong>-0.7 a -0.3:</strong> Correlación negativa moderada</li>
            <li><strong>-1.0 a -0.7:</strong> Correlación negativa fuerte</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def render_clustering_demo(data_loader: DataLoader):
    """Demo de clustering de países por características migratorias."""
    
    st.markdown("### 🎯 Clustering de Países")
    
    st.markdown("""
    Agrupa países con patrones migratorios similares usando **K-Means** y **PCA** 
    para visualización en 2D.
    """)
    
    # Cargar datos
    df_flows = data_loader.load_flows()
    if df_flows.empty:
        st.warning("No hay datos disponibles para clustering.")
        return
    
    # Calcular características por país
    country_features = data_loader.compute_net_migration(df_flows)
    
    # Preparar features para clustering (solo variables migratorias)
    feature_cols = ['immigration', 'emigration', 'net_balance', 'total_flow']
    
    # Filtrar países con datos completos
    clustering_data = country_features[['country'] + feature_cols].dropna()
    
    if len(clustering_data) < 10:
        st.warning("Datos insuficientes para clustering (mínimo 10 países con datos completos).")
        return
    
    # Número de clusters
    col1, col2 = st.columns([1, 3])
    with col1:
        n_clusters = st.slider("Número de Clusters", min_value=2, max_value=7, value=4)
    
    # Normalizar datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(clustering_data[feature_cols])
    
    # Aplicar K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clustering_data['cluster'] = kmeans.fit_predict(X_scaled)
    
    # PCA para visualización 2D
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    clustering_data['PC1'] = X_pca[:, 0]
    clustering_data['PC2'] = X_pca[:, 1]
    
    # Visualización
    fig = px.scatter(
        clustering_data,
        x='PC1',
        y='PC2',
        color='cluster',
        hover_name='country',
        hover_data=feature_cols,
        title=f'Clustering de Países en {n_clusters} Grupos (K-Means + PCA)',
        labels={
            'PC1': f'Componente Principal 1 ({pca.explained_variance_ratio_[0]:.1%} varianza)',
            'PC2': f'Componente Principal 2 ({pca.explained_variance_ratio_[1]:.1%} varianza)',
            'cluster': 'Cluster'
        },
        color_continuous_scale='Viridis'
    )
    
    fig.update_traces(marker=dict(size=12, line=dict(width=0.5, color='white')))
    fig.update_layout(
        height=600,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Interpretación de clusters
    st.markdown("### 📋 Perfil de cada Cluster")
    
    for cluster_id in range(n_clusters):
        cluster_countries = clustering_data[clustering_data['cluster'] == cluster_id]
        
        with st.expander(f"**Cluster {cluster_id}** ({len(cluster_countries)} países)"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Top 5 países del cluster
                st.markdown("**Países principales:**")
                top_countries = cluster_countries.nlargest(5, 'total_flow')['country'].tolist()
                st.write(", ".join(top_countries))
            
            with col2:
                # Características promedio
                st.markdown("**Promedios:**")
                avg_net = cluster_countries['net_balance'].mean()
                st.metric("Saldo Neto", f"{avg_net:,.0f}", 
                         delta="Atractor" if avg_net > 0 else "Exportador")
            
            # Estadísticas del cluster
            st.markdown("**Características:**")
            stats_df = cluster_countries[feature_cols].describe().loc[['mean', '50%']].T
            stats_df.columns = ['Media', 'Mediana']
            st.dataframe(stats_df.style.format("{:,.0f}"), use_container_width=True)


def render_prediction_demo(data_loader: DataLoader):
    """Análisis estadístico avanzado de patrones migratorios."""
    
    st.markdown("### � Análisis Estadístico Avanzado")
    
    st.markdown("""
    Análisis de distribuciones y patrones estadísticos en los flujos migratorios 
    de investigadores científicos.
    """)
    
    # Cargar datos
    df_flows = data_loader.load_flows()
    
    if df_flows.empty:
        st.warning("No hay datos disponibles.")
        return
    
    # Preparar datos
    net_migration = data_loader.compute_net_migration(df_flows)
    
    # Análisis de distribuciones
    st.markdown("### 📊 Distribución de Saldos Migratorios")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Países Atractores", 
                 len(net_migration[net_migration['net_balance'] > 0]),
                 help="Países con balance neto positivo")
    with col2:
        st.metric("Países Exportadores", 
                 len(net_migration[net_migration['net_balance'] < 0]),
                 help="Países con balance neto negativo")
    with col3:
        st.metric("Total Países", len(net_migration))
    
    # Histograma de saldos
    fig_hist = px.histogram(
        net_migration,
        x='net_balance',
        nbins=50,
        title='Distribución de Saldos Migratorios por País',
        labels={'net_balance': 'Saldo Migratorio Neto', 'count': 'Frecuencia'},
        color_discrete_sequence=[THEME_COLORS['primary']]
    )
    
    fig_hist.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Balance = 0")
    fig_hist.update_layout(
        height=400,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_hist, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Top atractores y exportadores
    st.markdown("### 🏆 Rankings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Top 10 Atractores:**")
        top_attractors = net_migration.nlargest(10, 'net_balance')[['country', 'net_balance', 'immigration']]
        top_attractors.columns = ['País', 'Saldo Neto', 'Inmigración']
        st.dataframe(top_attractors.style.format({'Saldo Neto': '{:,.0f}', 'Inmigración': '{:,.0f}'}), 
                    hide_index=True, use_container_width=True)
    
    with col2:
        st.markdown("**Top 10 Exportadores:**")
        top_exporters = net_migration.nsmallest(10, 'net_balance')[['country', 'net_balance', 'emigration']]
        top_exporters.columns = ['País', 'Saldo Neto', 'Emigración']
        st.dataframe(top_exporters.style.format({'Saldo Neto': '{:,.0f}', 'Emigración': '{:,.0f}'}), 
                    hide_index=True, use_container_width=True)
    
    # Análisis de regresión simple
    st.markdown("### 📈 Regresión: Inmigración vs. Emigración")
    
    st.markdown("""
    Analiza la relación entre inmigración y emigración para identificar patrones 
    (ej: países que atraen mucho también pierden mucho, o viceversa).
    """)
    
    # Scatter plot
    fig_scatter = px.scatter(
        net_migration,
        x='emigration',
        y='immigration',
        size='total_flow',
        hover_name='country',
        title='Relación entre Emigración e Inmigración',
        labels={
            'emigration': 'Emigración (investigadores)',
            'immigration': 'Inmigración (investigadores)',
            'total_flow': 'Flujo Total'
        },
        trendline="ols",
        color='net_balance',
        color_continuous_scale='RdYlGn'
    )
    
    fig_scatter.update_layout(
        height=500,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True, config=PLOTLY_CONFIG)
    
    # Correlación
    corr = net_migration[['immigration', 'emigration']].corr().iloc[0, 1]
    
    st.markdown(f"""
    <div class="alert-info">
        <h4>� Correlación: {corr:.3f}</h4>
        <p>{'Existe una correlación positiva moderada' if corr > 0.5 else 'La correlación es débil'} 
        entre inmigración y emigración. Esto sugiere que países con alta movilidad tienden a 
        tener flujos en ambas direcciones.</p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# RECURSOS ADICIONALES
# =============================================================================

def render_ml_resources():
    """Muestra recursos para aprender ML aplicado a ciencia de datos."""
    
    st.markdown("""
    ### 📚 Recursos para Machine Learning
    
    **Librerías Python:**
    - [scikit-learn](https://scikit-learn.org/): ML clásico
    - [TensorFlow](https://www.tensorflow.org/): Deep Learning
    - [Prophet](https://facebook.github.io/prophet/): Series temporales
    - [XGBoost](https://xgboost.readthedocs.io/): Gradient Boosting
    - [SHAP](https://shap.readthedocs.io/): Explicabilidad de modelos
    
    **Tutoriales:**
    - [Machine Learning Mastery](https://machinelearningmastery.com/)
    - [Kaggle Learn](https://www.kaggle.com/learn)
    - [Fast.ai](https://www.fast.ai/)
    """)
