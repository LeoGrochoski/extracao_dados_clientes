# ETL - Dados de Clientes

## Sobre o Projeto

Este projeto é uma extensão do projeto do Curso da IBM sobre a aula de ETL, ele tem a funcionalidade de pegar arquivos de um diretorio especifico, e extrair informações dos arquivos seja ele xml, csv ou json, resolvi implementar alguns conhecimentos recém adquiridos como POO e Type Hint para criar um codigo mais limpo e facil de ser lido. Além de documentar o projeto desde a primeira linha de codigo. 

Ele contem os dados de Clientes como e-mail, telefone, endereço e renda. No passo de transformação a renda está com os caracteres "R$" e para manipulações futuras é interessantes que ele seja uma dado float então é feito a transformação, o mesmo é feito com o telefone que é despadronizado, e padronizamos ele. 

Por fim geramos um dataframe e um csv com os dados tratados. 


## Tecnologias utilizadas

O ETL todo é feito em python, a extração utilizamos bibliotecas especificas para tratamento dos arquivos e seus respectivos formatos, para a transformação utilizamos regex e a principal biblioteca para isso é a re, e o carregamento utilizei python pandas, além disso implementei um sistema de log que verifica os inicios e terminos das etapas e registra a hora, utilizei a biblioteca datetime.

Acredito que o que mais legal desse projeto foi a documentação dele utilizando MKDocs, fica facil demais utilizar as docstrings, além da organização do codigo. 

E por fim os dados utilizados foram gerados de forma sintetica usando a bilbioteca Faker, queria muito utilizar novametne a biblioteca e com isso criei um script que me gera dados sinteticos dos clientes e os salva em 3 formatos diferentes de arquivo. 

## Como Rodar o Projeto

Primeiramente caso queira dados novos é interessante rodar o arquivo gerar_dados.py e ele vai criar as bases para trabalhar, depois bastar acessar a pasta etl_code e rodar o arquivo carregamento_dados.py para o etl todo rodar, ele irá gerar o arquivo csv e o arquivo de log. 

## Documentação