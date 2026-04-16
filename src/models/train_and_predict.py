"""
train_and_predict.py - Entrenar modelo y comparar predicciones vs datos reales
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# 1. Cargar datos
print("📊 CARGANDO DATOS...")
print("="*60)
data = pd.read_csv('data/raw/BTC_USD_2020_2024.csv', index_col=0, parse_dates=True)

# Usar solo precios de cierre
df = data[['Close']].copy()
df.columns = ['price']

# 2. Crear features (variables predictoras)
print("🔧 CREANDO FEATURES...")
print("="*60)

# Crear variables de tiempo
df['day_of_week'] = df.index.dayofweek
df['month'] = df.index.month
df['day_of_year'] = df.index.dayofyear

# Crear features de precio (lags - días anteriores)
for lag in [1, 2, 3, 5, 7, 14, 21, 30]:
    df[f'lag_{lag}'] = df['price'].shift(lag)

# Crear medias móviles
df['ma_7'] = df['price'].rolling(window=7).mean()
df['ma_14'] = df['price'].rolling(window=14).mean()
df['ma_30'] = df['price'].rolling(window=30).mean()

# Crear volatilidad (desviación estándar)
df['volatility_7'] = df['price'].rolling(window=7).std()
df['volatility_14'] = df['price'].rolling(window=14).std()

# Crear retornos
df['returns'] = df['price'].pct_change()
df['returns_lag_1'] = df['returns'].shift(1)
df['returns_lag_2'] = df['returns'].shift(2)

# Eliminar filas con NaN (primeros días sin datos suficientes)
df = df.dropna()

print(f"✅ Datos listos: {len(df)} filas")
print(f"📅 Desde: {df.index[0].date()} hasta: {df.index[-1].date()}")
print()

# 3. Dividir en entrenamiento (2020-2023) y prueba (2024)
print("✂️ DIVIDIENDO DATOS EN ENTRENAMIENTO Y PRUEBA...")
print("="*60)

train_data = df[df.index.year <= 2023]
test_data = df[df.index.year == 2024]

# Features (X) y target (y)
feature_cols = [col for col in df.columns if col != 'price']
X_train = train_data[feature_cols]
y_train = train_data['price']
X_test = test_data[feature_cols]
y_test = test_data['price']

print(f"📚 Entrenamiento: {len(X_train)} días (2020-2023)")
print(f"🎯 Prueba: {len(X_test)} días (2024)")
print()

# 4. Escalar features
print("⚙️ ESCALANDO FEATURES...")
print("="*60)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Entrenar modelo Random Forest
print("🤖 ENTRENANDO MODELO RANDOM FOREST...")
print("="*60)
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)
print("✅ Modelo entrenado!")
print()

# 6. Hacer predicciones
print("🔮 HACIENDO PREDICCIONES...")
print("="*60)
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# 7. Evaluar el modelo
print("📈 EVALUANDO RENDIMIENTO...")
print("="*60)

# Métricas en entrenamiento
train_mae = mean_absolute_error(y_train, y_pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
train_r2 = r2_score(y_train, y_pred_train)

# Métricas en prueba
test_mae = mean_absolute_error(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_r2 = r2_score(y_test, y_pred_test)

print("ENTRENAMIENTO (2020-2023):")
print(f"  MAE (Error Absoluto Medio): ${train_mae:,.2f}")
print(f"  RMSE (Error Cuadrático Medio): ${train_rmse:,.2f}")
print(f"  R² (Precisión): {train_r2:.4f}")
print()
print("PRUEBA (2024):")
print(f"  MAE (Error Absoluto Medio): ${test_mae:,.2f}")
print(f"  RMSE (Error Cuadrático Medio): ${test_rmse:,.2f}")
print(f"  R² (Precisión): {test_r2:.4f}")
print()

# 8. VISUALIZAR COMPARATIVA
print("🎨 GENERANDO GRÁFICOS COMPARATIVOS...")
print("="*60)

# Crear figura con 3 subplots
fig, axes = plt.subplots(3, 1, figsize=(15, 12))
fig.suptitle('Bitcoin: Comparativa Datos Reales vs Predicciones del Modelo', fontsize=16, fontweight='bold')

# Gráfico 1: Predicciones vs Reales (2024 completo)
ax1 = axes[0]
ax1.plot(test_data.index, y_test, label='Datos Reales', color='blue', linewidth=2)
ax1.plot(test_data.index, y_pred_test, label='Predicciones', color='red', linestyle='--', linewidth=1.5, alpha=0.8)
ax1.fill_between(test_data.index, y_test, y_pred_test, alpha=0.2, color='gray')
ax1.set_title('Comparativa 2024: Real vs Predicción', fontsize=12)
ax1.set_xlabel('Fecha')
ax1.set_ylabel('Precio BTC (USD)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Gráfico 2: Error de predicción
ax2 = axes[1]
error = y_test - y_pred_test
ax2.plot(test_data.index, error, color='purple', linewidth=1.5)
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax2.fill_between(test_data.index, 0, error, where=(error>0), color='green', alpha=0.3, label='Sobreestimación')
ax2.fill_between(test_data.index, 0, error, where=(error<0), color='red', alpha=0.3, label='Subestimación')
ax2.set_title('Error de Predicción (Real - Predicción)', fontsize=12)
ax2.set_xlabel('Fecha')
ax2.set_ylabel('Error (USD)')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='x', rotation=45)

# Gráfico 3: Comparativa de precios (entrenamiento + prueba)
ax3 = axes[2]
ax3.plot(df.index, df['price'], label='Datos Reales', color='blue', linewidth=1, alpha=0.7)
ax3.plot(test_data.index, y_pred_test, label='Predicciones 2024', color='red', linestyle='--', linewidth=2)
ax3.axvline(x=pd.Timestamp('2024-01-01'), color='black', linestyle='-', linewidth=1, alpha=0.5, label='Inicio 2024')
ax3.set_title('Serie Completa: Entrenamiento (2020-2023) y Predicciones (2024)', fontsize=12)
ax3.set_xlabel('Fecha')
ax3.set_ylabel('Precio BTC (USD)')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('results/comparativa_real_vs_prediccion.png', dpi=150, bbox_inches='tight')
plt.show()

# 9. Guardar resultados en CSV
print("💾 GUARDANDO RESULTADOS...")
print("="*60)

resultados = pd.DataFrame({
    'fecha': test_data.index,
    'precio_real': y_test,
    'precio_predicho': y_pred_test,
    'error': error,
    'error_porcentual': (error / y_test) * 100
})
resultados.to_csv('results/predicciones_vs_reales_2024.csv', index=False)
print("✅ Resultados guardados en: results/predicciones_vs_reales_2024.csv")
print("✅ Gráfico guardado en: results/comparativa_real_vs_prediccion.png")

# 10. Mostrar resumen final
print()
print("="*60)
print("📊 RESUMEN FINAL")
print("="*60)
print(f"Error promedio en 2024: ${test_mae:,.2f}")
print(f"Precisión del modelo (R²): {test_r2:.2%}")
print(f"Días con error < 5%: {(abs(error) / y_test * 100 < 5).sum()} de {len(error)} días")
print(f"Días con error < 10%: {(abs(error) / y_test * 100 < 10).sum()} de {len(error)} días")
print("="*60)

# Mostrar feature importance
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False).head(10)

print("\n📈 TOP 10 FEATURES MÁS IMPORTANTES:")
print(feature_importance.to_string(index=False))