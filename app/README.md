# 🌍 Panel de Inteligencia: Migración Científica Global

Aplicación interactiva desarrollada con **Streamlit** para visualizar y analizar patrones de migración de investigadores científicos a nivel mundial (2000-2016).

---

## 📊 Características

### 🏠 **Página de Inicio**
- Resumen ejecutivo con métricas clave
- Mapa mundial interactivo de saldos migratorios
- Rankings de top atractores y exportadores
- Principales hallazgos destacados

### 📈 **Análisis Exploratorio (EDA)**
Análisis exhaustivo organizado en 7 secciones:
1. **Resumen Estadístico:** Distribuciones, percentiles, medidas de tendencia
2. **Emisores y Receptores:** Países con mayor brain drain/gain
3. **Corredores Migratorios:** Rutas bilaterales más transitadas
4. **Análisis Regional:** Flujos entre regiones geográficas
5. **Correlación Económica:** Relación con PIB e I+D
6. **Evolución Temporal:** Tendencias históricas de migraciones
7. **Diagrama de Flujos:** Visualizaciones Sankey interactivas

### 📚 **Conclusiones**
- Hallazgos clave con interpretación contextual
- Implicaciones estratégicas para diferentes stakeholders
- Recomendaciones de política pública
- Limitaciones del análisis

### 🤖 **Machine Learning**
- Sección en desarrollo para análisis predictivo
- Roadmap de características futuras
- Demos interactivas (en construcción)

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.12 o superior
- pip instalado

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Scientific-Researcher-Migrations.git
cd Scientific-Researcher-Migrations
```

### Paso 2: Instalar dependencias
```bash
cd app
pip install -r requirements.txt
```

### Paso 3: Verificar estructura de datos
Asegúrate de tener los archivos procesados en:
```
outputs/processed/
├── migration_flows.csv (o .parquet)
├── migrations_clean.csv (opcional)
├── wdi_indicators.csv (opcional)
└── country_mapping.csv (opcional)
```

### Paso 4: Ejecutar la aplicación
```bash
streamlit run main.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📁 Estructura del Proyecto

```
app/
├── main.py                    # Punto de entrada principal
├── requirements.txt           # Dependencias Python
├── README.md                  # Esta documentación
│
├── config/                    # Configuración global
│   ├── __init__.py
│   └── settings.py           # Constantes, tema, rutas
│
└── components/                # Componentes modulares
    ├── __init__.py
    ├── data_loader.py        # Carga de datos con caché
    ├── sidebar.py            # Navegación y filtros
    ├── home.py               # Página de inicio
    ├── eda.py                # Análisis exploratorio
    ├── conclusions.py        # Conclusiones y hallazgos
    └── ml.py                 # Machine learning (en desarrollo)
```

---

## 🎨 Diseño y UX/UI

### Paleta de Colores
```python
PRIMARY = '#2E86AB'      # Azul principal
SECONDARY = '#A23B72'    # Magenta
ACCENT = '#F18F01'       # Naranja
SUCCESS = '#06A77D'      # Verde
WARNING = '#D00000'      # Rojo
```

### Características UX
- ✅ **Tema oscuro** optimizado para visualización de datos
- ✅ **Responsive design** adaptable a diferentes tamaños de pantalla
- ✅ **Navegación intuitiva** con sidebar persistente
- ✅ **Filtros interactivos** que afectan todas las visualizaciones
- ✅ **Tooltips informativos** en cada métrica y gráfico
- ✅ **Gráficos interactivos** con Plotly (zoom, pan, hover)

---

## 🔧 Configuración Avanzada

### Modificar Rutas de Datos
Edita `config/settings.py`:
```python
DATA_DIR = BASE_DIR / 'tu_carpeta_personalizada'
```

### Personalizar Tema Visual
Modifica `THEME_COLORS` en `config/settings.py`:
```python
THEME_COLORS = {
    'primary': '#TU_COLOR',
    # ...
}
```

### Ajustar Configuración de Página
Edita `PAGE_CONFIG` en `config/settings.py`:
```python
PAGE_CONFIG = {
    'page_title': 'Tu Título',
    'layout': 'wide',  # o 'centered'
    # ...
}
```

