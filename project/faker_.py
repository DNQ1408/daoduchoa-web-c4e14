from mlab import mlab_connect
from models.information import Service, Game
from faker import Faker
from random import choice, randint

mlab_connect()


service = Service(
    name=Faker().name(),
    occupied=choice([True,False]),
    fav_lane=choice(['top','mid','bot','jung']),
    credit=randint(1,5)
)
service.save()

game1 = Game(
    name="PlayerUnknown's Battlegrounds",
    info="Survival",
    num_account= randint(0,50),
    rating = randint(1,5)
)
game2 = Game(
    name="Leauge of Legends",
    info='Multiplayer Online Battle Arena',
    num_account= randint(0,50),
    rating = randint(1,5)
)
game3 = Game(
    name="Warface",
    info="First Player Shooting",
    num_account= randint(0,50),
    rating = randint(1,5)
)
game1.save()
game2.save()
game3.save()
