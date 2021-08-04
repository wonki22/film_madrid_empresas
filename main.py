import pandas as pd

last_update = "20210803"

data = pd.read_json("empresas_" + last_update + ".json", typ=pd.core.series)

df = pd.json_normalize(data['empresas'])

df.to_excel('empresas.xlsx', index=False)