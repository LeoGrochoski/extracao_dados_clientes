import csv
import json
import xml.etree.ElementTree as ET
from typing import List, Dict
from faker import Faker
from unidecode import unidecode

fake = Faker('pt_BR')  # Setei português para gerar os dados de clientes

def gerar_dados_csv(num_registros: int = 20) -> List[Dict[str, str]]:
    """
    Esta função tem o objetivo de gerar dados sintéticos para clientes com o formato .csv,
    estes dados são gerados a partir da biblioteca faker.
    """
    dados = []
    for _ in range(num_registros):
        dados.append({
            "nome": unidecode(fake.name()),
            "email": unidecode(fake.email()),
            "telefone": unidecode(fake.phone_number()),
            "endereco": unidecode(fake.address()),
            "renda": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return dados

def gerar_dados_json(num_registros: int = 20) -> List[Dict[str, str]]:
    """
    Esta função tem o objetivo de gerar dados sintéticos para clientes com o formato .json,
    estes dados são gerados a partir da biblioteca faker.
    """
    dados = []
    for _ in range(num_registros):
        dados.append({
            "nome": fake.name(),
            "email": fake.email(),
            "telefone": fake.phone_number(),
            "endereco": fake.address(),
            "renda": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return dados

def gerar_dados_xml(num_registros: int = 20) -> List[Dict[str, str]]:
    """
    Esta função tem o objetivo de gerar dados sintéticos para clientes com o formato .xml,
    estes dados são gerados a partir da biblioteca faker.
    """
    dados = []
    for _ in range(num_registros):
        dados.append({
            "nome": fake.name(),
            "email": fake.email(),
            "telefone": fake.phone_number(),
            "endereco": fake.address(),
            "renda": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return dados

def salvar_csv(dados: List[Dict[str, str]], nome_arquivo: str) -> None:
    """
    Função que salva os dados em formato CSV.
    """
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'email', 'telefone', 'endereco', 'renda']
        gerador = csv.DictWriter(arquivo_csv, fieldnames=campos)
        gerador.writeheader()
        for dado in dados:
            gerador.writerow(dado)

def salvar_json(dados: List[Dict[str, str]], nome_arquivo: str) -> None:
    """
    Função que salva os dados em formato JSON.
    """
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def salvar_xml(dados: List[Dict[str, str]], nome_arquivo: str) -> None:
    """
    Função que salva os dados em formato XML.
    """
    raiz = ET.Element("dados")
    for dado_x in dados:
        registro = ET.SubElement(raiz, "registro")
        for chave, valor in dado_x.items():
            ET.SubElement(registro, chave).text = str(valor)
    tree = ET.ElementTree(raiz)
    tree.write(nome_arquivo, encoding="utf-8", xml_declaration=True)

# Define os nomes dos arquivos
csv_nome_arquivo: str = 'C:\\Lab\\ibm_project_etl\\data\\dados_clientes.csv'
json_nome_arquivo: str = 'C:\\Lab\\ibm_project_etl\\data\\dados_clientes.json'
xml_nome_arquivo: str = 'C:\\Lab\\ibm_project_etl\\data\\clientes.xml'

# Gera os dados para cada tipo de arquivo
dados_csv: List[Dict[str, str]] = gerar_dados_csv()
dados_json: List[Dict[str, str]] = gerar_dados_json()
dados_xml: List[Dict[str, str]] = gerar_dados_xml()

# Salva os dados em cada formato
salvar_csv(dados_csv, csv_nome_arquivo)
salvar_json(dados_json, json_nome_arquivo)
salvar_xml(dados_xml, xml_nome_arquivo)

# Retorna os nomes dos arquivos
csv_nome_arquivo, json_nome_arquivo, xml_nome_arquivo
