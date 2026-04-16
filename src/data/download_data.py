"""
download_data.py - Descargar datos históricos de criptos 2020-2024
"""

import yfinance as yf
from pathlib import Path
import pandas as pd

# Crear carpetas si no existen
Path("data/raw").mkdir(parents=True, exist_ok=True)

def download_crypto_data(symbol: str = "BTC-USD", start: str = "2020-01-01", end: str = "2024-12-31"):
    """Descargar datos históricos de una criptomoneda"""
    
    print(f"📥 Descargando {symbol} desde {start} hasta {end}...")
    
    # Solución 1: Usar auto_adjust=False para obtener más datos
    data = yf.download(
        symbol, 
        start=start, 
        end=end,
        auto_adjust=False,  # Importante para datos completos
        progress=True
    )
    
    if data.empty:
        # Solución 2: Intentar con período específico
        print("⚠️ Intentando método alternativo...")
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start, end=end, auto_adjust=False)
    
    # Guardar en CSV
    filename = f"data/raw/{symbol.replace('-', '_')}_2020_2024.csv"
    data.to_csv(filename)
    
    print(f"✅ Datos guardados en: {filename}")
    print(f"📊 Filas descargadas: {len(data)}")
    if len(data) > 0:
        print(f"📅 Desde: {data.index[0]} hasta: {data.index[-1]}")
        print(f"\nPrimeras 3 filas:\n{data.head(3)}")
    else:
        print("❌ No se descargaron datos")
    
    return data

if __name__ == "__main__":
    # Descargar Bitcoin 2020-2024
    btc_data = download_crypto_data("BTC-USD", "2020-01-01", "2024-12-31")
    
    # Si solo tienes 2020, prueba con fechas más específicas
    if btc_data is not None and len(btc_data) < 365:
        print("\n⚠️ Datos limitados detectados. Intentando descarga por partes...")
        
        # Descargar por años
        for year in [2020, 2021, 2022, 2023, 2024]:
            start_date = f"{year}-01-01"
            end_date = f"{year}-12-31"
            print(f"\n📥 Descargando {year}...")
            year_data = yf.download("BTC-USD", start=start_date, end=end_date)
            print(f"Año {year}: {len(year_data)} filas")
            
            if year == 2020:
                all_data = year_data
            else:
                all_data = pd.concat([all_data, year_data])
        
        # Guardar datos combinados
        all_data.to_csv("data/raw/BTC_USD_2020_2024_completo.csv")
        print(f"\n✅ Total datos combinados: {len(all_data)} filas")