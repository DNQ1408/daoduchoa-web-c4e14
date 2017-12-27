from mlab import mlab_connect
from models.service import Service

mlab_connect()

# service = Service.objects()[0]
# print(service.id)
# for service in all_services:
#     print(service.name)
# id_to_find ='5a3a854da6db3a2b38e4c5da'
# # first = Service.objects(id='5a362df2a6db3a3a44757128').first() # regular
# rivera = Service.objects().with_id(id_to_find) #id only
#
# if rivera is None:
#     print('Not found')
# else:
#     print(rivera.name)
#     #first.delete()
#     rivera.update(set__occupied=False) # toán tử: set, inc
#     print(rivera.occupied)
#     rivera.reload()
#     print(rivera.occupied)


girl_160 = Service.objects(gender=0, height__gte=160)
print(girl_160)

first_girl_160 = Service.objects(gender=0, height__gte=160).first()
if first_girl_160 is not None:
    first_girl_160.delete()
else:
    print('Not found')

girl_160_change = Service.objects(gender=0, height__gte=160)
if girl_160_change is None:
    print('Not found')
else:
    girl_160_change.update(set_occupied=False)
