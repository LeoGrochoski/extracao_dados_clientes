import re

def transformacao(dados): 
    """
    Função para transformacao dos dados dos arquivos, retirando tudo que nao for numerico
    """
    dados['telefone'] = re.sub('[^0-9]', '', dados['telefone'])
    dados['renda'] = re.sub('[^0-9]', '', dados['renda'])
    
    return dados 
