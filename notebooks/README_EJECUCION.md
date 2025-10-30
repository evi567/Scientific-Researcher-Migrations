# 📘 Guía de Ejecución del Notebook `prep.ipynb`

## ✅ Opción 1: Ejecutar en VS Code (Recomendado)

**VS Code tiene soporte nativo para Jupyter Notebooks**, no necesitas instalar ni ejecutar Jupyter desde la terminal.

### Pasos:

1. **Abre el archivo** `prep.ipynb` en VS Code (ya lo tienes abierto)

2. **Selecciona un Kernel de Python:**
   - Busca en la esquina superior derecha del notebook un botón que dice **"Select Kernel"**
   - Haz clic y selecciona **Python 3.12.10** (o el que tengas instalado)
   - Si no aparece, selecciona "Python Environments..." y elige el intérprete

3. **Las dependencias ya se están instalando** (el comando `pip install` que lancé ya está en proceso)

4. **Ejecuta el notebook:**
   - **Opción A**: Usa `Shift + Enter` para ejecutar celda por celda
   - **Opción B**: Haz clic en **"Run All"** en la barra superior del notebook
   - **Opción C**: Usa el botón ▶️ que aparece a la izquierda de cada celda

---

## ⚙️ Opción 2: Ejecutar con Jupyter Notebook (navegador)

Si prefieres usar Jupyter en el navegador, las librerías ya se están instalando. Cuando termine:

1. **Abre una terminal en VS Code:**
   - Terminal → New Terminal

2. **Navega a la carpeta de notebooks:**
   ```powershell
   cd "c:\Users\José Luis\Documents\GitHub\Scientific-Researcher-Migrations\notebooks"
   ```

3. **Inicia Jupyter Notebook:**
   ```powershell
   jupyter notebook
   ```

4. Se abrirá tu navegador con la interfaz de Jupyter. Haz clic en `prep.ipynb`

---

## 📦 Dependencias Necesarias

Las siguientes librerías ya se están instalando automáticamente:

- ✅ `jupyter` - Framework de notebooks
- ✅ `pandas` - Manipulación de datos
- ✅ `numpy` - Operaciones numéricas
- ✅ `pycountry` - Mapeo de códigos ISO de países
- ✅ `pyarrow` - Lectura/escritura de archivos Parquet

---

## 🚨 Solución de Problemas

### Error: "jupyter no se reconoce como comando"
- **Solución**: Usa VS Code directamente (Opción 1), no necesitas ejecutar `jupyter` desde terminal

### Error: "No kernel selected"
- **Solución**: Haz clic en "Select Kernel" en la esquina superior derecha y selecciona Python 3.12

### Error: "Module not found"
- **Solución**: Espera a que termine la instalación de dependencias (ya en proceso)
- O ejecuta manualmente:
  ```powershell
  pip install pandas numpy pycountry pyarrow ipykernel
  ```

### El notebook tarda mucho en cargar WDI
- **Normal**: El archivo `Indicators.csv` es muy grande (~2GB)
- El notebook filtrará solo los indicadores necesarios

---

## 📂 Estructura de Salida

El notebook generará estos archivos en `outputs/processed/`:

```
outputs/processed/
├── migrations_clean.csv          # Dataset limpio de migraciones
├── migrations_clean.parquet      # (formato optimizado)
├── migration_flows.csv           # Flujos agregados origen→destino
├── migration_flows.parquet       # (formato optimizado)
├── country_mapping.csv           # Mapeo ISO2→ISO3
├── wdi_indicators.csv            # Indicadores WDI filtrados
└── wdi_indicators.parquet        # (formato optimizado)
```

---

## 🎯 Siguiente Paso

Después de ejecutar `prep.ipynb`, podrás ejecutar:
- `01_eda.ipynb` - Análisis exploratorio de datos
- Visualizaciones y dashboards

---

## 💡 Tip

**Usa siempre VS Code para notebooks** - es más rápido, integrado y no requiere servidor web.
