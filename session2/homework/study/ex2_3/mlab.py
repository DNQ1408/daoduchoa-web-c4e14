import mongoengine

# mongodb://:<dbpassword>@ds059546.mlab.com:59546/winter
#mongodb://<dbuser>:<dbpassword>@ds135519.mlab.com:35519/a-task-v2

host = "ds059546.mlab.com"
port = 59546
db_name = "winter"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
