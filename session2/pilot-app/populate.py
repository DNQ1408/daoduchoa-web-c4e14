from mlab import mlab_connect
from models.service import Service
from faker import Faker
from random import choice, randint


service_faker = Faker()
# print(service_faker.name())

mlab_connect()
# Service.drop_collection() # Xóa all collection
service = Service(  name=service_faker.name(),
                    yob=randint(1990,2000),
                    gender=randint(0,1),
                    height=randint(150,170),
                    occupied=choice([True,False]),
                    phone= '0916582487')
service.save()
