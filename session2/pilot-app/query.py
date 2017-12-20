from mlab import mlab_connect
from models.service import Service

mlab_connect()

all_services = Service.objects()
for service in all_services:
    print(service.name)
