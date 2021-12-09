from flask import Flask, request, render_template, redirect, url_for, flash, Response
from app import app, db
from app.src.domain.entity.Like import Like

def LikePhoto():
    if request.method == 'POST':
        user = request.form['userId']
        photo =  request.form['photoId'] 
        likeuser = Like.query.filter_by(user=user, photo=photo).all()
        like = Like(user, photo)
        if len(likeuser) > 0:
            Like.query.filter_by(user=user, photo=photo).delete()
            db.session.commit()
        else:    
            db.session.add(like)
            db.session.commit()
    return redirect(url_for('Home')) 

