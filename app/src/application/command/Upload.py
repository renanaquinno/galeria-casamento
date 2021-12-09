from flask import Flask, request, redirect, url_for, flash
from app import app, db, UPLOAD_FOLDER,ALLOWED_EXTENSIONS
from jinja2 import Environment
from werkzeug.utils import secure_filename
from app.src.domain.entity.Photo import Photo
from app.src.domain.entity.User import User
import os

def Upload():
    user = request.form['userId']
    file = request.files['photo']
    photo = request.files['photo']

    filename = 'upload/' + secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    
    if photo and allowed_file(photo.filename):
        file.save(filepath)
        userAdmin = User.query.filter_by(id=user).first()
        if userAdmin.isadmin == 1:
            photo = Photo(src = filename, photo = filepath, user = user, approved = 1)
            db.session.add(photo)
            db.session.commit()
            flash("Foto compartilhada com sucesso!")   
        else:
            photo = Photo(src = filename, photo = filepath, user = user, approved = 0)
            db.session.add(photo)
            db.session.commit()
            flash("Foto compartilhada com sucesso, aguardando a aprovação dos noivos!")   
        return redirect(url_for('Home'))
    else:
        flash('Somente imagens com extensão png, jpg ou jpeg')
        return redirect(url_for('Home'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS