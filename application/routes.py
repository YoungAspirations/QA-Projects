from application import app, db
from application.forms import GameDetailsForm, GamesForm, UsersForm, UpdateForm
from application.models import Games, GameDetails, Users
from flask import render_template, redirect, request,url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Add', methods=['GET', 'POST'])
def Add():
    form = GamesForm()
    if request.method == 'POST':
        game = Games(
            Title = form.title.data,
            Platform = form.platform.data,
            Rating = form.rating.data,
            Status = form.status.data,
            GameDetails_id = form.gamedetails_id.data,
            Users_id = form.user_id.data
        )
        db.session.add(game)
        db.session.commit()
        return render_template('AddGame.html', form=form)
    else:
        return render_template('AddGame.html', form=form)

@app.route('/AddDetails', methods=['GET', 'POST'])
def AddDetails():
    form = GameDetailsForm()
    if request.method == 'POST':
        gamedetail = GameDetails(
            Publisher = form.publisher.data,
            Genre = form.genre.data,
            Units_sold = form.units.data,
            ESRB_Rating = form.esrb_rating.data,
            Engine = form.engine.data
        )
        db.session.add(gamedetail)
        db.session.commit()
        return redirect(url_for('Read'))
    else:
        return render_template('GameDetails.html', form=form,)

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUser():
    form = UsersForm()
    if request.method == 'POST':
        user = Users(
            First_name = form.first_name.data,
            Last_name = form.last_name.data,
            User_name = form.user_name.data,
            Password = form.password.data,
            Email = form.email.data
        )
        db.session.add(user)
        db.session.commit()
        return render_template('User.html', form=form,)
    else:
        return render_template('User.html', form=form,)

@app.route('/Read', methods=['GET'])
def Read():
    gameslist = Games.query.all()
    extradetails = GameDetails.query.all()
    return render_template('ReadGame.html', gameslist = gameslist,  extradetails = extradetails)

@app.route('/Update/<Title>', methods=['GET', 'POST'])
def Update(Title):
    form = UpdateForm()
    game = Games.query.filter_by(Title = Title).first()
    if request.method == 'GET': 
        form.title.data = game.Title
        form.platform.data = game.Platform
        form.rating.data = game.Rating
        form.status.data = game.Status
        return render_template('UpdateGame.html', form=form)
    else:
        if request.method == 'POST':
            game.Title = form.title.data
            game.Platform = form.platform.data 
            game.Rating = form.rating.data 
            game.Status = form.status.data
            db.session.commit()    
            return redirect(url_for('Read'))
    

@app.route('/Delete/<Title>', methods=['GET', 'POST'])
def Delete(Title):
    game_to_delete = Games.query.filter_by(Title=Title).first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return redirect(url_for('Read'))

