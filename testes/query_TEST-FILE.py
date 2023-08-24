import unittest
from io import StringIO
import sys
import pickle
import json

# Importar a classe Query do seu script
from seu_script import Query

class TestQueryMethods(unittest.TestCase):
    def setUp(self):
        # Criar um índice de teste
        self.index_data = {
            'keyword1': [{'id': 1, 'resumo': ['Texto de exemplo contendo keyword1'], 'score': 0.5}],
            'keyword2': [{'id': 2, 'resumo': ['Texto de exemplo contendo keyword2'], 'score': 0.3}]
        }
        self.index_path = 'test_index.pkl'
        with open(self.index_path, 'wb') as index_file:
            pickle.dump(self.index_data, index_file)

    def tearDown(self):
        # Remover o índice de teste
        import os
        if os.path.exists(self.index_path):
            os.remove(self.index_path)

    def test_process_index(self):
        query = Query(self.index_path, 10, 'keyword1')
        query.process_index()
        self.assertEqual(len(query.result_data), 1)
        self.assertEqual(query.result_data[0]['id'], 1)

    def test_display_results(self):
        query = Query(self.index_path, 10, 'keyword2')
        
        # Redirecionar a saída padrão para um buffer para capturar a saída do print
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        query.display_results()

        # Capturar a saída e reverter a alteração na saída padrão
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        # Verificar se a saída contém o resultado esperado
        self.assertIn("keyword2", output)
        self.assertIn("score", output)

if __name__ == '__main__':
    unittest.main()
