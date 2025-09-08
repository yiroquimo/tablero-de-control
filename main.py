import pandas as pd
ruta = "https://github.com/VMjavier/claseAnalisisDatos/raw/refs/heads/main/datos_reales.zip"
df = pd.read_csv(ruta)

print(df.head())