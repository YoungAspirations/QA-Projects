from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class UsersForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=2,max=30)])
    last_name = StringField('Last name', validators=[DataRequired(),Length(min=2,max=30)])
    user_name = StringField('User name', validators=[DataRequired(), Length(min=5,max=30)])
    password = StringField('Password', validators=[DataRequired(), Length(min=8,max=30)])
    email = StringField('Email name', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Add Credentials')

class GameDetailsForm(FlaskForm):
    publisher = StringField('First name', validators=[Length(min=2,max=30)])
    genre = SelectField('Genre', categories = 
            [("action", "Action"), 
            ("adventure", "Adventure"),
            ("rpg","RPG"),
            ("mmo","MMO"),
            ("fps","FPS"),
            ("open world","Open World"),
            ("arena brawler","Arena Brawler")
    ])
    units = IntegerField("Units sold")
    esrb_rating = SelectField('Video game age rating', esrb =
            [("e (everyone)","E (Everyone)"),
            ("e10+ (everyone 10+)","E10+ (Everyone 10+)"),
            ("teen","Teen"),
            ("mature 17+","Mature 17+"),
            ("adult 18+","Adult 18+"),
            ("rp (rating pending)","RP (Rating Pending)"),
            ("rp 17+ (rating pending likely 17+)","RP 17+ (Rating Pending likely 17+)")
    ])
    engine = StringField('Development engine', validators=[Length(max=30)])  
    submit = SubmitField('Add Game Details')

class GamesForm(FlaskForm):
    title = StringField('Game Title', validators=[DataRequired(), Length(max=30)])
    platform = StringField('Platform', validators=[Length(max=30)])
    rating = SelectField('Your score', score = 
            [("1","1"),
            ("2","2"),
            ("3","3"),
            ("4","4"),
            ("5","5"),
            ("6","6"),
            ("7","7"),
            ("8","8"),
            ("9","9"),
            ("10","10")
    ]) 
    status = SelectField("status of the game", status_of_game = 
            [("plan to play","Plan to play"),
            ("playing","Playing"),
            ("on hold","On Hold"),
            ("completed","Completed"),
            ("dropped","Dropped")
    ])
    submit = SubmitField('Add Game')