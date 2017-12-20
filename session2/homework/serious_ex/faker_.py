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
    game_name="PlayerUnknown's Battlegrounds",
    game_info="Survival",
    num_account= randint(0,50)
)
game2 = Game(
    game_name="Leauge of Legends",
    game_info='Multiplayer Online Battle Arena',
    num_account= randint(0,50)
)
game3 = Game(
    game_name="Warface",
    game_info="First Player Shooting",
    num_account= randint(0,50)
)
game1.save()
game2.save()
game3.save()
