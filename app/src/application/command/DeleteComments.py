from flask import Flask, redirect, url_for, flash
from app import app, db
from app.src.domain.entity.Comment import Comment

def DeleteComments(id):
    Comment.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Comentario apagado com sucesso!")   
    return redirect(url_for('Home')) 