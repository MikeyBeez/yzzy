import psycopg2
from dbconf import connection_string

class DBConnection:

  def __init__(self):
    self.connection = None

  def connect(self):
    self.connection = psycopg2.connect(connection_string)
    return self.connection

  @con
  @contextmanager
  def __enter__(self):
    self.connection = self.connect()
    try:
      yield self
    finally:
      self.close()

  def query(self, sql, params=None):
    with self.connection.cursor() as cursor:
      cursor.execute(sql, params)
      return cursor.fetchall()

  def insert(self, table, columns, values):
    placeholders = ", ".join(["%s"] * len(values))
    cols = ", ".join(columns)
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    
    with self.connection.cursor() as cursor:
      cursor.execute(sql, values)
      self.connection.commit()

  def close(self):
    self.connection.close()

# Example usage

with DBConnection() as db:

  sql = "SELECT * FROM users WHERE id = %s"
  result = db.query(sql, [123])

  db.insert("logs", ["msg", "level"], ["App started", "INFO"]) 

