# Crypto ML Energy - Machine Learning para Criptomonedas con Análisis Energético

Proyecto completo de Machine Learning para análisis y predicción de criptomonedas, integrando métricas de consumo energético y consideraciones de eficiencia.

## 🎯 Objetivo

Desarrollar un sistema de análisis predictivo de criptomonedas que considere:
- Análisis técnico tradicional
- Modelos de Machine Learning avanzados
- Métricas de consumo energético de blockchains
- Estrategias de trading automatizado con gestión de riesgo

## 📁 Estructura del Proyecto

```
crypto-ml-energy/
├── data/
│   ├── raw/                 # Datos crudos sin procesar
│   └── processed/           # Datos procesados y listos para modelos
├── notebooks/               # Jupyter notebooks para exploración
├── src/
│   ├── data/               # Carga y procesamiento de datos
│   │   ├── load_data.py
│   │   └── __init__.py
│   ├── features/           # Ingeniería de características
│   │   ├── build_features.py
│   │   └── __init__.py
│   ├── models/             # Entrenamiento y predicción
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── __init__.py
│   ├── strategy/           # Estrategias de trading
│   │   ├── decision.py
│   │   ├── backtest.py
│   │   └── __init__.py
│   ├── energy/             # Análisis energético
│   │   ├── measure.py
│   │   └── __init__.py
│   └── __init__.py
├── results/                # Resultados, reportes y gráficos
├── main.py                 # Punto de entrada
├── requirements.txt        # Dependencias
└── README.md
```

## 🚀 Componentes Principales

### 1. **Carga de Datos** (`src/data/load_data.py`)
- Importación de datos históricos de criptomonedas
- Carga de métricas energéticas de blockchains
- Validación y limpieza de datos
- Fusión de datasets

### 2. **Ingeniería de Características** (`src/features/build_features.py`)
- Indicadores técnicos (RSI, MACD, Bollinger Bands, etc.)
- Características basadas en energía
- Variables lag y rolling windows
- Normalización de datos

### 3. **Modelado** (`src/models/`)
- Entrenamiento con XGBoost, LightGBM y redes neuronales
- Validación cruzada y ajuste de hiperparámetros
- Predicciones con intervalos de confianza
- Generación de señales de trading

### 4. **Estrategia de Trading** (`src/strategy/`)
- Motor de decisiones inteligente
- Backtesting de estrategias
- Gestión de riesgo y posiciones
- Cálculo de métricas de rendimiento

### 5. **Análisis Energético** (`src/energy/measure.py`)
- Consumo energético de blockchains
- Eficiencia energética
- Huella de carbono
- Análisis de tendencias

## 📊 Flujo de Trabajo

1. **Recopilación de datos**: Carga automática de precios y métricas energéticas
2. **Preparación**: Limpieza y normalización de datos
3. **Características**: Generación de indicadores técnicos y energéticos
4. **Entrenamiento**: Modelos optimizados
5. **Validación**: Backtesting con datos históricos
6. **Decisiones**: Generación de señales de trading
7. **Reportes**: Análisis de rendimiento y riesgo

## 🔧 Instalación

### Requisitos previos
- Python 3.8+
- pip o conda

### Setup

```bash
# Clonar repositorio
git clone <repository-url>
cd crypto-ml-energy

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 📈 Uso

```bash
# Ejecutar pipeline completo
python main.py

# Ejecutar análisis específico
python -m src.data.load_data
python -m src.features.build_features
```

## 📚 Módulos Disponibles

### `src.data`
- `load_crypto_data()`: Cargar datos de precios
- `load_energy_data()`: Cargar consumo energético
- `merge_datasets()`: Fusionar datasets

### `src.features`
- `calculate_technical_indicators()`: Indicadores técnicos
- `calculate_energy_features()`: Características energéticas
- `create_lag_features()`: Variables retrasadas
- `normalize_features()`: Normalización

### `src.models`
- `train_xgboost_model()`: Entrenar XGBoost
- `train_lightgbm_model()`: Entrenar LightGBM
- `predict_with_confidence()`: Predicciones con confianza
- `generate_signals()`: Generar señales

### `src.strategy`
- `TradingDecisionEngine`: Motor de decisiones
- `BacktestEngine`: Motor de backtesting
- `apply_risk_management()`: Gestión de riesgo

### `src.energy`
- `get_blockchain_energy_consumption()`: Consumo energético
- `estimate_carbon_footprint()`: Huella de carbono
- `calculate_energy_efficiency()`: Eficiencia energética

## 🎓 Características Clave

✅ Análisis técnico avanzado  
✅ Machine Learning multi-modelo  
✅ Integración de métricas energéticas  
✅ Backtesting automático  
✅ Gestión de riesgo  
✅ Reportes detallados  
✅ Código modular y escalable  

## 📝 Próximos Pasos

- [ ] Implementar conexiones a APIs de datos reales
- [ ] Desarrollar dashboard de monitoreo
- [ ] Agregar almacenamiento en bases de datos
- [ ] Crear sistema de alertas
- [ ] Documentación técnica detallada

## 📧 Contacto

Para preguntas o sugerencias, contactar al equipo del proyecto.

## 📄 Licencia

Este proyecto está bajo licencia MIT.

---

**Estado**: Estructura base completada ✓  
**Última actualización**: 2026
