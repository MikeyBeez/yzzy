import subprocess
import requests
import json
import os
import gcloud
import sys
import pinecone

# Import model for embedding 
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to Pinecone
#pinecone.init(api_key='YOUR_API_KEY')
#index = pinecone.Index('chatbot_data')

api_endpoint = "us-central1-aiplatform.googleapis.com"
project_id = "modular-bot-392623"  
model_id = "projects/modular-bot-392623/models/codechat-bison/versions/001"


def sayItPrintIt(reply): 
#   Mute microphone
#   subprocess.call([
#       'osascript',
#       '-e',
#       'set volume input 0'
#   ])
#   cmd = """osascript -e 'set volume input muted true'"""
#   os.system(cmd)
#   os.system("sleep 1")

    print(reply)
#   subprocess.call(['say', reply])

#   Unmute microphone 
#   os.system('osascript -e "set volume input muted false"')
#   os.system("sleep 1")

def chat():

  while True:
    
    user_input = input("You: ")
#   store user_input as a vector with date time and relevant context

    if user_input  == "exit":
        sys.exit()

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

    url = f"https://{api_endpoint}/v1/projects/{project_id}/locations/us-central1/publishers/google/models/chat-bison:predict"
#    print(url)
    
    headers = {
       "Authorization": f"Bearer {access_token}",  
       "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=request_json, headers=headers)
#    print(response.json())
    if response.status_code == 400:
        print(response.text) # print error response
    
    if response.status_code != 200:
      print(f"Error: {response.status_code}")
      continue

#    print(f"Bot: {response.json()['predictions'][0]['content']}")

    reply = response.json().get('predictions',[{}])[0].get('candidates',[{}])[0].get('content')
#   store reply as a vector

    sayItPrintIt(reply)

def outer():
    chat()
      
if __name__ == "__main__":
    outer()

