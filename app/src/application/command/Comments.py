from flask import Flask, request, redirect, url_for, flash
from app import app, db
from app.src.domain.entity.Comment import Comment

def Comments():
    if request.method == 'POST':
        text = request.form['comment']
        user = request.form['userId']
        photo =  request.form['photoId']        
        if len(text) == 0:
            flash("Comentario não pode ser vazio")
        else: 
            comment = Comment(text, user, photo)
            db.session.add(comment)
            db.session.commit()
            flash("Comentario adicionado com sucesso!")  
        return redirect(url_for('Home'))

 
        