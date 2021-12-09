from app import app, db

class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,autoincrement=True, primary_key="True")
    text = db.Column(db.String(256))
    user = db.Column(db.Integer)
    photo = db.Column(db.Integer)

    def __init__(self, text, user, photo):
        self.text = text
        self.user = user
        self.photo = photo