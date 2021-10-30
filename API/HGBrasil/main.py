import requests
import sqlite3

conn = sqlite3.connect('c:\\sqlite\\aula.db')
cursor = conn.cursor()

url = "https://api.hgbrasil.com/finance?format=json-cors&key=dc36b041"

r = requests.get(url)
data = '25/09/2021'

if r.status_code == 200:
    json = r.json()
    dolar = json['results']['currencies']['USD']['buy']
    euro = json['results']['currencies']['EUR']['buy']
    cursor.execute("""INSERT INTO cotacao (data, euro, dolar) values(?, ?, ?)""",
        (data, euro, dolar))
    print(json['results']['currencies']['USD']['buy'])
    print(json['results']['currencies']['EUR']['buy'])
    conn.commit()
else:
    print('Falhou')

conn.close()
