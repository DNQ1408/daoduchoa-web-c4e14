from mlab import mlab_connect
from models.river import river
mlab_connect()

africa = river.objects(continent='Africa')
if africa is None:
    print('Not found')
else:
    print(africa)

print('*'*30)

s_america_lt_1000 = river.objects(continent='S. America', length__lt=1000)
if s_america_lt_1000 is None:
    print('Not found')
else:
    print(s_america_lt_1000)
