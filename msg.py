def gameStart(city):
    return {"action": "start", "msg": city}

def gameEnd():
    return "TODO"

def init(id):
    return {"action": "init", "id": id}

def send(msg):
    return {"action": "msg", "msg": msg}
