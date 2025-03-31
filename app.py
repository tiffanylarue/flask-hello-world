import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Tiffany LaRue in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://tiffsdb_user:m6bgJHymMgWBsEaFCzNWnwwCtd935qMS@dpg-cvlcrrq4d50c73e5akl0-a/tiffsdb")
    conn.close()
    return "Database connection successful!"