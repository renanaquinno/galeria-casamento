from app.src.domain.entity.Photo import Photo
from app import app, db
from flask import Flask, request, redirect, url_for, flash

def Show():
    if request.method == 'POST':
        photoId =  request.form['photoId'] 
        photo = Photo.query.filter_by(id=photoId).first()
        print(photo.approved)
        if photo.approved == 0:
            photo.approved = 1
            db.session.commit()
            flash("Foto aprovada com sucesso")   
        else:    
            photo.approved = 0
            db.session.commit()
            flash("Foto ocultada com sucesso")   
    return redirect(url_for('Home')) 