---

## 📊 Fuentes de Datos

### 1. Datos de Migración Científica
- **Fuente:** ORCID + Afiliaciones institucionales
- **Cobertura:** ~741,000 registros de investigadores
- **Período:** 2000-2016
- **Variables:** Origen, destino, año doctorado, afiliaciones

### 2. World Development Indicators (WDI)
- **Fuente:** Banco Mundial
- **Indicadores:** PIB per cápita, Gasto I+D, Población, Densidad de investigadores
- **Período:** 2014-2016

### 3. Mapeo Geográfico
- Códigos ISO2/ISO3 de países
- Clasificación en 7 regiones geográficas

---

## 🛠️ Desarrollo y Contribución

### Añadir Nuevas Visualizaciones

1. **Crear función de renderizado** en componente correspondiente:
```python
def render_nueva_visualizacion(df: pd.DataFrame):
    fig = px.bar(df, x='col1', y='col2', title='Mi Gráfico')
    st.plotly_chart(fig, use_container_width=True)
```

2. **Llamar desde tab o sección** en el componente principal

### Añadir Nuevos Filtros

1. **Agregar control en `sidebar.py`:**
```python
nuevo_filtro = st.selectbox("Mi Filtro", opciones)
```

2. **Incluir en diccionario de retorno:**
```python
return {'nuevo_filtro': nuevo_filtro, ...}
```

3. **Usar en funciones de renderizado:**
```python
if filters.get('nuevo_filtro'):
    df = df[df['columna'] == filters['nuevo_filtro']]
```

### Añadir Nueva Página

1. **Crear archivo** en `components/`:
```python
# components/mi_pagina.py
def render_mi_pagina(data_loader, filters):
    st.title("Mi Nueva Página")
    # Tu código aquí
```

2. **Importar en `main.py`:**
```python
from components.mi_pagina import render_mi_pagina
```

3. **Añadir opción en sidebar** (`sidebar.py`)

4. **Añadir routing en `main()`** (`main.py`)

---

## 🐛 Solución de Problemas

### Error: "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Error: "No se encontró migration_flows.csv"
Verifica que los archivos estén en `outputs/processed/`

### Gráficos no se muestran
- Asegúrate de tener instalado Plotly: `pip install plotly`
- Verifica que los datos no estén vacíos

### Aplicación lenta
- Reduce `top_n` en filtros para menos datos
- Verifica que el cache de Streamlit esté funcionando (`@st.cache_data`)

---

## 📚 Recursos Adicionales

### Documentación
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Guide](https://pandas.pydata.org/docs/)

### Datasets
- [ORCID](https://orcid.org/)
- [World Bank Open Data](https://data.worldbank.org/)

---

## 📄 Licencia

Este proyecto utiliza datos públicos de ORCID y World Bank. 

El código está disponible para uso académico y de políticas públicas con atribución apropiada.

---

## 👥 Autor

**Análisis de Movilidad Científica Global**

Desarrollado con ❤️ usando:
- 🐍 Python 3.12
- 📊 Streamlit
- 📈 Plotly
- 🐼 Pandas

---

## 🎯 Roadmap Futuro

### Versión 2.0 (Q1 2026)
- [ ] Análisis por disciplina científica (STEM vs. Humanidades)
- [ ] Dimensión de género en migración
- [ ] Impacto de COVID-19 (datos 2020-2024)
- [ ] Comparador interactivo de países

### Versión 3.0 (Q2 2026)
- [ ] Modelos predictivos con Machine Learning
- [ ] API REST para consultas programáticas
- [ ] Exportación de reportes personalizados (PDF)
- [ ] Sistema de alertas para cambios de tendencia

### Versión 4.0 (Q3-Q4 2026)
- [ ] Integración con bases de datos en tiempo real
- [ ] Dashboard de administración
- [ ] Autenticación y perfiles de usuario
- [ ] Colaboración y anotaciones compartidas

---

**¡Disfruta explorando los datos de migración científica global! 🌍🔬**
