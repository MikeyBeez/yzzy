import psycopg2
from contextlib import contextmanager
from dbconf import connection_string

class DBConnection:

  def __init__(self):
    self.connection = None

  def connect(self):
    self.connection = psycopg2.connect(connection_string)
    return self.connection

  @contextmanager
  def __enter__(self):
    self.connection = self.connect()
    return self

import psycopg2
from contextlib import contextmanager
from dbconf import connection_string

class DBConnection:

  def __init__(self):
    self.connection = self.connect()

  def connect(self):
    self.connection = psycopg2.connect(connection_string)
    return self.connection

  @contextmanager
  def __enter__(self):
    return self

  def __exit__(self):
    self.connection.close()

  def query(self, sql, params=None):
    with self.connection.cursor() as cursor:
      cursor.execute(sql, params)
      return cursor.fetchall()

  def close(self):
    """Close the database connection."""

    if self.connection is not None:
      
      try:
        self.connection.close()
        print("Database connection closed.")

      except Exception as e:
        print(f"Error closing database connection: {e}")

      finally:
        self.connection = None


  def insert(self, table, columns, values):
    placeholders = ", ".join(["%s"] * len(values))
    cols = ", ".join(columns)
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"

    with self.connection.cursor() as cursor:
      cursor.execute(sql, values)
      self.connection.commit()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.connection.close()

  @contextmanager
  def db_connection() -> DBConnection:
    conn = DBConnection()
    try:
      yield conn
    finally:
      # conn.close()
      pass

with DBConnection() as db:
  sql = "SELECT * FROM users WHERE id = %s"
  result = db.query(sql, [1])

  db.insert("logs", ["msg", "level"], ["App started", "INFO"]) 


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

    # Also call the `close()` method explicitly.
    self.close()
    

# Example usage

with DBConnection() as db:
  sql = "SELECT * FROM users WHERE id = %s"
  result = db.query(sql, [123])

  db.insert("logs", ["msg", "level"], ["App started", "INFO"]) 

