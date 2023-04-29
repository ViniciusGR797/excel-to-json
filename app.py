import pandas as pd
import json
import os.path

filename = 'test.xlsx'
json_filename = 'test.json'

# Verificar se o arquivo Excel existe
if not os.path.isfile(filename):
    print(f'File "{filename}" not found.')
    exit()

try:
    # Ler o arquivo Excel
    df = pd.read_excel(filename)

    # Converter os dados para um dicionário
    data = df.to_dict(orient='records')

    # Converter o dicionário para um objeto JSON, mantendo a acentuação
    json_data = json.dumps(data, ensure_ascii=False)

    # Salvar o JSON em um arquivo
    with open(json_filename, 'w', encoding='utf-8') as f:
        f.write(json_data)
        print(f'File "{json_filename}" saved successfully.')
except Exception as e:
    print('An error occurred:', e)
