from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy.dialects.sqlite import BLOB


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    bio = db.Column(db.String(128))
    spol = db.Column(db.String(10))
    user_picture = db.Column(db.String(120))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Trip(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String(120),index=True)
    about = db.Column(db.String(1000),index=True)
    date = db.Column(db.DateTime,index=True)
    min_people = db.Column(db.String(120),index=True)
    max_people = db.Column(db.String(120),index=True)
    total_cost = db.Column(db.Integer,index=True)
    transport = db.Column(db.String(120),index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    trip_rating = db.Column(db.Integer, default = '0')
    trip_picture = db.Column(db.String(120))


class User_rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer,db.ForeignKey('trip.id'))
    coments = db.Column(db.String(500), index=True)

class JoinTrip(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	trip_id = db.Column(db.Integer,db.ForeignKey('trip.id'))