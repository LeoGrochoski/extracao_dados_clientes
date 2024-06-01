# Sobre o Projeto

## ETL de arquivos de extensões diversas

O projeto visa o aprendizado de trabalho com extração, transformação e carregamendo de dados vindos de fontes como .csv, .json e .xml.

## Objetivos

O objetivo principal é manter um projeto coeso, documentado e que sirva de consulta para ferramentas como bibliotecas comuns em etls, documentação, uso de ambiente virtual e versionamento de codigo.

## Como executar o projeto

1 – Clonar o Repositorio: 
~~~
git clone https://github.com/LeoGrochoski/extracao_dados_clientes
~~~
2 - Iniciar o ambiente Virtual:
~~~
 python -m venv .venv
~~~
3 – Instalar as bibliotecas do projeto, pode verificar no arquivo requirements.txt.
4 – Caso queira utilizar o script para gerar dados sintéticos, rodar o script gerar_dados.py: 
~~~
python gerar_dados.py
~~~
5 – Para rodar o codigo de carregamento do ETL, ele já executa automaticamente a extração e transformação, arquivo carregamento_dados.py: 
~~~
python carregamento_dados.py
~~~
6 - É gerado o arquivo dados_clientes_tratados.csv no diretorio "data" contendo os dados tratados.

7  - Também é gerado o arquivo de log: arquivo_log.txt

## Principais bibliotecas e suas versões

- Python 3.12.1
- Pandas 2.2.2
- MKDocs 1.60
- Markdown 3.6
- Unidecode 1.3.8


