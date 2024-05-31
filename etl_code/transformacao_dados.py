import re # Biblioteca para utilização de regex e localização de alfanumericos. 
import pandas as pd

def transformacao(info): 
    """
    Função para transformacão dos dados dos arquivos, retirando tudo que nao for numérico.
    """

    info['telefone'] = info['telefone'].str.replace(r'[^a-zA-Z0-9 ]+', '').str.replace(r'\s+', ' ').str.strip()
    info['renda'] = info['renda'].str[2:].astype(float)

    return info 
