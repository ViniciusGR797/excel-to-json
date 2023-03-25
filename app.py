import pandas as pd
import json

# Ler o arquivo Excel
df = pd.read_excel('test.xlsx')

# Converter os dados para um dicionário
data = df.to_dict(orient='records')

# Converter o dicionário para um objeto JSON
json_data = json.dumps(data)

# Salvar o JSON em um arquivo
with open('test.json', 'w') as f:
    f.write(json_data)
