from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import urllib.request
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

UPLOAD_FOLDER = 'app/static/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

###app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'db_casamento.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\renan\\Desktop\\defensoria\\app\\src\\infrastructure\\persistence\\sqlite\\db_casamento.sqlite'

app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')