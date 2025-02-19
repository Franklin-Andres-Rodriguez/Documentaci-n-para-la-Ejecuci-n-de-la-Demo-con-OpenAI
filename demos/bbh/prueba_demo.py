import os
import openai
from dotenv import load_dotenv

# Cargar el archivo .env desde el directorio actual
load_dotenv(override=True)

# Configurar OpenAI con la API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_api(messages):
    response = openai.ChatCompletion.create(
        model=os.getenv("OPENAI_MODEL_NAME"),  # Ejemplo: "gpt-3.5-turbo"
        messages=messages,
        temperature=0.0
    )
    prediction = response.choices[0].message.content
    return prediction

def extract_between(start, end, text):
    start_index = text.find(start)
    if start_index == -1:
        return ''
    start_index += len(start)
    end_index = text.find(end, start_index)
    if end_index == -1:
        return ''
    return text[start_index:end_index]

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "Eres un asistente de pruebas."},
        {"role": "user", "content": "Dime algo interesante."}
    ]
    
    respuesta = call_api(messages)
    print("Respuesta del API:", respuesta)
    
    extraido = extract_between("<ANS_START>", "<ANS_END>", respuesta)
    print("Texto extraído:", extraido)

