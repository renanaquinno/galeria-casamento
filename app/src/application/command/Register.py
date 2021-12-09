from flask import Flask, request, render_template, redirect, url_for, flash
from app import app, db
from app.src.domain.entity.User import User

def Register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password =  request.form['password']
        isadmin = 0
        usernameused = User.query.filter_by(username=username).first()
        if usernameused:
            flash("Usuario já esta sendo usado!")
        else:    
            if len(password) < 4 or len(name) == 0 or len(username) == 0:
                flash("Senha precisa ter no minimo 4 caracteres, nome e usuario não podem ser vazios !")
            else:
                user = User(name, username, password, isadmin)
                db.session.add(user)
                db.session.commit()
                flash("Usuario cadastrado com sucesso, agora você pode fazer o login!")     
                return redirect(url_for('Login'))
    return render_template("register.html")