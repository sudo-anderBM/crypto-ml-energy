import yfinance as yf
from pathlib import Path
import pandas as pd

Path("data/raw").mkdir(parents=True, exist_ok=True)

print("Descargando Bitcoin 2020-2024...")
print("Por favor espera...")

# Método más confiable
btc = yf.Ticker("BTC-USD")
data = btc.history(start="2020-01-01", end="2024-12-31", interval="1d")

print(f"✅ Datos descargados: {len(data)} filas")
print(f"📅 Desde: {data.index[0]} hasta: {data.index[-1]}")

# Guardar
data.to_csv("data/raw/BTC_USD_2020_2024.csv")
print("💾 Guardado en: data/raw/BTC_USD_2020_2024.csv")
print(f"\nVista previa:\n{data.head()}")