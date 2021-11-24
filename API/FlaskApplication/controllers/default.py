from flask import render_template
from FlaskApplication import app
from FlaskApplication.models.forms import CadastroForm, AlterarForm, ExcluirForm
import sqlite3
from sqlite3 import Error


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()

    if form.validate_on_submit():
        descricao = form.descricao.data
        precocompra = form.precocompra.data
        precovenda = form.precovenda.data
        datacriacao = form.datacriacao.data
        if descricao and precocompra and precovenda and datacriacao:
            registro = (descricao, precocompra, precovenda, datacriacao)
            print(registro)
            try:
                conn = sqlite3.connect('database\produtos.db')
                sql = ''' INSERT INTO produtos(descricao, precocompra,
                                precovenda, datacriacao)
                                VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
            except Error as e:
                print(e)
            finally:
                conn.close()
        return render_template('cadastrar.html', form=form)
    return render_template('cadastrar.html', form=form)


@app.route("/alterar", methods=['GET', 'POST'])
def alterar():
    form = AlterarForm()
    if form.validate_on_submit():
        idproduto = form.idproduto.data
        descricao = form.descricao.data
        precocompra = form.precocompra.data
        precovenda = form.precovenda.data
        datacriacao = form.datacriacao.data
        if idproduto and descricao and precocompra and precovenda and datacriacao:
            id = idproduto
            registro = (descricao, precocompra, precovenda, datacriacao)
            print(f"{registro}, {id}")
            try:
                conn = sqlite3.connect('database\produtos.db')
                sql = ''' UPDATE produtos SET descricao = ?, precocompra = ?,precovenda = ?, datacriacao = ? WHERE idproduto = ''' + str(
                    id)
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
            except Error as e:
                print(e)
            finally:
                conn.close()
        return render_template('alterar.html', form=form)
    return render_template('alterar.html', form=form)


@app.route("/excluir", methods=['GET', 'POST'])
def excluir():
    form = ExcluirForm()

    if form.validate_on_submit():
        idproduto = form.idproduto.data
        registro = idproduto
        print(registro)
        print(idproduto)
        try:
            conn = sqlite3.connect('database\produtos.db')
            sql = '''DELETE FROM produtos WHERE idproduto = ''' + str(registro)

            cur = conn.cursor()
            cur.execute(sql)

            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()
    return render_template('excluir.html', form=form)


@app.route('/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect('database\produtos.db')
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        return '{}'.format(registros)
    except Error as e:
        print(e)
    finally:
        conn.close()
