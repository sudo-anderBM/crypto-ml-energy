"""
ver_datos.py - Visualizar los datos descargados
"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('data/raw/BTC_USD_2020_2024.csv', index_col=0, parse_dates=True)

print('📊 RESUMEN DE DATOS BTC 2020-2024')
print('='*50)
print(f'Total de filas: {len(data)}')
print(f'Columnas: {list(data.columns)}')
print()

# Mostrar por año
for año in [2020, 2021, 2022, 2023, 2024]:
    datos_año = data[data.index.year == año]
    print(f'{año}: {len(datos_año)} filas')
    print(f'  Desde: {datos_año.index[0].date()}')
    print(f'  Hasta: {datos_año.index[-1].date()}')
    print(f'  Precio mínimo: ${datos_año["Close"].min():.2f}')
    print(f'  Precio máximo: ${datos_año["Close"].max():.2f}')
    print()

# Estadísticas básicas
print('='*50)
print('ESTADÍSTICAS GENERALES:')
print('='*50)
print(f'Precio promedio: ${data["Close"].mean():.2f}')
print(f'Volumen promedio: {data["Volume"].mean():.0f}')
print()

# Gráfico rápido (opcional)
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], linewidth=1, color='blue')
plt.title('Bitcoin Price (2020-2024)', fontsize=14)
plt.xlabel('Fecha')
plt.ylabel('Precio USD')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('data/raw/bitcoin_price_2020_2024.png', dpi=100)
print('📈 Gráfico guardado en: data/raw/bitcoin_price_2020_2024.png')
plt.show()