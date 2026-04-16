# ==========================================
# Entrenamiento de Modelos
# ==========================================
# Aquí es donde nuestro modelo aprende del pasado:
# - Preparar datos para entrenar
# - Entrenar XGBoost, LightGBM y redes neuronales
# - Validación cruzada
# - Ajuste de hiperparámetros

import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple, Optional


def prepare_training_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    validation_split: float = 0.1
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # Prepara los datos para entrenar
    # df: DataFrame con features y variable objetivo
    # test_size: cuánto guardamos para pruebas (20%)
    # validation_split: cuánto para validar (10%)
    # Retorna: (X_train, X_val, X_test, y_train, y_val, y_test)
    pass


def train_xgboost_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: Optional[np.ndarray] = None,
    y_val: Optional[np.ndarray] = None,
    params: Optional[Dict[str, Any]] = None
) -> Any:
    # Entrena un modelo XGBoost (rápido y poderoso)
    # X_train: features de entrenamiento
    # y_train: objetivos de entrenamiento
    # X_val, y_val: datos de validación (opcional)
    # params: hiperparámetros personalizados
    # Sale: modelo ya entrenado
    pass


def train_lightgbm_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: Optional[np.ndarray] = None,
    y_val: Optional[np.ndarray] = None,
    params: Optional[Dict[str, Any]] = None
) -> Any:
    # Entrena un modelo LightGBM (ultra rápido)
    # X_train: features de entrenamiento
    # y_train: objetivos de entrenamiento
    # X_val, y_val: datos de validación (opcional)
    # params: hiperparámetros personalizados
    # Retorna: modelo entrenado
    pass


def train_neural_network(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: Optional[np.ndarray] = None,
    y_val: Optional[np.ndarray] = None,
    layers: Optional[list] = None,
    epochs: int = 100
) -> Any:
    # Entrena una red neuronal (lo más sofisticado)
    # X_train: features de entrenamiento
    # y_train: objetivos de entrenamiento
    # X_val, y_val: datos de validación (opcional)
    # layers: arquitectura de la red
    # epochs: número de pasadas completas
    # Sale: modelo neural entrenado
    pass


def evaluate_model(
    model: Any,
    X_test: np.ndarray,
    y_test: np.ndarray
) -> Dict[str, float]:
    # Evalúa qué tan bueno es el modelo
    # Calcula: MAE, RMSE, R², Sharpe Ratio
    # model: modelo a evaluar
    # X_test, y_test: datos de prueba
    # Retorna: diccionario con todas las métricas
    pass


def save_model(model: Any, filepath: str) -> None:
    # Guarda el modelo en un archivo para usar después
    # model: modelo a guardar
    # filepath: donde lo vamos a guardar
    pass


def load_model(filepath: str) -> Any:
    # Carga un modelo guardado previamente
    # filepath: ruta donde está el modelo
    # Retorna: modelo listo para usar
    pass
