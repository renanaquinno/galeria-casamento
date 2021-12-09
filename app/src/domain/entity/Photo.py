from app import app, db

class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer,autoincrement=True, primary_key="True")
    src = db.Column(db.String(256))
    photo = db.Column(db.String(256), unique=True)
    user = db.Column(db.Integer)
    approved = db.Column(db.Integer)