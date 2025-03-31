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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://tiffsdb_user:m6bgJHymMgWBsEaFCzNWnwwCtd935qMS@dpg-cvlcrrq4d50c73e5akl0-a/tiffsdb")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "The Basketball table was successful created!"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://tiffsdb_user:m6bgJHymMgWBsEaFCzNWnwwCtd935qMS@dpg-cvlcrrq4d50c73e5akl0-a/tiffsdb")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Tiffany', 'LaRue', 'CU Boulder', 'Burndown for What?', 3308);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table populated!"

@app.route('/db_select')
def select_all():
    conn = psycopg2.connect("postgresql://tiffsdb_user:m6bgJHymMgWBsEaFCzNWnwwCtd935qMS@dpg-cvlcrrq4d50c73e5akl0-a/tiffsdb")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    conn.close()
    response_string = ''
    response_string+='<table>'
    for player in records:
        response_string+='<tr>'
        for info in player:
            response_string+='<td>{}</td>'.format(info)
        response_string+='</tr>'
    response_string+='</table>'
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://tiffsdb_user:m6bgJHymMgWBsEaFCzNWnwwCtd935qMS@dpg-cvlcrrq4d50c73e5akl0-a/tiffsdb")
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    conn.close()
    return "Basketball table dropped!"