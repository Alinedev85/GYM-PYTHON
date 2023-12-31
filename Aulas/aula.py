# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wLkBEnrfI9eIUPaelxj6X4Xrahd1lB-S
"""


import pandas  as pd

url = "https://raw.githubusercontent.com/escola-de-dados/notebooks-python-pandas/master/mlb.csv"

#ler um arquivo csv e transformando em dataframe

try:
  response = requests.get(url)
  response.raise_for_status() #lanca uma exceção/ erro em caso de erro http

  #usar stringIO como se fosse arquivo
  df = pd.read_csv(StringIO(response.text))

  #exibir as primeiras linhas do dataframe

  print("primeiras linhas do DataFrame")
  print(df.head())

except requests.exceptions.RequestException as error:
  print(f"erro ao ler o arquivo .csv: {error}")

import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/escola-de-dados/notebooks-python-pandas/master/mlb.csv"

try:
    # Realiza a solicitação HTTP
    response = requests.get(url)
    response.raise_for_status()  # Lança uma exceção/erro em caso de erro HTTP

    # Usa StringIO como se fosse um arquivo
    df = pd.read_csv(StringIO(response.text))

    # Exibe as primeiras linhas do DataFrame
    print("Primeiras linhas do DataFrame:")
    print(df.head())

except requests.exceptions.RequestException as error:
    print(f"Erro ao ler o arquivo .csv: {error}")

#ordene o data df pela coluna name

df.sort_values("NAME")





df.tail() #ultimo registro

df.sample(10) # linhas aleatórias no codigo

df.shape # verificar cabecalho (linhas, colunas )

df.dtypes #lista o tipos de dados e objetos que tem nas colunas

#ordenação dos dados

df.sort_values("SALARY")

df.sort_values("SALARY", ascending=False) #deixar o salarios por ordem do maior para o menor

df.sort_values("SALARY", ascending=False).head() #deixar o salarios por ordem do maior para o menor mostrando apenas o cabecalho

df[df.SALARY > 1000]

df.sort_values(["SALARY", "TEAM"], ascending=[False, True]).head()

ordenacaoPorTime = df.sort_values('TEAM')
ordenacaoPorTime

import requests
import pandas as pd

from io import StringIO

url = "https://repositorio.seade.gov.br/dataset/aacd1b41-25de-4cae-9ae6-526f9417a53b/resource/bbce7c2c-d1ec-4c09-b64c-8d4ed7c2207d/download/econ_comex.csv"

try:

    response = requests.get(url, verify=False)
    response.raise_for_status()

    df = pd.read_csv(StringIO(response.text))


    print("Primeiras linhas do DataFrame:")
    print(df.head())

except requests.exceptions.RequestException as error:
    print(f"Erro ao ler o arquivo .csv: {error}")



print(df.columns)





df.sort_values(["Localidades", "Valor das Exportações"], ascending=[False, True]).head()

ordene o dataframe  df pela coluna pos de modo descendente

df.describe() #estatisticas gerais

# mostre todos os dados no dataframe

## para colunas numpéricas, metodos basicos ex:

# df.salary.min()
# df.salary.max()
# df.salary.mediana()
df.salary.mean() # média da coluna espessifica

df[df.salary > 100000]

#select *from dataframe where salary > 100000
