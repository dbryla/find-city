from utils import generateCity


class Game(object):

    def __init__(self, id, player1, player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2

    def start(self):
        self.city = generateCity()

class Player(object):

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket

    def setPartner(self, player):
        self.partner = player

class City(object):
    pass