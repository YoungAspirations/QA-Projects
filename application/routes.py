from application import app
from application.forms import GameDetailsForm, GamesForm
from flask import render_template


@app.route('/')

def home():
    return render_template('home.html')

@app.route('/Add', methods=['GET', 'POST'])
def GameAdd():
    form = GamesForm()
    form2 =GameDetailsForm()
    if request.methods == 'POST':
    
    else:
        return render_template('AddGame.html', form=form, form2=form2)

@app.route('/Read', methods=['GET'])
def GameRead():
    form3 = GamesForm()
    form4 = GameDetailsForm()
    return render_template('ReadGame.html', form3=form3, form4=form4)

@app.route('/Update', methods=['GET', 'PUT'])
def GameUpdate():
    form5 = GamesForm()
    
    if request.methods == 'PUT':
        
    else: 
        return render_template('UpdateGame.html', form5=form5)

@app.route('/Delete', methods=['GET', 'DELETE'])
def GameDelete():
    form6 = GamesForm()
    if request.methods == 'DELETE':
    
    else :
        return render_template('DeleteGame.html', form6=form6)
