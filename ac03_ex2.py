import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE exercicio2
        (id integer primary key,
        nome text not null,
        email text)''')

c.execute("INSERT INTO exercicio2 VALUES (1, 'Tiago Prado', 'tiago.prado@aluno.faculdadeimpacta.com.br')")

c.execute("INSERT INTO exercicio2 VALUES (2, 'Bruno dos Santos', null)")


for row in c.execute('SELECT * FROM exercicio2'):
    print(row)