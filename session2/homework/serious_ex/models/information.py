from mongoengine import Document, StringField, IntField, BooleanField

class Game(Document):
    game_name = StringField()
    game_info = StringField()
    num_account = IntField()

class Service(Document):
    name = StringField()
    occupied = BooleanField()
    fav_lane = StringField() # top, mid , bot, jung
    credit = IntField() # 1-5
