from application import app
from application.forms import GameDetailsForm, GamesForm
from application.models import Games, GameDetails
from flask import render_template, redirect


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Add', methods=['GET', 'POST'])
def Add():
    form = GamesForm()
    form2 = GameDetailsForm()
    if request.methods == 'POST':
        game = Game(
            title = form.title.data,
            platform = form.platform.data,
            rating = form.rating.data,
            status = form.status.data
        )
        gamedetail = Gamedetail(
            publisher = form2.publisher.data,
            genre = form2.genre.data,
            units = form2.units.data,
            esrb_rating = form2.esrb_rating.data,
            engine = form2.engine.data
        )        
        db.session.add(game)
        db.session.add(gamedetail)
        db.session.commit()
        return redirect(url_for('Read'), form=form2, form2=form2)
    else:
        return render_template('AddGame.html', form=form, form2=form2)

@app.route('/Read', methods=['GET'])
def Read():
    gameslist = Games.query.all()
    extradetails = GameDetails.query.all()
    return render_template('ReadGame.html')

@app.route('/Update', methods=['GET', 'POST'])
def Update():
    form = GamesForm()
    if request.methods == 'POST':
        return redirect(url_for('Read'), form=form)
    else: 
        return render_template('UpdateGame.html', form=form)

@app.route('/Delete/<game_title>', methods=['GET', 'POST'])
def Delete(game_title):
    form = GamesForm()
    if request.methods == 'POST':
        game_to_delete = Games.query.filter_by(Title = game_title).first()
        db.session.delete(game_to_delete)
        db.session.commit()
        return render_template('DeleteGame.html', form=form)
    else :
        return render_template('DeleteGame.html', form=form)
()