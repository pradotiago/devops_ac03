import sqlite3

conn = sqlite3.connect('ac03.db')
c = conn.cursor()

c.execute('''CREATE TABLE exercicio
        (id integer primary key,
        nome text not null,
        email text)''')