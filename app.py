from flask import Flask, redirect, url_for, flash
from app import app, db

from app.src.domain.entity.Comment import Comment

from app.src.application.command.Home import Home
from app.src.application.command.LikePhoto import LikePhoto
from app.src.application.command.Comments import Comments
from app.src.application.command.DeleteComments import DeleteComments
from app.src.application.command.Register import Register
from app.src.application.command.Login import Login
from app.src.application.command.Logout import Logout
from app.src.application.command.Upload import Upload
from app.src.application.command.Show import Show
from app.src.application.command.Error import Error
from jinja2 import Environment

app.add_url_rule("/", methods=['POST','GET'],view_func=Home)

app.add_url_rule("/home", methods=['POST','GET'],view_func=Home)

app.add_url_rule("/register", methods=['POST','GET'],view_func=Register)

app.add_url_rule("/login", methods=['POST','GET'],view_func=Login)

app.add_url_rule("/logout", methods=['GET','POST'],view_func=Logout)

app.add_url_rule("/like", methods=['POST'],view_func=LikePhoto)

app.add_url_rule("/upload", methods=['POST'],view_func=Upload)

app.add_url_rule("/show", methods=['POST'],view_func=Show)

app.add_url_rule("/comment", methods=['POST'],view_func=Comments)

app.add_url_rule("/<string:nome>", methods=['GET'],view_func=Error)

#app.add_url_rule("/deleteComment/<id>",view_func=DeleteComments(id))

@app.route('/deleteComment/<id>')
def deleteComment(id):
    Comment.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Comentario apagado com sucesso!")   
    return redirect(url_for('Home')) 



def environment(**options):
    env = Environment(**options, extensions=['jinja2.ext.loopcontrols'])
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    return env

if __name__ == '__main__':
    app.run()