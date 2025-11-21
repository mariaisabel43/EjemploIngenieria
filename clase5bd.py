import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar una base de datos en línea (ejemplo: Titanic dataset de seaborn)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# 2. Mostrar las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# 3. Generar estadísticas básicas de columnas numéricas
print("\nEstadísticas básicas:")
print(df.describe())
print("\nColumnas del dataset:")
print(df.columns)
# 4. Estadísticas adicionales (por ejemplo, mediana y moda de la edad)
print("\nEstadísticas adicionales:")
print(f"Mediana de edad: {df['age'].median()}")
print(f"Moda de edad: {df['age'].mode()[0]}")

# 5. Gráfico de barras: número de pasajeros por clase
clase_counts = df['class'].value_counts()

plt.figure(figsize=(8, 6))
clase_counts.plot(kind='bar', color='skyblue')
plt.title('Número de Pasajeros por Clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
#plt.xticks(rotation=0)
#plt.tight_layout()
plt.show()