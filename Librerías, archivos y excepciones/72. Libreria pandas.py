import pandas as pd

datos = {
    "Producto": ["bimbo", "alpura", "suavitel", "pachoncito"],
    "Precio": [45, 27, 72, 103],
    "Cantidad": [400, 350, 273, 321]
}

df = pd.DataFrame(datos)
print(df)
print("\nEstadísticas principales:")
print(df.describe())
