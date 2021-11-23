import mysql.connector
from flask import render_template
from apiPrecoPlacas import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'developer'
app.config['MYSQL_PASSWORD'] = 'chessus123'
app.config['MYSQL_DB'] = 'api_placas'


@app.route("/")
@app.route("/index")
def index():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('index.html', results=results)


@app.route("/adm")
def adm():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('adm.html', results=results)


@app.route("/amd")
def amd():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('amd.html', results=results)


@app.route("/nvidia")
def nvidia():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('nvidia.html', results=results)


@app.route("/todas")
def todas():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('todas.html', results=results)


@app.route("/teste")
def teste():
    cur = mysql.connection.cursor()
    sql = "select * from placa"
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('teste.html', results=results)



















'''
json = {"Placas": "default", "valid_key": True, "results": [
        {"Nome": "Nvidia RTX 2060", "valid_key": True, "results": [
            {"Preco": 4299.9},
            {"Data": '2021-09-01'},
        ]
         },
        {"Nome": "AMD Radeon RX 6700XT", "valid_key": True, "results": [
            {"Preco": 6499.99},
            {"Data": '2021-09-01'},
        ]
         },
    ]
            }
'''