from Flask import db


class Descricao(db.Model):
    __tablename__ = "produtos"

    idProduto = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, unique=False)
    precoCompra = db.Column(db.Text, unique=False)
    precoVenda = db.Column(db.Text, unique=False)
    dataCriacao = db.Column(db.Text, unique=False)

    def __init__(self, descricao, precoCompra, precoVenda, dataCriacao):
        self.descricao = descricao
        self.precoCompra = precoCompra
        self.precoVenda = precoVenda
        self.dataCriacao = dataCriacao
