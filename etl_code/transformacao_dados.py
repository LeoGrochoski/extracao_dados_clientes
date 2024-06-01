import re # Biblioteca para utilização de regex e localização de alfanumericos. 
import pandas as pd

def transformacao(info): 
    """
    Função para transformacão dos dados dos arquivos, retirando tudo que nao for numérico.
    """

    info['telefone'] = info['telefone'].str.replace(r'[^\d]', '', regex=True)
    info['telefone'] = info['telefone'].str.replace(r'^55', '', regex=True)


    return info 
