from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(30), nullable = False)
    Last_name = db.Column(db.String(50), nullable = False)
    User_name = db.Column(db.String(30), nullable = False)
    Password = db.Column(db.String(30), nullable = False)
    Email = db.Column(db.String(50), nullable = False)
    games = db.relationship('Games', backref='users')

class GameDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Publisher = db.Column(db.String(30), nullable = True)
    Genre = db.Column(db.String(30), nullable = True)
    Units_sold = db.Column(db.Integer, nullable = True)
    ESRB_Rating = db.Column(db.String(30), nullable = True)
    Engine = db.Column(db.String(30), nullable = True)
    games = db.relationship('Games', backref='gamedetails')

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    GameDetails_id = db.Column(db.Integer, db.ForeignKey('game_details.id'), nullable=False)
    Title = db.Column(db.String(30), nullable = False)
    Platform = db.Column(db.String(30), nullable = True)
    Rating = db.Column(db.Integer, nullable = True)
    Status = db.Column(db.String(30), nullable = False)