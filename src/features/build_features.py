# ==========================================
# Ingeniería de Características
# ==========================================
# Aquí creamos las "superpotencias" que le damos a nuestro modelo:
# - Indicadores técnicos clásicos (RSI, MACD, etc.)
# - Características basadas en energía del blockchain
# - Variables lag (valores pasados)
# - Ventanas móviles y estadísticas

import pandas as pd
import numpy as np
from typing import Tuple, List


def calculate_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Calcula los indicadores técnicos chicos pero efectivos
    # RSI, MACD, Bollinger Bands, media móvil simple (SMA), media móvil exponencial (EMA)
    # df: DataFrame con OHLCV (Open, High, Low, Close, Volume)
    # Sale: el DataFrame con todos los indicadores metidos
    pass


def calculate_energy_features(
    df: pd.DataFrame,
    energy_consumption: pd.Series
) -> pd.DataFrame:
    # Crea features que capturan info energética
    # Como: ratio energía vs precio, tendencia energética, densidad de carbono
    # df: DataFrame de precios
    # energy_consumption: la serie con consumo energético
    # Retorna: DataFrame con features energéticas nuevas
    pass


def create_lag_features(
    df: pd.DataFrame,
    lag_days: List[int] = [1, 7, 30]
) -> pd.DataFrame:
    # Agrega valores del pasado como features
    # (precio de ayer, de hace una semana, de hace un mes)
    # df: el DataFrame
    # lag_days: [1, 7, 30] significa lags de 1, 7 y 30 días
    # Devuelve: DataFrame con los lags agregados
    pass


def create_rolling_features(
    df: pd.DataFrame,
    windows: List[int] = [7, 14, 30]
) -> pd.DataFrame:
    # Calcula estadísticas en ventanas móviles
    # (media, desv std, máximos, mínimos)
    # df: el DataFrame
    # windows: tamaños de ventana [7, 14, 30]
    # Sale: DataFrame con features rolling nuevas
    pass


def normalize_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    # Normaliza todo para que el modelo esté cómodo
    # (estandarización con z-score)
    # df: DataFrame con features
    # Devuelve: (DataFrame normalizado, parámetros para después)
    pass


def select_features(
    df: pd.DataFrame,
    target: str,
    n_features: int = 20
) -> List[str]:
    # Selecciona las features más importantes
    # (usa correlación e importancia)
    # df: DataFrame completo
    # target: nombre de lo que queremos predecir
    # n_features: cuántas features queremos (default 20)
    # Retorna: lista con nombres de las features elegidas
    pass
