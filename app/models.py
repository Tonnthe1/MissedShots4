from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    linkedin = db.Column(db.String(150), nullable=True)
    facebook = db.Column(db.String(150), nullable=True)
    twitter = db.Column(db.String(150), nullable=True)
    github = db.Column(db.String(150), nullable=True)
    phone_visible = db.Column(db.Boolean, default=True)
    linkedin_visible = db.Column(db.Boolean, default=True)
    facebook_visible = db.Column(db.Boolean, default=True)
    twitter_visible = db.Column(db.Boolean, default=True)
    github_visible = db.Column(db.Boolean, default=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    online = db.Column(db.Boolean, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('events', lazy=True))
