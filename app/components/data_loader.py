"""
Cargador de Datos con Caché
============================

Maneja la carga eficiente de datasets con cache de Streamlit
para optimizar rendimiento de la aplicación.
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Tuple

from config.settings import DATA_DIR, REGION_MAP


class DataLoader:
    """
    Clase para gestionar carga y procesamiento de datos con cache.
    
    Attributes:
        data_dir (Path): Directorio de datos procesados
        _flows_cache (pd.DataFrame): Cache de flujos migratorios
        _migrations_cache (pd.DataFrame): Cache de migraciones individuales
        _wdi_cache (pd.DataFrame): Cache de indicadores WDI
        _mapping_cache (pd.DataFrame): Cache de mapeo de países
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """
        Inicializa el cargador de datos.
        
        Args:
            data_dir: Directorio personalizado de datos (usa default si None)
        """
        self.data_dir = data_dir or DATA_DIR
        self._flows_cache = None
        self._migrations_cache = None
        self._wdi_cache = None
        self._mapping_cache = None
    
    @st.cache_data(ttl=3600)  # Cache por 1 hora
    def load_flows(_self) -> pd.DataFrame:
        """
        Carga dataset de flujos migratorios agregados (origen→destino).
        
        Returns:
            DataFrame con flujos migratorios entre países
        """
        try:
            csv_path = _self.data_dir / 'migration_flows.csv'
            parquet_path = _self.data_dir / 'migration_flows.parquet'
            
            if parquet_path.exists():
                df = pd.read_parquet(parquet_path)
            elif csv_path.exists():
                df = pd.read_csv(csv_path)
            else:
                st.error(f"❌ No se encontró migration_flows en {_self.data_dir}")
                return pd.DataFrame()
            
            # Agregar región de origen y destino
            df['origin_region'] = df['origin_iso3'].map(REGION_MAP).fillna('Otros')
            df['destination_region'] = df['destination_iso3'].map(REGION_MAP).fillna('Otros')
            
            return df
            
        except Exception as e:
            st.error(f"❌ Error cargando flows: {str(e)}")
            return pd.DataFrame()
    
    @st.cache_data(ttl=3600)
    def load_migrations(_self) -> pd.DataFrame:
        """
        Carga dataset de migraciones individuales de investigadores.
        
        Returns:
            DataFrame con registros individuales de investigadores
        """
        try:
            csv_path = _self.data_dir / 'migrations_clean.csv'
            parquet_path = _self.data_dir / 'migrations_clean.parquet'
            
            if parquet_path.exists():
                df = pd.read_parquet(parquet_path)
            elif csv_path.exists():
                df = pd.read_csv(csv_path)
            else:
                st.warning("⚠️ No se encontró migrations_clean (opcional)")
                return pd.DataFrame()
            
            return df
            
        except Exception as e:
            st.warning(f"⚠️ Error cargando migrations: {str(e)}")
            return pd.DataFrame()
    
    @st.cache_data(ttl=3600)
    def load_wdi(_self) -> pd.DataFrame:
        """
        Carga World Development Indicators (Banco Mundial).
        
        Returns:
            DataFrame con indicadores económicos y de desarrollo
        """
        try:
            csv_path = _self.data_dir / 'wdi_indicators.csv'
            parquet_path = _self.data_dir / 'wdi_indicators.parquet'
            
            if parquet_path.exists():
                df = pd.read_parquet(parquet_path)
            elif csv_path.exists():
                df = pd.read_csv(csv_path)
            else:
                st.warning("⚠️ No se encontró wdi_indicators (opcional)")
                return pd.DataFrame()
            
            return df
            
        except Exception as e:
            st.warning(f"⚠️ Error cargando WDI: {str(e)}")
            return pd.DataFrame()
    
    @st.cache_data(ttl=3600)
    def load_mapping(_self) -> pd.DataFrame:
        """
        Carga mapeo de códigos de país (ISO2 ↔ ISO3).
        
        Returns:
            DataFrame con mapeo de códigos de países
        """
        try:
            csv_path = _self.data_dir / 'country_mapping.csv'
            
            if csv_path.exists():
                df = pd.read_csv(csv_path)
                return df
            else:
                st.warning("⚠️ No se encontró country_mapping (opcional)")
                return pd.DataFrame()
            
        except Exception as e:
            st.warning(f"⚠️ Error cargando mapping: {str(e)}")
            return pd.DataFrame()
    
    @st.cache_data(ttl=3600)
    def compute_net_migration(_self, df_flows: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula saldo migratorio neto por país (inmigración - emigración).
        
        Args:
            df_flows: DataFrame de flujos migratorios
            
        Returns:
            DataFrame con saldo migratorio por país
        """
        # Calcular inmigración (destino)
        immigration = df_flows.groupby('destination')['n_researchers'].sum().reset_index()
        immigration.columns = ['country', 'immigration']
        
        # Calcular emigración (origen)
        emigration = df_flows.groupby('origin')['n_researchers'].sum().reset_index()
        emigration.columns = ['country', 'emigration']
        
        # Merge y calcular saldo neto
        net_migration = immigration.merge(emigration, on='country', how='outer').fillna(0)
        net_migration['net_balance'] = net_migration['immigration'] - net_migration['emigration']
        net_migration['total_flow'] = net_migration['immigration'] + net_migration['emigration']
        
        # Ratio inmigración/emigración
        net_migration['migration_ratio'] = np.where(
            net_migration['emigration'] > 0,
            net_migration['immigration'] / net_migration['emigration'],
            np.inf
        )
        
        # Clasificar países
        net_migration['type'] = np.where(
            net_migration['net_balance'] > 0, 
            'Atractor', 
            'Exportador'
        )
        
        # Ordenar por saldo neto descendente
        net_migration = net_migration.sort_values('net_balance', ascending=False).reset_index(drop=True)
        
        return net_migration
    
    @st.cache_data(ttl=3600)
    def get_top_emitters(_self, df_flows: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
        """
        Obtiene los top N países emisores (brain drain).
        
        Args:
            df_flows: DataFrame de flujos migratorios
            top_n: Número de países a retornar
            
        Returns:
            DataFrame con top países emisores
        """
        top_emitters = df_flows.groupby('origin')['n_researchers'].sum().sort_values(ascending=False).reset_index()
        top_emitters.columns = ['country', 'total_emigrants']
        top_emitters['rank'] = range(1, len(top_emitters) + 1)
        
        return top_emitters.head(top_n)
    
    @st.cache_data(ttl=3600)
    def get_top_receivers(_self, df_flows: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
        """
        Obtiene los top N países receptores (brain gain).
        
        Args:
            df_flows: DataFrame de flujos migratorios
            top_n: Número de países a retornar
            
        Returns:
            DataFrame con top países receptores
        """
        top_receivers = df_flows.groupby('destination')['n_researchers'].sum().sort_values(ascending=False).reset_index()
        top_receivers.columns = ['country', 'total_immigrants']
        top_receivers['rank'] = range(1, len(top_receivers) + 1)
        
        return top_receivers.head(top_n)
    
    @st.cache_data(ttl=3600)
    def get_top_corridors(_self, df_flows: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
        """
        Obtiene los top N corredores migratorios bilaterales.
        
        Args:
            df_flows: DataFrame de flujos migratorios
            top_n: Número de corredores a retornar
            
        Returns:
            DataFrame con top corredores
        """
        return df_flows.nlargest(top_n, 'n_researchers')
    
    @st.cache_data(ttl=3600)
    def get_regional_flows(_self, df_flows: pd.DataFrame) -> pd.DataFrame:
        """
        Agrega flujos por región geográfica.
        
        Args:
            df_flows: DataFrame de flujos migratorios
            
        Returns:
            DataFrame con flujos agregados por región
        """
        # Agrupar por región origen y destino
        region_flows = df_flows.groupby(['origin_region', 'destination_region'])['n_researchers'].sum().reset_index()
        
        # Excluir flujos intra-región
        region_flows = region_flows[region_flows['origin_region'] != region_flows['destination_region']]
        
        # Ordenar por magnitud
        region_flows = region_flows.sort_values('n_researchers', ascending=False).reset_index(drop=True)
        
        return region_flows
    
    def get_summary_stats(self, df_flows: pd.DataFrame) -> Dict[str, any]:
        """
        Calcula estadísticas resumen del dataset.
        
        Args:
            df_flows: DataFrame de flujos migratorios
            
        Returns:
            Diccionario con estadísticas clave
        """
        return {
            'total_routes': len(df_flows),
            'total_researchers': int(df_flows['n_researchers'].sum()),
            'unique_origins': df_flows['origin'].nunique(),
            'unique_destinations': df_flows['destination'].nunique(),
            'mean_per_route': df_flows['n_researchers'].mean(),
            'median_per_route': df_flows['n_researchers'].median(),
            'year_range': (
                int(df_flows['phd_year_min'].min()) if 'phd_year_min' in df_flows.columns else None,
                int(df_flows['phd_year_max'].max()) if 'phd_year_max' in df_flows.columns else None
            )
        }
    
    def load_all(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Carga todos los datasets disponibles.
        
        Returns:
            Tupla con (flows, migrations, wdi, mapping)
        """
        return (
            self.load_flows(),
            self.load_migrations(),
            self.load_wdi(),
            self.load_mapping()
        )
