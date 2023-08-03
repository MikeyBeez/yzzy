import requests
from google.cloud import aiplatform

API_ENDPOINT = "https://us-central1-aiplatform.googleapis.com"  
PROJECT_ID = "modular-bot-392623"
MODEL_ID = "chat-bison"

def call_api(conversation):

  # Bard API code
  
  client_options = {"api_endpoint": API_ENDPOINT}
  client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

  instance = aiplatform.gapic.Instance(content=conversation)
  parameters = {"parameters": {"model": MODEL_ID}}
  response = client.predict([instance], parameters)
  
  reply = response.predictions[0].display_name
  
  return reply

def chatbot(conversation):

  response = call_api(conversation)
  
  return response
  
def get_user_input():

  # get user input
  text = input('\n\nUSER:\n\n')

  # check if scratchpad updated, continue
  
  return text
  
def main():

  conversation = []
  
  while True:
  
    user_input = get_user_input()
    conversation.append({"role": "user", "content": user_input})

    ai_response = chatbot(conversation)
    conversation.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
  main()
