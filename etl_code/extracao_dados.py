import pandas as pd # Biblioteca para manipulação de dados em CSV e JSON e transformação em dados tabulares
import glob # Biblioteca para trabalhar com arquivos e diretorios
import xml.etree.ElementTree as ET # Biblioteca para manipulação de dados XML
from datetime import datetime # Biblioteca para trabalhar com data e horario, muito utilizada para geração de logs. 
import os # Biblioteca para realizar operação de sistemas, arquivos e paths

diretorio = "C:\Lab\extracao_dados_clientes\data"


def extracao_csv(arquivo: str) -> pd.DataFrame:
    """
    Função para extrair dados dos arquivos .csv
    """
    try:
        dados_csv = pd.read_csv(arquivo)
        return dados_csv
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV {arquivo}: {e}")
        return pd.DataFrame()

def extracao_json(arquivo: str) -> pd.DataFrame:
    """
    Função para extrair dados dos arquivos .json
    """
    try:
        dados_json = pd.read_json(arquivo)
        return dados_json
    except ValueError as e:
        print(f"Erro ao ler o arquivo JSON {arquivo}: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo JSON {arquivo}: {e}")
        return pd.DataFrame()


def extracao_xml(arquivo: str) -> pd.DataFrame:
    """
    Função para extrair dados dos arquivos .xml
    """
    dados_xml = pd.DataFrame(columns=["nome", "email", "telefone", "endereco", "renda"])
    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()
        for registro in root:
            nome = registro.find("nome").text
            email = registro.find("email").text
            telefone = registro.find("telefone").text
            endereco = registro.find("endereco").text
            renda = registro.find("renda").text
            dados_xml = pd.concat([dados_xml, pd.DataFrame([{"nome": nome, "email": email, "telefone": telefone, "endereco": endereco, "renda": renda}])], ignore_index=True)
    except Exception as e:
        print(f"Erro ao ler o arquivo XML {arquivo}: {e}")
    return dados_xml

# A logica que utilizarei é a criação de um DF vazio para persistir os dados 
# e depois extrair os dados para cada extensâo e concatena-las no dataframe vazio recem criado.


dados_csv = []
dados_json = []
dados_xml = []

def extracao(diretorio):    
    dados_extraidos = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    
    for csvfile in glob.glob(os.path.join(diretorio, "*.csv")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_csv(csvfile))], ignore_index=True) 
         
    for jsonfile in glob.glob(os.path.join(diretorio, "*.json")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_json(jsonfile))], ignore_index=True) 
     
    for xmlfile in glob.glob(os.path.join(diretorio, "*.xml")): 
        dados_extraidos = pd.concat([dados_extraidos, pd.DataFrame(extracao_xml(xmlfile))], ignore_index=True) 
         
    return dados_extraidos


# Concatena os dados extraídos de cada tipo de arquivo
# dados_extraidos = pd.concat(dados_csv + dados_json + dados_xml, ignore_index=True)




