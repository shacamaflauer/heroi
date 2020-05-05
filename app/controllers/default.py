from flask import render_template, redirect, url_for
from app import app, db
from app.models.form import User, Login
from app.models.tables import Pessoa
from flask_login import login_user, logout_user



@app.route("/")
@app.route("/index")
def index():
    return render_template('index1.html')


@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    form = User()
    if form.validate_on_submit():
        i = Pessoa(form.nome_pessoa.data,
                 form.cpf_pessoa.data,
                 form.endereco.data,
                 form.numero.data,
                 form.bairro.data,
                 form.cidade.data,
                 form.celular.data,
                 form.senha.data)
        print('Cadastrado')
        db.session.add(i)
        db.session.commit()
    else:
        print()
    return render_template('formulario.html', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = Login()
    user = form.cpf_login
    if form.validate_on_submit():
        print(form.cpf_login.data)
        print(form.senha_login.data)
        u = Pessoa.query.filter_by(cpf_pessoa=form.cpf_login.data).first()
        if u and u.verify_password(form.senha_login.data) == True:

            print("Logo")
            login_user(u)
            return redirect(url_for('especializacao'))
        else:
            print("nao Logo")
            #return redirect(url_for('index'))
    return render_template('login.html', form=form, user=user)

@app.route("/especializacao")
def especializacao():
    return render_template('especializacao.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('logout'))


@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/entrada")
def entrada():
    return render_template('entrada.html')
