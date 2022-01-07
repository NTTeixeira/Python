from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CadastroForm(FlaskForm):
    descricao = StringField("descricao", validators=[DataRequired()])
    precocompra = StringField("precocompra", validators=[DataRequired()])
    precovenda = StringField("precovenda", validators=[DataRequired()])
    datacriacao = StringField("datacriacao", validators=[DataRequired()])


class AlterarForm(FlaskForm):
    idproduto = StringField("idproduto", validators=[DataRequired()])
    descricao = StringField("descricao", validators=[DataRequired()])
    precocompra = StringField("precocompra", validators=[DataRequired()])
    precovenda = StringField("precovenda", validators=[DataRequired()])
    datacriacao = StringField("datacriacao", validators=[DataRequired()])


class ExcluirForm(FlaskForm):
    idproduto = StringField("idproduto", validators=[DataRequired()])
