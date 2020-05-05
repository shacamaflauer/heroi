from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Pessoa.query.filter_by(cpf_pessoa=user_id).first()

class Pessoa(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nome_pessoa = db.Column (db.String)
    cpf_pessoa = db.Column(db.String(11), unique=True)
    endereco = db.Column(db.String)
    numero = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    celular = db.Column(db.String)
    senha = db.Column(db.String)


    def __init__(self, nome_pessoa, cpf_pessoa, endereco, numero, bairro, cidade, celular, senha):
        self.nome_pessoa = nome_pessoa
        self.cpf_pessoa = cpf_pessoa
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.celular = celular
        self.senha = generate_password_hash(senha)

    def verify_password(self, pwd):
        return check_password_hash(self.senha, pwd)

    def __repr__(self):
        return '<Nome %r>' % self.nome_pessoa

class Item(db.Model, UserMixin):
    __tablename__ = "itens"

    id = db.Column(db.Integer, primary_key=True)
    cesta_basica = db.Column(db.String)
    higiene = db.Column(db.String)
    gas_cozinha = db.Column(db.String)

    def __init__(self, cesta_basica, higiene, gas_cozinha):
        self.cesta_basica = cesta_basica
        self.higiene = higiene
        self.gas_cozinha = gas_cozinha

item = Item('Cesta Basica', 'Kit Higiene', 'Botijão')
print(item)

'''
class Pedido(db.Model):
    __tablename__ = "pedidos"

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_recebedor = db.Column(db.Integer, foreign_key=None)
    id_doador = db.Column(db.Integer, default=None) 
    id_iten = db.Column(db.Integer), db.ForeignKey('person.id')
    id_fornecedor = db.Column(db.Integer, default=None)
    id_entregador = db.Column(db.Integer, default=None)
    quant_adulto = db.Column(db.Integer, default=1)'''
