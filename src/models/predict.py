# ==========================================
# Predicción con Modelos
# ==========================================
# Aquí el modelo ya entrenado hace sus predicciones:
# - Predecir valores futuros
# - Calcular confianza de predicciones
# - Generar señales de trading
# - Análisis de incertidumbre

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional


def predict(
    model: Any,
    X: np.ndarray
) -> np.ndarray:
    # Hace predicciones con el modelo entrenado
    # model: modelo ya listo
    # X: features de entrada
    # Retorna: array con predicciones
    pass


def predict_with_confidence(
    model: Any,
    X: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    # Predice pero también dice qué tan seguro está
    # (con intervalos de confianza)
    # model: modelo entrenado
    # X: features de entrada
    # Sale: (predicciones, confianza)
    pass


def generate_signals(
    predictions: np.ndarray,
    threshold: float = 0.5
) -> np.ndarray:
    # Convierte predicciones en señales de trading
    # -1 = vender, 0 = mantener, 1 = comprar
    # predictions: array con predicciones
    # threshold: umbral para decidir
    # Retorna: array con señales
    pass


def calculate_prediction_uncertainty(
    predictions: np.ndarray,
    confidence: np.ndarray
) -> Dict[str, float]:
    # Calcula cuánta incertidumbre hay en las predicciones
    # predictions: array con predicciones
    # confidence: array con confianza
    # Sale: diccionario con métricas de incertidumbre
    pass
