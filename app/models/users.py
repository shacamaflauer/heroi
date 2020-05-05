from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from wtforms.form import BaseForm

class User(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
