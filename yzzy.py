# main.py

from modules.ap import call_api
from modules.db import db 

def main():

  db = db.DBConnection()
  conn = db.connect()

  with db:
  
    while True:
    
      user_input = input("You: ")
      if user_input == "exit":
        break

      # response = api.call_api(user_input)
      
      # db.insert("conversations", ["question", "answer"], [user_input, response])

  db.close()

if __name__ == "__main__":
  
  main()
