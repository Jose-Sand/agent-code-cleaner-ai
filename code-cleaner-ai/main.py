import os
import argparse
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np

def get_code(path):
    with open(path, 'r') as f:
        return f.read()

def suggest_changes(code):
    # Preprocesamiento del código (por ejemplo, tokenización y embeddings)
    inputs = tokenizer.encode_plus(
        code,
        add_special_tokens=True,
        max_length=512,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

    # Utilizar el modelo para hacer predicciones
    outputs = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])

    # Extraer la probabilidad de que sea código limpio
    score = np.mean(outputs.logits)

    # Sugerir cambios si la probabilidad es baja
    if score < 0.5:
        return "El código puede ser optimizado"
    else:
        return "El código parece estar bien"

def run_cli():
    parser = argparse.ArgumentParser(description='Code Cleaner AI')
    parser.add_argument('--path', type=str, help='Path al archivo de código a limpiar')
    args = parser.parse_args()

    code = get_code(args.path)
    suggestions = suggest_changes(code)

    print(suggestions)

if __name__ == '__main__':
    model_name = 'distilbert-base-uncased'
    tokenizer_name = f'{model_name}-tokenizer'

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    run_cli()