import openai
import requests
import os

API_KEY = "" # API KEY OpenAI

def gerar_imagem(prompt: str, nome_arquivo:str, path:str):
    client = openai.OpenAI(api_key=API_KEY)
    if(len(API_KEY) < 10):
        print("É necessário uma chave de API OpenAI (python/BricolagemOpenIA.py - API_KEY)")
        exit(1)

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )


    url_imagem = response.data[0].url
    img_data = requests.get(url_imagem).content

    os.makedirs(path, exist_ok=True)
    with open(path+'/'+nome_arquivo, 'wb') as f:
        f.write(img_data)

