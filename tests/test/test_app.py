from flask_testing import TestCase
from application import app, db
from application.models import GameDetails, Games, Users
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI ='sqlite:///',
            DEBUG=True,
            SECRET_KEY ='SUPER_SECRET_KEY',
            WTF_CSRF_ENABLED=False
        )
        return app
    
    def setUp(self):
        db.create_all()
        user = Users(First_name='Lawrence', Last_name='Ford', User_name='Anonymouse', Password='SpikeL3372', Email='Lawrence@hotmail.co.uk')
        game = Games(Users_id=int(1), GameDetails_id=int(1), Title='Halo', Platform='Xbox', Rating='9', Status='completed')
        game_details = GameDetails(Publisher='Bungie', Genre='FPS', Units_sold=int(4000), ESRB_Rating='mature 17+', Engine='Blam engine')
        user2 = Users(First_name='Terrence', Last_name = 'Crawford', User_name='BasementCrawler', Password='password123', Email='terrycraw@gmail.com')
        game2 = Games(Users_id=2, GameDetails_id=2, Title='Zombie Party', Platform='Wii', Rating='4' , Status='plan to play')
        game_details2 = GameDetails(Publisher= 'Nintendo', Genre='party game', Units_sold=int(500), ESRB_Rating='e (everyone)', Engine='Unreal')
        db.session.add(user)
        db.session.add(user2)
        db.session.add(game)
        db.session.add(game2)
        db.session.add(game_details)
        db.session.add(game_details2)        
    
    def tearDown(self):
        db.drop_all()

class TestView(TestBase):
    
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_get(self):
        response = self.client.get(url_for('AddUser'))
        self.assertEqual(response.status_code, 200)

    def test_gamedetails_get(self):
        response = self.client.get(url_for('AddDetails'))
        self.assertEqual(response.status_code, 200)

    def test_game_get(self):
        response = self.client.get(url_for('Add'))
        self.assertEqual(response.status_code, 200)
    
    def test_read_get(self):
        response = self.client.get(url_for('Read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Halo', response.data)
        self.assertIn(b'Zombie Party', response.data)

    def test_update_get(self):
        response = self.client.get(url_for('Update', Title = 'Halo' ))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_add_user(self):
        response = self.client.post(
            url_for('AddUser'),
            data = dict(first_name='Darnell',
            last_name='Cambell',
            user_name='BallisLife',
            password='Pa$$W0rD',
            email='DarnellCambell@gmail.com')
        )
        self.assertEqual(response.status_code, 200)
        assert Users.query.filter_by(First_name= 'Darnell').first().id == 3
        assert len(Users.query.all()) == 3

    def test_add_game_details(self):
        response = self.client.post(
            url_for('AddDetails'),
            data = dict( publisher='Square Enix',
            genre='rpg',
            units_sold= int(500),
            esrb_rating= 'e (everyone)',
            engine= 'Frostbite')
        )
        assert GameDetails.query.filter_by(Publisher= 'Square Enix').first().id == 3
        assert len(GameDetails.query.all()) == 3
        
    def test_add_game(self):
        response = self.client.post(
            url_for('Add'),
            data = dict(user_id= int(3),
            gamedetails_id= int(3),
            title = 'Banjo Kazooie',
            platform = 'Xbox 360',
            rating= int(6),
            status = 'plan to play')
         )
        assert Games.query.filter_by(Title= 'Banjo Kazooie').first().id == 3
        assert len(Games.query.all()) == 3

    def test_update_game(self):
        response = self.client.post(
            url_for('Update', Title = 'Halo'),
            data = dict(title = 'Gears of War',
            platform = 'Xbox 360', 
            rating = int(10),
            status ='playing',
            follow_redirect = True)
        )
        assert Games.query.filter_by(Title= 'Gears of War').first().id == 1

    def test_delete_game(self):
        response = self.client.post(
            url_for('Delete', Title= 'Halo')
        )
        assert len(Games.query.all()) == 1