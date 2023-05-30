import csv

def listar_conteudo(nomearquivo):
    with open(nomearquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)
            
            arquivo = 'This Pc/Downloads/articles.csv'
            listar_conteudo(arquivo)
