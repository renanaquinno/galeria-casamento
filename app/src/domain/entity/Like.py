from app import app, db

class Like(db.Model):
    __tablename__ = 'like'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,autoincrement=True, primary_key="True")
    user = db.Column(db.Integer)
    photo = db.Column(db.Integer)

    def __init__(self, user, photo):
        self.user = user
        self.photo = photo
