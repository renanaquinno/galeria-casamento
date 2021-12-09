from flask import Flask, request, render_template, redirect, url_for, flash, Response
from flask_login import login_user, login_required, logout_user, current_user
from app.src.domain.entity.User import User

@login_required
def Logout():
    logout_user()
    flash("Usuario Deslogado")     
    return redirect(url_for('Login'))