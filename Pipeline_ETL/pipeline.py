# %%
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# %%
#EXTRACT

import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

#%%

import requests
import json

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# %%
#TRANSFORM

openai_api_key = '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'

# %%
# import os
# import openai

# openai.api_key = os.getenv("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")

# def generate_ai_news(user):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system", 
#                 "content": "Você é um especialista em marketing bancário."
#             },
#             {
#                 "role": "user", 
#                 "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
#             }
#         ]
#     )
#     return completion.choices[0].message.content.strip('\"')

for user in users:
    # news = generate_ai_news(user)
    user['news'].append({"description": f"{user['name']}, invista hoje para garantir um futuro seguro! "})
    print(user)

# %%
#LOAD

def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    sucess = update_user(user)
    print(f"User {user['name']} updated? {sucess}!")