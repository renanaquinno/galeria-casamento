from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import login_user
from app.src.domain.entity.User import User

def Login():
    if request.method == 'POST':
        username = request.form['username']
        password =  request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            flash("Usuario ou senha incorreto(s)")     
        else:
            login_user(user)
            return redirect(url_for('Home'))
    return render_template("login.html")