import unittest
from utils import semantic_score, keyword_score, extract_keywords

class TestUtils(unittest.TestCase):
    def test_semantic_score(self):
        prompt = "What is supervised learning?"
        response = "Supervised learning uses labeled data."
        feedback, score = semantic_score(prompt, response)
        self.assertIn("Good semantic alignment!", feedback)

    def test_keyword_score(self):
        response = "Supervised learning involves labels and classification."
        keywords = ["labels", "classification", "regression"]
        feedback, score = keyword_score(response, keywords)
        self.assertIn("Matched", feedback)

    def test_extract_keywords(self):
        prompt = "Explain the concept of reinforcement learning."
        keywords = extract_keywords(prompt)
        self.assertIn("reinforcement", keywords)
        self.assertIn("learning", keywords)

if __name__ == "__main__":
    unittest.main()
