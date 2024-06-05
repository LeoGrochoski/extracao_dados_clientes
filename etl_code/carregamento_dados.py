from datetime import datetime 
from transformacao_dados import transformacao
from extracao_dados import extracao
import pandas as pd


arquivo_log = r"C:/Lab/extracao_dados_clientes/data/arquivo_log.txt" 
arquivo_salvo = r"C:/Lab/extracao_dados_clientes/data/dados_clientes_tratados.csv" 

def carrega_dados(arquivo_salvo, dados_transformados): 
    """
    Função para criar arquivo csv que ira armazenar os dados transformados
    """
    dados_transformados.to_csv(arquivo_salvo)
    
def progresso_log(mensagem): 
    """
    Função para criação do log de eventos do ETL
    """
    formato_timestamp = '%Y-%h-%d-%H:%M:%S' # Ano-Mes-Dia-Hora-Minuto-Segundo
    now = datetime.now() 
    timestamp = now.strftime(formato_timestamp) 
    with open(arquivo_log,"a") as f: 
        f.write(mensagem + "[" + timestamp + "]"'\n') 
        
# Log da inicialização do processo de ETL
progresso_log("ETL Iniciado: ") 
 
# Log do inicio da etapa de extracao 
progresso_log("Fase de Extracao iniciada: ") 
dados_extraidos = extracao() 
 
# Log do processo de extracao completo 
progresso_log("Fase de Extracao finalizada: ") 
 
# Log do inicio da etapa de transformacao 
progresso_log("Fase de Transformacao iniciada: ") 
dados_transformados = transformacao(dados_extraidos) 
print("Dados Transformados: ") 
print(dados_transformados) 
 
# Log do processo de transformacao completo 
progresso_log("Fase de Transformacao finalizada: ") 
 
# Log do inicio da etapa de carregamento 
progresso_log("Fase de Carregamento iniciada: ") 
carrega_dados(arquivo_salvo,dados_transformados) 
 
# Log do processo de carregamento completo 
progresso_log("Fase de Carregamento finalizado: ") 
 
# Log do ETL completo
progresso_log("ETL Finalizado: ")