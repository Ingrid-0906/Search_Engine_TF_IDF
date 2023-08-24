import sys
import json
import pickle

class Query:
    def __init__(self, index_path, n, keyword):
        """
        Inicializa um objeto Query.

        :param index_path: Caminho para o arquivo de índice pickle
        :param n: Número máximo de resultados a serem exibidos
        :param keyword: Palavras-chave para a consulta
        """
        self.index_path = index_path
        self.n = int(n)
        self.keywords = keyword.split()
        self.result_data = []


    def process_index(self):
        """
        Processa o arquivo de índice e encontra os documentos relevantes.

        Lê o arquivo de índice pickle e encontra os documentos relevantes com base nas palavras-chave.
        Armazena os resultados em self.result_data.
        """
        with open(self.index_path, 'rb') as index_file:
            index_data = pickle.load(index_file)

        relevant_docs = {}
        for keyword in self.keywords:
            relevant_docs.update({doc['id']: doc for doc in index_data.get(keyword, [])})

        self.result_data = list(relevant_docs.values())


    def display_results(self):
        """
        Exibe os resultados da consulta.

        Exibe os resultados relevantes ordenados por peso em ordem decrescente.
        Limite de resultados é controlado por self.n.
        """
        for doc in sorted(self.result_data, key=lambda k: k['score'], reverse=False)[:self.n]:
            print(json.dumps(doc))

