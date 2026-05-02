import unittest
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from code_cleaner_ai.main import CodeCleanerAI

class TestCodeCleanerAI(unittest.TestCase):

    def setUp(self):
        self.tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased')

    def test_recommend_changes(self):
        code_to_clean = "def hello_world():\n  print('Hello World')"
        cleaner = CodeCleanerAI(self.tokenizer, self.model)
        recommendations = cleaner.recommend_changes(code_to_clean)
        self.assertGreater(len(recommendations), 0)

    def test_reduce_code_size(self):
        code_to_clean = "def hello_world():\n  print('Hello World')\n\nhello_world()"
        cleaner = CodeCleanerAI(self.tokenizer, self.model)
        cleaned_code = cleaner.reduce_code_size(code_to_clean)
        self.assertLess(len(cleaned_code), len(code_to_clean))

    def test_improve_readability(self):
        code_to_clean = "def hello_world():\n  print('Hello World')\n\nhello_world()"
        cleaner = CodeCleanerAI(self.tokenizer, self.model)
        cleaned_code = cleaner.improve_readability(code_to_clean)
        self.assertLess(len(cleaned_code.split('\n')), len(code_to_clean.split('\n')))

if __name__ == '__main__':
    unittest.main()