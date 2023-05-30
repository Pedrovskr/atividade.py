import csv
import streamlit as st
def listar_conteudo(nomearquivo):
    with open(nomearquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            st.write(linha)

arquivo = 'articles.csv'
listar_conteudo(arquivo)
