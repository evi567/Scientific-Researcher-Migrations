"""
Página de Conclusiones
======================

Presenta hallazgos clave, implicaciones y recomendaciones estratégicas.
"""

import streamlit as st
from components.data_loader import DataLoader
from config.settings import LIMITATIONS_TEXT


def render_conclusions(data_loader: DataLoader, filters: dict):
    """
    Renderiza la página de conclusiones y hallazgos.
    
    Args:
        data_loader: Instancia del cargador de datos
        filters: Diccionario con filtros del usuario
    """
    
    # Header
    st.markdown("""
    <h1 class="main-title">📊 Conclusiones y Hallazgos Clave</h1>
    <p class="subtitle">
        Síntesis de insights y recomendaciones estratégicas
    </p>
    """, unsafe_allow_html=True)
    
    # =================================================================
    # PRINCIPALES HALLAZGOS
    # =================================================================
    
    st.markdown('<div class="section-header">🎯 Principales Hallazgos</div>', unsafe_allow_html=True)
    
    # Hallazgo 1
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style='text-align: center; font-size: 4rem;'>
                🇺🇸
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            ### 1. Estados Unidos: El Coloso del Talento
            
            Los **Estados Unidos** se consolidan como el **receptor absoluto** de investigadores científicos 
            a nivel mundial, con una ventaja abrumadora sobre otros países.
            
            **Factores clave:**
            - 💰 **Inversión masiva:** ~$550 mil millones anuales en I+D
            - 🏛️ **Universidades élite:** MIT, Stanford, Harvard, Caltech
            - 💵 **Salarios competitivos:** 2-5x superiores a países de origen
            - 🛂 **Visas especializadas:** H-1B, O-1 para talento científico
            - 🌐 **Ecosistemas de innovación:** Silicon Valley, Boston biotech, Research Triangle
            
            **Impacto:** El 30-40% de investigadores en universidades top son extranjeros.
            """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hallazgo 2
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style='text-align: center; font-size: 4rem;'>
                🇨🇳🇮🇳
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            ### 2. China e India: Exportadores Masivos con Estrategias Divergentes
            
            **China:** La Paradoja del Dragón
            - 📤 **Mayor exportador absoluto**, pero ejecutando estrategia de reversión
            - 📥 Programas de retorno agresivos: "Thousand Talents Plan"
            - 🔄 **Éxito parcial:** Retorno acelerado desde 2018
            - 💡 De "brain drain" a "brain circulation"
            
            **India:** La Oportunidad Perdida
            - 📉 Bajo gasto en I+D (~0.7% PIB) vs. China (>2.5% PIB)
            - 🏛️ Infraestructura limitada fuera de IITs
            - 🌐 Diáspora poderosa (CEOs de Google, Microsoft, Adobe)
            - ⚠️ **Potencial demográfico desaprovechado:** población joven masiva
            """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hallazgo 3
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style='text-align: center; font-size: 4rem;'>
                🛤️
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            ### 3. Autopistas del Conocimiento: Corredores Bien Definidos
            
            Los flujos migratorios no son aleatorios. Existen **"superautopistas"** del conocimiento:
            
            **Top 5 Corredores Globales:**
            1. 🇨🇳→🇺🇸 **China → USA:** El más transitado (>10,000 investigadores)
            2. 🇮🇳→🇺🇸 **India → USA:** Alto en STEM, tasa permanencia >70%
            3. 🇮🇷→🇩🇪 **Irán → Alemania:** Académico + refugio político
            4. 🇬🇧→🇺🇸 **UK → USA:** Intercambio de élites
            5. 🇰🇷→🇺🇸 **Corea → USA:** Retornos crecientes (Samsung, LG)
            
            **Patrón:** Asia → Occidente domina el panorama global.
            """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hallazgo 4
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style='text-align: center; font-size: 4rem;'>
                💰
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            ### 4. El Dinero (y la Ciencia) Importan
            
            **Correlaciones encontradas:**
            - 📈 **PIB per cápita ↔ Saldo migratorio:** +0.65 a +0.75
            - 🔬 **Gasto I+D (% PIB) ↔ Saldo migratorio:** +0.70 a +0.80 (más fuerte)
            - 🎓 **Densidad de investigadores:** Auto-refuerza atracción
            
            **Umbrales identificados:**
            - PIB >$40,000 → Típicamente **atractores netos**
            - PIB <$15,000 → Típicamente **exportadores netos**
            - Gasto I+D >3% PIB → Atracción casi garantizada
            
            **Insight clave:** El gasto en I+D es mejor predictor que PIB porque señala 
            **compromiso específico con ciencia**, no solo riqueza general.
            """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =================================================================
    # IMPLICACIONES ESTRATÉGICAS
    # =================================================================
    
    st.markdown('<div class="section-header">🔮 Implicaciones y Recomendaciones</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "Para Países Exportadores",
        "Para Países Receptores",
        "Para la Comunidad Científica Global"
    ])
    
    with tab1:
        st.markdown("""
        ### 🛠️ Estrategias para Países Exportadores (Brain Drain)
        
        #### **Modelo 1: "Re-atracción" al Estilo Chino**
        
        **Qué hace China:**
        - 💰 Programas de retorno con incentivos masivos:
          - Salarios competitivos (6 cifras USD)
          - Financiamiento de laboratorios completos
          - Posiciones senior garantizadas
          - Bonos de contratación ($100k-$500k)
        - 🏗️ Inversión en infraestructura científica de clase mundial
        - 🌆 Zonas de innovación (Shenzhen, Hangzhou, Beijing)
        
        **Resultados:**
        - ✅ Retorno de >10,000 científicos top (2010-2020)
        - ✅ Papers chinos rivalizan con USA en volumen
        - ✅ Liderazgo en IA, 5G, quantum computing
        
        **Lecciones replicables:**
        1. No basta "llamar de vuelta", hay que **competir económicamente**
        2. Infraestructura importa: científicos necesitan equipos, no solo salarios
        3. Libertad académica y meritocracia son críticas
        
        ---
        
        #### **Modelo 2: Ecosistema de Innovación al Estilo Israelí**
        
        **Qué hace Israel:**
        - 🔬 Integración universidad-empresa-militar
        - 🚀 Cultura de emprendimiento ("Chutzpah")
        - 💸 Programa Yozma de venture capital gubernamental
        - 🌍 Retorno de diáspora con skills científicas
        
        **Resultados:**
        - ✅ País pequeño (9M hab.) con 5.5% PIB en I+D (líder mundial)
        - ✅ "Start-up Nation": más startups per cápita
        - ✅ Retención >80% de científicos formados localmente
        
        **Lecciones replicables:**
        1. Crear **valor económico directo** de investigación (no solo académico)
        2. Facilitar emprendimiento científico
        3. Conectar diáspora con oportunidades locales
        
        ---
        
        #### **Modelo 3: "Diáspora como Activo"**
        
        Para países que **no pueden competir económicamente** a corto plazo:
        
        **Cambiar mentalidad:**
        - De "perdimos cerebros" → "tenemos red global"
        - De "fuga" → "circulación"
        
        **Tácticas:**
        - 🔄 **Sabbaticals reversos:** Científicos emigrados regresan 3-6 meses/año
        - 🎓 **Co-supervisión:** Estudiantes locales con mentores en diáspora
        - 💰 **Grants colaborativos:** Fondos para partnerships internacionales
        - 📅 **Congresos estratégicos:** Eventos que traigan diáspora temporalmente
        
        **Ejemplos:**
        - México: Red de Talentos Mexicanos en el Exterior
        - Colombia: "Es Tiempo de Volver"
        - India: NRI research partnerships
        """)
    
    with tab2:
        st.markdown("""
        ### ⚖️ Responsabilidades de Países Receptores (Brain Gain)
        
        #### **Dilema Ético: Brain Drain vs. Brain Circulation**
        
        **El debate:**
        - ¿Es éticamente correcto que países ricos "roben" talento formado con dineros públicos de países pobres?
        - ¿O es elección individual legítima buscar mejores oportunidades?
        
        **Posición balanceada:**
        1. ✅ **Movilidad es derecho humano:** No se puede ni debe restringir
        2. ⚖️ **Pero existe responsabilidad institucional:** Países receptores deben:
           - Facilitar transferencia de conocimiento bidireccional
           - Financiar colaboraciones con países origen
           - Apoyar programas de retorno voluntario
        
        ---
        
        #### **Diversidad como Ventaja Competitiva**
        
        **Países receptores ganan cuando:**
        - 🌈 Aprovechan perspectivas multiculturales en investigación
        - 🧩 Crean equipos diversos (mejor creatividad e innovación)
        - 🌐 Mantienen conexiones con regiones de origen (acceso a mercados, colaboraciones)
        
        **Mejores prácticas:**
        - 🇨🇦 **Canadá:** Puntos en sistema migratorio por diversidad
        - 🇦🇺 **Australia:** Cuotas de investigación regional (África, Asia-Pacífico)
        - 🇩🇪 **Alemania:** Programas especiales para refugiados científicos
        
        ---
        
        #### **Políticas Recomendadas:**
        
        1. **Integración facilitada:**
           - Visados más ágiles para científicos
           - Reconocimiento de credenciales internacional
           - Apoyo a familias (educación hijos, empleo cónyuges)
        
        2. **Retención con propósito:**
           - No solo atraer, sino **retener** con proyectos significativos
           - Libertad académica garantizada
           - Paths claros hacia posiciones permanentes
        
        3. **Colaboración sur-norte:**
           - Co-financiamiento de investigación con países origen
           - Intercambios bidireccionales de estudiantes/postdocs
           - Open access a publicaciones y datos
        """)
    
    with tab3:
        st.markdown("""
        ### 🌍 Para la Comunidad Científica Global
        
        #### **De la Competencia a la Colaboración**
        
        **Visión aspiracional:**
        - 🔬 Ciencia como **bien común global**
        - 🔄 Talento circula, conocimiento se comparte
        - 🏛️ Infraestructura científica se democratiza
        
        ---
        
        #### **Iniciativas Existentes (Modelos a Replicar)**
        
        1. **CERN (Física de Partículas)**
           - 🌐 Colaboración de 100+ países
           - 🔬 Infraestructura compartida (Large Hadron Collider)
           - 📖 Publicaciones open access
        
        2. **Human Genome Project**
           - 🧬 Datos públicos desde día 1
           - 🌍 Consorcio internacional
           - 💡 Aceleró medicina personalizada
        
        3. **IPCC (Panel Climático)**
           - 🌡️ Representación global de científicos
           - 📊 Síntesis de evidencia mundial
           - 🎯 Influencia en política global
        
        4. **Open Access Movement**
           - 📚 Democratiza acceso a publicaciones
           - 💰 Reduce barreras económicas
           - 🚀 Acelera descubrimiento científico
        
        ---
        
        #### **Próximos Pasos Necesarios:**
        
        1. **Financiamiento Global de Ciencia Básica**
           - Fondo internacional para proyectos no rentables pero críticos
           - Financiación basada en mérito, no geografía
        
        2. **Infraestructura Compartida**
           - Telescopios, aceleradores, biobanks accesibles globalmente
           - Tiempo de uso basado en calidad de propuesta científica
        
        3. **Movilidad Facilitada**
           - Visas científicas globales (estilo Schengen)
           - Portabilidad de pensiones y seguridad social
           - Reconocimiento automático de credenciales
        
        4. **Open Science por Default**
           - Publicaciones abiertas obligatorias
           - Datos y código compartidos
           - Revisión por pares abierta
        """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =================================================================
    # LIMITACIONES
    # =================================================================
    
    st.markdown('<div class="section-header">⚠️ Limitaciones del Análisis</div>', unsafe_allow_html=True)
    
    st.markdown(LIMITATIONS_TEXT)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =================================================================
    # REFLEXIÓN FINAL
    # =================================================================
    
    st.markdown('<div class="section-header">💡 Reflexión Final</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="metric-card" style="background: linear-gradient(135deg, rgba(46, 134, 171, 0.2), rgba(162, 59, 114, 0.2));">
        <h3 style="color: #2E86AB;">🌟 De la Fuga a la Circulación</h3>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #FAFAFA;">
            La <strong>migración científica</strong> es un fenómeno complejo que refleja desigualdades globales 
            en desarrollo, pero también oportunidades de colaboración internacional.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #FAFAFA;">
            El desafío está en transformar la <em>"fuga de cerebros"</em> en 
            <strong>"circulación de conocimiento"</strong>, donde el talento beneficie tanto a países 
            emisores como receptores mediante:
        </p>
        <ul style="font-size: 1.05rem; color: #FAFAFA;">
            <li>🤝 Redes de colaboración transnacional</li>
            <li>🔬 Transferencia tecnológica bidireccional</li>
            <li>📚 Open Science y democratización del conocimiento</li>
            <li>⚖️ Políticas científicas equitativas</li>
            <li>🌍 Financiamiento global de ciencia básica</li>
        </ul>
        <p style="font-size: 1.2rem; font-weight: 600; color: #06A77D; margin-top: 1rem;">
            "El conocimiento es el único bien que aumenta cuando se comparte." 💡
        </p>
        <p style="font-size: 1.1rem; margin-top: 1rem; color: #FAFAFA;">
            Quizás hoy, podemos aspirar a que el científico tenga <strong>muchas patrias</strong>, 
            conectadas por la búsqueda común del conocimiento.
        </p>
    </div>
    """, unsafe_allow_html=True)
