import unittest
from analysis import analyze_response

class TestAnalysis(unittest.TestCase):
    def test_valid_response(self):
        prompt = "Explain the concept of neural networks."
        response = "Neural networks consist of layers and weights."
        feedback = analyze_response(prompt, response)
        self.assertIn("Your response is", feedback)

    def test_invalid_prompt(self):
        prompt = "Explain quantum mechanics."
        response = "This is a physics topic."
        feedback = analyze_response(prompt, response)
        self.assertEqual(feedback, "No specific scoring criteria for this prompt.")

if __name__ == "__main__":
    unittest.main()
