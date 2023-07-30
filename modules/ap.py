# api.py

import subprocess
import requests

API_ENDPOINT = "https://us-central1-aiplatform.googleapis.com"
PROJECT_ID = "modular-bot-392623" 
MODEL_ID = "chat-bison"

def call_api(user_input):

  request_json = {
    "instances": [
      {
        "messages": [
          {
            "content": user_input,
            "author": "user",  
          }
        ]
      }
    ]
  }

  access_token = subprocess.check_output(['gcloud', 'auth', 'print-access-token']).decode().strip()

  headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json" 
  }

  url = f"https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict"

  response = requests.post(url, json=request_json, headers=headers)

  if response.status_code != 200:
    print(f"Error: {response.status_code}")
    return

  reply = response.json()['predictions'][0]['candidates'][0]['content']
  
  return reply