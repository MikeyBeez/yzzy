# dbconf.py
import psycopg2

MY_DB_CONFIG = {
  'host': 'localhost',
  'database': 'bard',
  'user': 'postgres',
  'password': '',
  'conn': 'None',
  'user_id': 'Mikey'
}

connection_string = "dbname='{}' user='{}' host='{}' password='{}'".format(
  MY_DB_CONFIG['database'], MY_DB_CONFIG['user'], MY_DB_CONFIG['host'], MY_DB_CONFIG['password'])

connection = psycopg2.connect(connection_string)
