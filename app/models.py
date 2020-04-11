from . import db
from datetime import date

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    bio = db.Column(db.String(1000))
    photo = db.Column(db.String(100))
    date = db.Column(db.String(10))
    

    def __init__(self,first_name,last_name,email,location,gender,bio,photo):
        self.first_name = first_name
        self.last_name=last_name
        self.email=email
        self.location=location
        self.gender = gender
        self.bio = bio
        self.photo = photo
        self.date = str(date.today())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
