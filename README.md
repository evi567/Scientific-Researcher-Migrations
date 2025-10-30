# 🌍 Scientific Researcher Migrations

<div align="center">

**Análisis Integral de la Movilidad del Talento Científico Global**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*"El talento no conoce fronteras, pero las oportunidades sí"*

[📊 Ver Demo](#-demo) • [🚀 Inicio Rápido](#-inicio-rápido) • [📖 Documentación](#-estructura-del-proyecto) • [🤝 Contribuir](#-contribución)

</div>

---

## 📖 Resumen Ejecutivo

Este proyecto presenta un **análisis exhaustivo y multidimensional** de los patrones de migración de investigadores científicos a nivel global, revelando las dinámicas que definen el **mapa mundial del talento científico**.

A través del procesamiento y análisis de **más de 740,000 registros** de investigadores y **4,249 corredores migratorios** entre países, este trabajo descubre historias de ambición, oportunidad y desafío que moldean el futuro de la ciencia global.

### 🎯 ¿Qué descubrirás en este proyecto?

- 🧠 **Patrones de "Brain Drain" y "Brain Gain"**: Identificación de países que atraen vs. pierden talento científico
- 🛤️ **Autopistas del Conocimiento**: Los principales corredores migratorios que conectan Asia con Occidente
- 💰 **Correlación Económica**: Relación entre PIB, inversión en I+D y capacidad de atracción de talento
- 📈 **Evolución Temporal**: Tendencias históricas (2000-2016) en la movilidad científica
- 🎨 **Visualizaciones Interactivas**: Mapas globales, diagramas de flujo Sankey, y dashboards dinámicos
- 🤖 **Machine Learning**: Clustering de países por similitud migratoria y análisis predictivo

---

## 🌟 Características Principales

### 📊 Panel de Inteligencia Interactivo

Aplicación web desarrollada con **Streamlit** que permite:

<table>
<tr>
<td width="50%">

#### 🏠 **Vista de Inicio**
- Métricas globales en tiempo real
- Mapa mundial interactivo de saldos migratorios
- Rankings de top atractores y exportadores
- Resumen ejecutivo con hallazgos clave

</td>
<td width="50%">

#### 📈 **Análisis Exploratorio (EDA)**
- 7 secciones de análisis detallado
- Visualizaciones dinámicas con Plotly
- Filtros por años, regiones y volúmenes
- Estadísticas descriptivas avanzadas

</td>
</tr>
<tr>
<td width="50%">

#### 📚 **Conclusiones y Recomendaciones**
- Interpretación contextual de hallazgos
- Implicaciones estratégicas por stakeholder
- Recomendaciones de política pública
- Limitaciones y trabajo futuro

</td>
<td width="50%">

#### 🤖 **Machine Learning**
- Clustering de países por comportamiento migratorio
- Análisis de correlaciones multivariadas
- Framework para modelado predictivo
- Visualizaciones de componentes principales (PCA)

</td>
</tr>
</table>

### 🔬 Pipeline de Análisis de Datos

```
📊 FLUJO DE TRABAJO

1️⃣ PREPROCESAMIENTO (notebooks/prep.ipynb)
   ├─ Limpieza y validación de datos
   ├─ Detección de migraciones (origen ≠ destino)
   ├─ Agregación de flujos bilaterales
   └─ Integración con World Development Indicators (WDI)

2️⃣ ANÁLISIS EXPLORATORIO (notebooks/eda.ipynb)
   ├─ Identificación de emisores/receptores netos
   ├─ Cálculo de saldos migratorios
   ├─ Análisis de corredores principales
   ├─ Correlaciones con indicadores económicos
   └─ Visualizaciones narrativas

3️⃣ APLICACIÓN INTERACTIVA (app/main.py)
   ├─ Dashboard multi-página con Streamlit
   ├─ Filtros dinámicos y controles interactivos
   ├─ Exportación de datos procesados
   └─ Sistema modular y escalable
```

---

## 🗂️ Estructura del Proyecto

```
Scientific-Researcher-Migrations/
│
├── 📁 app/                          # Aplicación Streamlit
│   ├── main.py                      # Punto de entrada principal
│   ├── requirements.txt             # Dependencias Python
│   ├── README.md                    # Documentación de la app
│   │
│   ├── 📁 components/               # Módulos de UI modulares
│   │   ├── __init__.py
│   │   ├── data_loader.py           # Cargador de datos centralizado
│   │   ├── sidebar.py               # Barra lateral con filtros
│   │   ├── home.py                  # Página de inicio
│   │   ├── eda.py                   # Análisis exploratorio
│   │   ├── conclusions.py           # Hallazgos y recomendaciones
│   │   └── ml.py                    # Machine Learning
│   │
│   └── 📁 config/                   # Configuraciones globales
│       ├── __init__.py
│       └── settings.py              # Constantes y temas
│
├── 📁 data/                         # Datos raw
│   ├── Scientific Researcher Migrations.csv    # Dataset principal (~741K registros)
│   │
│   └── 📁 World Development Indicators/        # Indicadores del Banco Mundial
│       ├── Country.csv              # Metadata de países
│       ├── Indicators.csv           # Indicadores económicos (PIB, I+D, etc.)
│       ├── Series.csv               # Descripción de series
│       └── ...
│
├── 📁 outputs/                      # Datos procesados
│   └── 📁 processed/
│       ├── migrations_clean.csv     # Datos limpios de migraciones
│       ├── migration_flows.csv      # Flujos agregados (origen → destino)
│       ├── country_mapping.csv      # Mapeo ISO2 ↔ ISO3
│       └── wdi_indicators.csv       # Indicadores WDI filtrados
│
├── 📁 notebooks/                    # Jupyter Notebooks
│   ├── prep.ipynb                   # 🔧 Preprocesamiento de datos
│   ├── eda.ipynb                    # 📊 Análisis exploratorio
│   └── README_EJECUCION.md          # Guía de ejecución
│
├── 📁 docs/                         # Documentación narrativa
│   ├── eda.md                       # 📖 Análisis narrativo completo (918 líneas)
│   └── info.md                      # Información adicional
│
└── README.md                        # 👈 Estás aquí
```

---

## 🚀 Inicio Rápido

### 📋 Requisitos Previos

- **Python 3.12+** ([Descargar aquí](https://www.python.org/downloads/))
- **pip** (incluido con Python)
- **Git** (opcional, para clonar el repo)

### ⚡ Instalación en 3 Pasos

#### 1️⃣ **Clonar el repositorio**

```powershell
git clone https://github.com/tu-usuario/Scientific-Researcher-Migrations.git
cd Scientific-Researcher-Migrations
```

#### 2️⃣ **Instalar dependencias**

```powershell
pip install -r app/requirements.txt
```

<details>
<summary>📦 <b>Ver lista de dependencias</b></summary>

```
streamlit>=1.28.0          # Framework web
pandas>=2.0.0              # Manipulación de datos
numpy>=1.24.0              # Operaciones numéricas
plotly>=5.17.0             # Visualizaciones interactivas
scikit-learn>=1.3.0        # Machine Learning
statsmodels>=0.14.0        # Análisis estadístico
pyarrow>=14.0.0            # Lectura optimizada de archivos
```

</details>

#### 3️⃣ **Ejecutar la aplicación**

```powershell
streamlit run app/main.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501` 🎉

---

## 📊 Demo

### 🖥️ Capturas de Pantalla

<div align="center">

| Vista de Inicio | Mapa Interactivo |
|:---:|:---:|
| _Métricas globales y rankings de países_ | _Saldos migratorios netos por país_ |

| Análisis de Corredores | Machine Learning |
|:---:|:---:|
| _Principales rutas migratorias bilaterales_ | _Clustering de países por comportamiento_ |

</div>

> 💡 **Tip**: Explora los filtros en la barra lateral para personalizar tu análisis por años, regiones o volumen de migraciones.

---

## 🔍 Fuentes de Datos

### 1. **Migración de Investigadores Científicos**

- **Fuente**: Dataset basado en ORCID y afiliaciones institucionales
- **Cobertura**: ~741,000 registros de investigadores individuales
- **Período**: 2000-2016
- **Variables clave**:
  - País de origen y destino
  - Año de obtención del doctorado
  - Año de primera afiliación en país destino
  - Cambios de afiliación institucional

### 2. **World Development Indicators (Banco Mundial)**

- **Indicadores seleccionados**:
  - PIB per cápita (USD corrientes)
  - Gasto en Investigación y Desarrollo (% del PIB)
  - Población total
  - Densidad de investigadores (por millón de habitantes)
- **Período**: 2014-2016 (alineado con datos de migración)
- **Fuente**: [World Bank Open Data](https://data.worldbank.org/)

### 3. **Mapeo Geográfico**

- Códigos ISO2 e ISO3 de países
- Clasificación regional (Europa, Asia, Norteamérica, etc.)

---

## 📈 Metodología de Análisis

### 🧹 Preprocesamiento de Datos

El notebook `prep.ipynb` realiza las siguientes transformaciones:

1. **Limpieza de datos raw**:
   - Eliminación de registros duplicados
   - Validación de códigos de países (ISO2/ISO3)
   - Tratamiento de valores nulos

2. **Detección de migraciones**:
   ```python
   # Un investigador migró si: país_origen ≠ país_destino
   migrations = df[df['origin'] != df['destination']]
   ```

3. **Agregación de flujos**:
   - Agrupación por par (origen, destino)
   - Cálculo de volúmenes totales de investigadores
   - Creación de matriz de flujos bilaterales

4. **Integración con WDI**:
   - Filtrado de indicadores relevantes (GDP, R&D, Population)
   - Join con datos de migración por código de país
   - Imputación de valores faltantes cuando es posible

### 📊 Análisis Exploratorio

El notebook `eda.ipynb` y la aplicación Streamlit incluyen:

#### **Análisis Univariados**
- Distribuciones de flujos migratorios
- Estadísticas descriptivas (media, mediana, percentiles)
- Identificación de outliers

#### **Análisis Bivariados**
- Correlaciones entre variables económicas y migratorias
- Scatter plots con líneas de tendencia
- Matrices de correlación

#### **Análisis Geoespaciales**
- Mapas coropleth con saldos migratorios netos
- Identificación de "brain drain" vs "brain gain"
- Visualizaciones de corredores principales

#### **Análisis Temporales**
- Evolución de flujos por década
- Identificación de tendencias y cambios de régimen
- Proyecciones a futuro (en desarrollo)

### 🤖 Machine Learning

Técnicas implementadas:

- **Clustering (K-Means)**: Agrupación de países por similitud migratoria
- **PCA**: Reducción de dimensionalidad para visualización
- **Regresión Lineal**: Modelado de relación entre PIB e I+D con atracción de talento
- **Análisis de Correlaciones**: Identificación de variables predictoras

---

## 📚 Hallazgos Clave

### 🥇 Los Grandes Atractores

1. **🇺🇸 Estados Unidos**: El coloso indiscutible del talento científico
   - Saldo neto: **+15,000 a +20,000 investigadores**
   - Principales orígenes: China, India, Irán, Corea del Sur
   - Factor clave: Inversión masiva en I+D (~$550B/año)

2. **🇬🇧 Reino Unido**: El hub europeo
   - Ventaja del idioma inglés
   - Universidades de élite (Oxford, Cambridge, Imperial)
   - ⚠️ Impacto post-Brexit observable

3. **🇩🇪 Alemania**: Gigante industrial-académico
   - Balance entre investigación básica y aplicada
   - Atracción regional desde Europa del Este

### 🔴 Los Grandes Exportadores

1. **🇨🇳 China**: La paradoja del dragón
   - Mayor exportador absoluto histórico
   - Estrategia reciente de reversión exitosa ("Thousand Talents Plan")
   - Transición de "brain drain" a "brain circulation"

2. **🇮🇳 India**: La diáspora poderosa
   - Segundo mayor exportador
   - Fuerte presencia en Silicon Valley y universidades USA
   - Infraestructura científica doméstica limitada

### 🛤️ Corredores Principales

Los 5 corredores más transitados:

1. China → Estados Unidos
2. India → Estados Unidos
3. Alemania → Estados Unidos
4. Reino Unido → Estados Unidos
5. Irán → Estados Unidos

> 💡 **Insight**: Estados Unidos no solo atrae más talento, sino que lo hace de manera **geográficamente diversa**, consolidándose como el hub científico global.

---

## 🛠️ Desarrollo y Arquitectura

### 🏗️ Arquitectura de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│                      STREAMLIT FRONTEND                     │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────┐ │
│  │   Home    │  │    EDA    │  │   ML      │  │ Conclu-  │ │
│  │   Page    │  │   Page    │  │   Page    │  │ sions    │ │
│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └────┬─────┘ │
└────────┼──────────────┼──────────────┼─────────────┼────────┘
         │              │              │             │
         └──────────────┴──────────────┴─────────────┘
                            │
                    ┌───────▼────────┐
                    │  Data Loader   │  (Singleton)
                    │  & Cache Layer │
                    └───────┬────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    ┌────▼─────┐    ┌───────▼────────┐   ┌────▼─────┐
    │ Cleaned  │    │  Migration     │   │   WDI    │
    │Migration │    │    Flows       │   │Indicators│
    │   Data   │    │ (Aggregated)   │   │          │
    └──────────┘    └────────────────┘   └──────────┘
```

### 🎨 Principios de Diseño

- **Modularidad**: Cada componente es independiente y reutilizable
- **Caching inteligente**: Uso de `@st.cache_data` para optimizar carga
- **Responsividad**: Layout adaptativo para diferentes resoluciones
- **UX/UI Cuidado**: Tema personalizado, tooltips informativos, feedback visual

### 🧩 Componentes Principales

| Componente | Responsabilidad |
|------------|-----------------|
| `data_loader.py` | Carga centralizada y caching de datos |
| `sidebar.py` | Filtros globales y controles de usuario |
| `home.py` | Vista de inicio con métricas y mapas |
| `eda.py` | 7 secciones de análisis exploratorio |
| `ml.py` | Clustering, correlaciones y ML |
| `conclusions.py` | Hallazgos y recomendaciones estratégicas |
| `settings.py` | Configuraciones globales (colores, temas, paths) |

---

## 🧪 Ejecutar Notebooks

### Opción 1: VS Code (Recomendado)

1. Abre `notebooks/prep.ipynb` o `notebooks/eda.ipynb` en VS Code
2. Selecciona el kernel de Python 3.12+
3. Ejecuta celda por celda con `Shift + Enter`

### Opción 2: Jupyter Notebook

```powershell
cd notebooks
jupyter notebook
```

### 📦 Dependencias adicionales para notebooks

```powershell
pip install jupyter pandas numpy pycountry pyarrow matplotlib seaborn
```

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! 🎉

### Cómo contribuir:

1. **Fork** el repositorio
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### 💡 Ideas para contribuir:

- 🌐 **Traducciones**: Añadir soporte multiidioma (inglés, francés, etc.)
- 📊 **Nuevas visualizaciones**: Diagramas de Sankey más complejos, mapas 3D
- 🤖 **Modelos ML**: Implementar ARIMA, Prophet, LSTM para predicciones temporales
- 📈 **Datos actualizados**: Integrar datos 2017-2024 cuando estén disponibles
- 🎨 **Mejoras UI/UX**: Modo oscuro, exportación de reportes PDF
- 🧪 **Tests**: Añadir suite de tests unitarios y de integración

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**José Luis**

- 📧 Email: [tu-email@example.com](mailto:tu-email@example.com)
- 💼 LinkedIn: [Tu perfil](https://www.linkedin.com/in/tu-perfil)
- 🐙 GitHub: [@tu-usuario](https://github.com/tu-usuario)

---

## 🙏 Agradecimientos

- **World Bank** por los World Development Indicators
- **ORCID** por los datos de afiliaciones de investigadores
- Comunidad de **Streamlit** por el excelente framework
- Comunidad de **Python científico** (Pandas, NumPy, Plotly, scikit-learn)

---

## 📞 Contacto y Soporte

¿Tienes preguntas o sugerencias?

- 🐛 **Reportar bugs**: [Abrir un Issue](https://github.com/tu-usuario/Scientific-Researcher-Migrations/issues)
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/tu-usuario/Scientific-Researcher-Migrations/discussions)
- 📧 **Email directo**: tu-email@example.com

---

## 📊 Estado del Proyecto

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Maintained](https://img.shields.io/badge/Maintained-Yes-green?style=for-the-badge)

**Última actualización**: Octubre 2025

### 🚧 Roadmap

- [x] Pipeline de preprocesamiento completo
- [x] Análisis exploratorio exhaustivo
- [x] Aplicación Streamlit funcional
- [x] Clustering y análisis ML básico
- [ ] Modelos predictivos avanzados (ARIMA, LSTM)
- [ ] Integración de datos 2017-2024
- [ ] API REST para consultas programáticas
- [ ] Dashboard en tiempo real con actualizaciones automáticas
- [ ] Sistema de alertas para cambios significativos

---

<div align="center">

### ⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub ⭐

**Hecho con ❤️ y ☕ por investigadores apasionados por los datos**

[⬆ Volver arriba](#-scientific-researcher-migrations)

</div>
