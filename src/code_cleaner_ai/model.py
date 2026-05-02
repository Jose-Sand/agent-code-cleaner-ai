import logging
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np

logging.basicConfig(level=logging.INFO)

class CodeCleanerModel:
    def __init__(self, model_name: str, tokenizer_name: str):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def preprocess_code(self, code: str) -> dict:
        inputs = self.tokenizer(code, return_tensors="pt")
        input_ids = inputs["input_ids"].numpy()[0]
        attention_mask = inputs["attention_mask"].numpy()[0]

        return {
            "input_ids": np.array(input_ids),
            "attention_mask": np.array(attention_mask)
        }

    def make_prediction(self, code: str) -> dict:
        inputs = self.preprocess_code(code)

        outputs = self.model(inputs["input_ids"], attention_mask=inputs["attention_mask"])
        logits = outputs.logits

        return {
            "logits": logits.detach().numpy(),
            "probs": np.exp(logits).detach().numpy()
        }

    def get_recommendations(self, code: str) -> list:
        prediction = self.make_prediction(code)
        probs = prediction["probs"]

        # Example of how to use the probabilities to make recommendations
        recommended_changes = []
        for i in range(len(probs)):
            if probs[i] > 0.5:
                recommended_changes.append(f"Change line {i+1}")

        return recommended_changes

# Example usage
if __name__ == "__main__":
    model_name = "code-cleaner-ai/model"
    tokenizer_name = "code-cleaner-ai/tokenizer"

    model = CodeCleanerModel(model_name, tokenizer_name)
    code = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""

    recommendations = model.get_recommendations(code)

    for recommendation in recommendations:
        logging.info(recommendation)