import db_api 

def main():
  db = db_api.DBConnection()

  print(db_api.connection_string)

if __name__ == "__main__":
  main()
