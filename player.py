import time


class Player(object):
    def __init__(self, id, socket):
        self.id = id
        self.socket = socket
        self.click = None
        self.game = None
        self.record = 0

    def setPartner(self, player):
        self.partner = player

    def setGame(self, game):
        self.game = game

    def setRecord(self, record):
        self.record = record

    def endGame(self, click):
        if not self.click:
            self.click = click
            self.click.time = self.game.calculateTime(time.time())
            self.game.end()


class PlayerClick(object):
    time = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class City(object):
    def __init__(self, name, country, x, y):
        self.name = name
        self.country = country
        self.x = x
        self.y = y

    def __str__(self):
        return str({"name": self.name, "country": self.country, "x": self.x, "y": self.y})