import csv

def listar_conteudo(articles.csv):
    with open(articles.csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)
            
            arquivo_csv = 'This Pc/Downloads/articles.csv'
listar_conteudo(arquivo_csv)
