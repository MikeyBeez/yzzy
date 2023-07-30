# main.py

from contextlib import contextmanager
from api import call_api
import db_api 

def main():

  db = db_api.DBConnection()
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
