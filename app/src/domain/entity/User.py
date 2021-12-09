from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True, primary_key="True")
    name = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    isadmin = db.Column(db.Integer)

    @property
    def is_active(self):
        return True
    
    def __init__(self, name, username, password,isadmin):
        self.name = name
        self.username = username
        self.password = generate_password_hash(password)
        self.isadmin = 0

    def verify_password(self, password):
        return check_password_hash(self.password, password)