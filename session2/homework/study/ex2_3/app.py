from mlab import mlab_connect
from models.service import Service

mlab_connect()

mlab_connect()

record = Service.objects.get(id='5a3629c4a6db3a30a8d74630')
record.delete()
