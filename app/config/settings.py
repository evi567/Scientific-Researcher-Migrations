"""
Configuración Global de la Aplicación
======================================

Define constantes, configuraciones de página y tema visual.
"""

from pathlib import Path

# =============================================================================
# RUTAS DEL PROYECTO
# =============================================================================

BASE_DIR = Path(__file__).parent.parent  # Carpeta 'app'
PROJECT_ROOT = BASE_DIR.parent  # Carpeta raíz del proyecto
DATA_DIR = PROJECT_ROOT / 'outputs' / 'processed'
DOCS_DIR = PROJECT_ROOT / 'docs'
IMG_DIR = PROJECT_ROOT / 'img'

# =============================================================================
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# =============================================================================

PAGE_CONFIG = {
    'page_title': '🌍 Migración Científica Global',
    'page_icon': '🔬',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
    'menu_items': {
        'Get Help': 'https://github.com',
        'Report a bug': 'https://github.com',
        'About': '''
        # Panel de Inteligencia: Migración Científica Global
        
        Análisis exhaustivo de patrones de migración de investigadores 
        científicos a nivel mundial (2000-2016).
        
        **Fuentes de datos:**
        - ORCID (identificadores de investigadores)
        - World Development Indicators (Banco Mundial)
        
        **Versión:** 1.0.0
        '''
    }
}

# =============================================================================
# TEMA DE COLORES (Sincronizado con notebooks)
# =============================================================================

THEME_COLORS = {
    'primary': '#2E86AB',      # Azul principal
    'secondary': '#A23B72',    # Magenta secundario
    'accent': '#F18F01',       # Naranja acento
    'success': '#06A77D',      # Verde éxito
    'warning': '#D00000',      # Rojo advertencia
    'neutral': '#6C757D',      # Gris neutral
    'background': '#0E1117',   # Fondo oscuro
    'card_bg': '#1E2128'       # Fondo de tarjetas
}

# =============================================================================
# CONFIGURACIÓN DE VISUALIZACIONES
# =============================================================================

PLOTLY_CONFIG = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['lasso2d', 'select2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'scientific_migration_chart',
        'height': 800,
        'width': 1200,
        'scale': 2
    }
}

PLOTLY_TEMPLATE = 'plotly_dark'

# =============================================================================
# MAPEOS GEOGRÁFICOS
# =============================================================================

REGION_MAP = {
    # Europa
    'GBR': 'Europa', 'DEU': 'Europa', 'FRA': 'Europa', 'ITA': 'Europa', 
    'ESP': 'Europa', 'NLD': 'Europa', 'BEL': 'Europa', 'CHE': 'Europa', 
    'AUT': 'Europa', 'SWE': 'Europa', 'NOR': 'Europa', 'DNK': 'Europa', 
    'FIN': 'Europa', 'POL': 'Europa', 'CZE': 'Europa', 'HUN': 'Europa', 
    'ROU': 'Europa', 'BGR': 'Europa', 'GRC': 'Europa', 'PRT': 'Europa',
    'IRL': 'Europa', 'HRV': 'Europa', 'SVK': 'Europa', 'SVN': 'Europa', 
    'LUX': 'Europa', 'EST': 'Europa', 'LVA': 'Europa', 'LTU': 'Europa',
    
    # Norteamérica
    'USA': 'Norteamérica', 'CAN': 'Norteamérica', 'MEX': 'Norteamérica',
    
    # Asia
    'CHN': 'Asia', 'JPN': 'Asia', 'IND': 'Asia', 'KOR': 'Asia', 
    'IDN': 'Asia', 'THA': 'Asia', 'MYS': 'Asia', 'SGP': 'Asia', 
    'PHL': 'Asia', 'VNM': 'Asia', 'PAK': 'Asia', 'BGD': 'Asia', 
    'IRN': 'Asia', 'TUR': 'Asia', 'SAU': 'Asia', 'ARE': 'Asia', 
    'ISR': 'Asia',
    
    # Sudamérica
    'BRA': 'Sudamérica', 'ARG': 'Sudamérica', 'CHL': 'Sudamérica', 
    'COL': 'Sudamérica', 'PER': 'Sudamérica', 'VEN': 'Sudamérica', 
    'ECU': 'Sudamérica', 'BOL': 'Sudamérica', 'PRY': 'Sudamérica', 
    'URY': 'Sudamérica',
    
    # Oceanía
    'AUS': 'Oceanía', 'NZL': 'Oceanía',
    
    # África
    'ZAF': 'África', 'EGY': 'África', 'NGA': 'África', 'KEN': 'África', 
    'MAR': 'África', 'TUN': 'África', 'GHA': 'África', 'ETH': 'África', 
    'UGA': 'África'
}

# =============================================================================
# CONSTANTES DE ANÁLISIS
# =============================================================================

# Umbrales para clasificación de países
GDP_THRESHOLD_HIGH = 40000  # USD per cápita
GDP_THRESHOLD_LOW = 15000   # USD per cápita

RD_THRESHOLD_HIGH = 3.0     # % del PIB en I+D
RD_THRESHOLD_MEDIUM = 1.5   # % del PIB en I+D

# Rangos de años
YEAR_MIN = 1950
YEAR_MAX = 2020

# Top N para visualizaciones
TOP_N_DEFAULT = 15
TOP_N_CORRIDORS = 20

# =============================================================================
# TEXTOS Y DESCRIPCIONES
# =============================================================================

ABOUT_TEXT = """
### 🌍 Sobre este Panel

Este panel de inteligencia analiza **más de 60,000 flujos migratorios** entre países,
revelando patrones de atracción y expulsión de talento científico.

**Hallazgos clave:**
- 🔴 **Concentración masiva** de talento en países desarrollados
- 🌐 **Autopistas del conocimiento** conectando Asia con Occidente  
- 💡 **Correlación fuerte** entre PIB/I+D y atracción de talento
- 📉 **Brain drain crítico** en países en desarrollo

**Tecnologías utilizadas:**
- 🐍 Python (pandas, numpy, plotly)
- 📊 Streamlit (framework web)
- 🗄️ Datasets: ORCID + World Bank WDI
"""

DATA_INFO_TEXT = """
### 📊 Fuentes de Datos

#### 1. Datos de Migración Científica
- **Fuente:** ORCID + Afiliaciones institucionales
- **Cobertura:** ~741,000 registros de investigadores
- **Período:** 2000-2016
- **Variables:** Origen, destino, año doctorado, afiliaciones

#### 2. World Development Indicators (WDI)
- **Fuente:** Banco Mundial
- **Indicadores:**
  - PIB per cápita (USD)
  - Gasto en I+D (% PIB)
  - Población total
  - Densidad de investigadores (por millón hab.)
- **Período:** 2014-2016

#### 3. Mapeo Geográfico
- Códigos ISO2/ISO3 de países
- Clasificación regional (7 regiones)
"""

LIMITATIONS_TEXT = """
### ⚠️ Limitaciones del Análisis

1. **Temporalidad:** Datos hasta 2016, eventos recientes no reflejados (Brexit, COVID-19)
2. **Definición de migración:** Basada en cambio de afiliación, no residencia permanente
3. **Sesgo de cobertura:** Mayor representación de investigadores digitalizados (ORCID)
4. **Calidad vs Cantidad:** No capturamos impacto científico, solo número de investigadores
5. **Causalidad:** Correlaciones observadas no implican causalidad directa
"""
