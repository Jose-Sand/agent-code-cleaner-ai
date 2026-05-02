import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def get_tokenizer(model_name):
    """
    Carga un modelo de tokenización a partir del nombre del modelo.

    Args:
        model_name (str): Nombre del modelo de tokenización.

    Returns:
        tokenizer: Modelo de tokenización cargado.
    """
    return AutoTokenizer.from_pretrained(model_name)

def get_model(model_name):
    """
    Carga un modelo de secuencia de clasificación a partir del nombre del modelo.

    Args:
        model_name (str): Nombre del modelo de secuencia de clasificación.

    Returns:
        model: Modelo de secuencia de clasificación cargado.
    """
    return AutoModelForSequenceClassification.from_pretrained(model_name)

def tokenize_text(text, tokenizer):
    """
    Tokeniza un texto a partir de un modelo de tokenización.

    Args:
        text (str): Texto a tokenizar.
        tokenizer: Modelo de tokenización.

    Returns:
        tokens: Tokens del texto.
    """
    return tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

def predict(model, input_ids, attention_mask):
    """
    Realiza una predicción con un modelo de secuencia de clasificación.

    Args:
        model: Modelo de secuencia de clasificación.
        input_ids (np.array): IDs de entrada del modelo.
        attention_mask (np.array): Máscara de atención del modelo.

    Returns:
        prediccion: Predicción realizada por el modelo.
    """
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    return outputs

def evaluate_prediction(prediction):
    """
    Evaluación de la predicción realizada por el modelo.

    Args:
        prediction (np.array): Predicción realizada por el modelo.

    Returns:
        score: Puntuación de la predicción.
    """
    return np.argmax(prediction)