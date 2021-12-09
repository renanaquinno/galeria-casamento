
from flask import Flask, render_template,Response
from flask_login import current_user
from app import app
from jinja2 import Environment

from app.src.domain.entity.Photo import Photo
from app.src.domain.entity.User import User
from app.src.domain.entity.Comment import Comment
from app.src.domain.entity.Like import Like

def Home():
    comments = Comment.query.order_by(Comment.id).all()
    photosAll = Photo.query.order_by(Photo.id).all()
    photosApproved = Photo.query.filter_by(approved=1).all()
    user = User.query.order_by(User.id).all()
    likes = Like.query.order_by(Like.id).all()
    if current_user.is_authenticated:
        return render_template("index.html", currentUser = current_user, id=current_user.id, comments = comments, photosAll=photosAll,photosApproved = photosApproved, user = user, likes=likes)
    else:
        return render_template("error.html")