import pandas as pd

data = pd.read_json("empresas.json", typ=series)

df = pd.json_normalize(data['empresas'])

df.to_excel('empresas.xlsx', index=False)