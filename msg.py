def gameStart(city):
    return {"action": "start", "msg": str(city)}

def gameWait():
    return {"action": "wait", "msg": "5 sec to start"}

def gameEnd(winner):
    return {"action": "end", "msg": winner}

def init(id):
    return {"action": "init", "msg": id}

def send(msg):
    return {"action": "msg", "msg": msg}
