from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class User(FlaskForm):
    nome_pessoa = StringField("nome_pessoa", validators=[DataRequired()])
    cpf_pessoa = IntegerField("cpf_pessoa", validators=[DataRequired()])
    endereco = StringField("endereco", validators=[DataRequired()])
    numero = IntegerField("numero", validators=[DataRequired()])
    bairro = StringField("bairro", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    celular = IntegerField("celular", validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])

class Login(FlaskForm):
    cpf_login = IntegerField("cpf_login", validators=[DataRequired()])
    senha_login = PasswordField("senha_login", validators=[DataRequired()])

class Item(FlaskForm):
    cesta_basica = BooleanField("cesta_basica", validators=[DataRequired()])
    higiene = BooleanField("higiene", validators=[DataRequired()])
    gas_cozinha = BooleanField("gas_cozinha", validators=[DataRequired()])

class Especializacao(FlaskForm):
    tipo = IntegerField("tipo", validators=[DataRequired()])

#class Pedido(FlaskForm):
 #
  #  id_lista = IntegerField("id_lista")
   # id_recebedor = IntegerField("id_recebedor")
    #id_doador = IntegerField("id_doador")
#    id_fornecedor = IntegerField("id_fornecedor")
 #   id_entregador = IntegerField("id_entrega")
  #  selo_dc = BooleanField("selo", validators=[DataRequired()])
  #quant_adulto