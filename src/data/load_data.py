# ==========================================
# Módulo de Carga de Datos
# ==========================================
# Aquí metemos toda la lógica para traer datos de:
# - Precios históricos de criptomonedas
# - Consumo energético de blockchains
# - Limpieza y validación de información

import pandas as pd
from typing import Optional, Dict, List


def load_crypto_data(
    filepath: str,
    crypto_symbol: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> pd.DataFrame:
    # Carga datos históricos de precios de una cripto
    # filepath: donde está el archivo con los datos
    # crypto_symbol: por ej, BTC o ETH
    # start_date y end_date: filtrar por rango de fechas (YYYY-MM-DD)
    # Devuelve: un DataFrame listo para usar
    pass


def load_energy_data(
    filepath: str,
    blockchain: str
) -> pd.DataFrame:
    # Trae datos del consumo energético de un blockchain
    # filepath: ruta del archivo con la info energética
    # blockchain: el nombre (Bitcoin, Ethereum, etc.)
    # Retorna: DataFrame con las métricas de energía
    pass


def validate_data(df: pd.DataFrame) -> bool:
    # Verifica que los datos estén completos y sin errores
    # df: el DataFrame a chequear
    # Devuelve: True si está bien, False si hay problemas
    pass


def merge_datasets(
    crypto_df: pd.DataFrame,
    energy_df: pd.DataFrame
) -> pd.DataFrame:
    # Junta los datos de precios con los de energía
    # crypto_df: DataFrame con precios
    # energy_df: DataFrame con consumo energético
    # Sale: un DataFrame único con toda la info combinada
    pass
