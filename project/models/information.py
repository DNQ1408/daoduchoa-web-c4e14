from mongoengine import Document, StringField, IntField, BooleanField

class Game(Document):
    name = StringField()
    info = StringField()
    num_account = IntField()
    rating = IntField() #1-5

class Service(Document):
    name = StringField()
    occupied = BooleanField()
    fav_lane = StringField() # top, mid , bot, jung
    credit = IntField() # 1-5
