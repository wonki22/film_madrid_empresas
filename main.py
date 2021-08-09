import pandas as pd
from os import system

system('node dump_empresas.js');

data = pd.read_json("empresas.json", typ=series)

df = pd.json_normalize(data['empresas'])

df.to_excel('empresas.xlsx', index=False)
