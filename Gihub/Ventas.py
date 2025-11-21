import pandas as pd # pd es la abreviatura de pandas
# cargar el archivo csv
df=pd.read_csv("C:/Users/Rivas/Desktop/base.csv")

print("\nDatos\n")
print(df) # esta df es una variable que visualiza la tabla

# Estadisticas sobre productos
print("Estadisticas de Ventas ")
print("La cantidad ",df["Ganancia"].count())
print("Maximo:",df["Ganancia"].max())
print("Mimimo:",df["Ganancia"].min())
print("Promedio:",round(df["Ganancia"].mean(),2))
print("Mediana:",df["Ganancia"].median())
print("Moda:",df["Ganancia"].mode()[0]) # para que genere otros datos si hay moda escribir 0
print("Desviacion estandar:",round(df["Ganancia"].std(),2))

print("\n Estadisticas de Precios ")
print("Maximo:",df["Precio"].max())
print("Mimimo:",df["Precio"].min())
print("Promedio:",round(df["Precio"].mean(),2))