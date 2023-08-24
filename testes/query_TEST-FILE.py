import sys
import json
import pickle
import unittest

class Query:
    def __init__(self, index_path, n, keyword):
        self.index_path = index_path
        self.n = int(n)
        self.keywords = keyword.split()
        self.result_data = []

    def process_index(self):
        with open(self.index_path, 'rb') as index_file:
            index_data = pickle.load(index_file)

        relevant_docs = {}
        for keyword in self.keywords:
            relevant_docs.update({doc['id']: doc for doc in index_data.get(keyword, [])})

        self.result_data = list(relevant_docs.values())

    def display_results(self):
        for doc in sorted(self.result_data, key=lambda k: k['score'], reverse=True)[:self.n]:
            print(json.dumps(doc))

class TestQueryMethods(unittest.TestCase):
    def setUp(self):
        self.index_path = 'test_index.pkl'
        self.test_index_data = {
            'keyword1': [{'id': 1, 'score': 0.8}],
            'keyword2': [{'id': 2, 'score': 0.7}],
            'keyword3': [{'id': 1, 'score': 0.5}]
        }
        with open(self.index_path, 'wb') as index_file:
            pickle.dump(self.test_index_data, index_file)

    def test_process_index(self):
        query = Query(self.index_path, 10, 'keyword1 keyword2')
        query.process_index()
        self.assertEqual(len(query.result_data), 2)

    def test_display_results(self):
        query = Query(self.index_path, 1, 'keyword1')
        query.process_index()
        self.assertIsNone(query.display_results())

if __name__ == "__main__":
    unittest.main()
