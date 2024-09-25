import pandas as pd
import json
import os
import glob

from utils_log import log_decorator

"""
Função de extract lê e consolida os JSON
"""
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) 
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

"""
Função de transformação - Inclusão de uma nova coluna
"""
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

"""
Função load - Carregar dados
"""
def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)

if __name__ == "__main__":
    pasta_argumento = "data"
    data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    formato_de_saida: list = ["csv", "parquet"]
    carregar_dados(data_frame_calculado, formato_de_saida)
