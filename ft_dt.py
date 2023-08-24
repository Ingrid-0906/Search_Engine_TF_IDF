import pickle
import sys
import json
import math
import nltk
import datetime

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

class SearchEngine:
    """A classe é definida e possui vários métodos para realizar a análise e cálculos."""
    
    def __init__(self, input_data, output_data):
        """
        Inicializa um objeto SearchEngine.

        :param input_data: Caminho para o arquivo JSON de entrada
        :param output_data: Caminho para o arquivo de saída pickle para salvar os resultados
        """
        
        self.input_data = input_data
        self.output_data = output_data
        self.tf_idf = {}


    def process_data(self):
        """
        Processa os dados de entrada e calcula os escores TF-IDF.

        Lê os dados JSON, calcula os escores TF-IDF para as palavras e armazena os resultados em self.tf_idf.
        """
        self.tf_idf = {}
        with open(self.input_data.lower()) as file:
            data = [json.loads(line) for line in file]
            
        for data_entry in data:
            sacos = data_entry['texto'][0].split()
            for word in sacos:
                word = word.lower()
                if word in stopwords:
                    continue
                decoded_word = word.encode('utf-8').decode('utf-8')
                self.tf_idf.setdefault(decoded_word, []).append({
                    'id': data_entry['id'],
                    'titulo': data_entry['titulo'],
                    'resumo': data_entry['texto'][:15],
                    'url': data_entry['url'],
                    'score': (sacos.count(word) * math.log10(len(data) / len(sacos)))
                })


    def save_result(self):
        """
        Salva os resultados TF-IDF calculados em um arquivo pickle.

        Grava os dados self.tf_idf no arquivo pickle de saída.
        """
        with open(self.output_data, 'wb') as file:
            pickle.dump(self.tf_idf, file)
