from tornado import web
from msg import gameStart, gameEnd
from utils import generateCity


class Game(object):

    def __init__(self, id, player1, player2):
        self.id = id
        player1.setGame(id)
        self.player1 = player1
        player2.setGame(id)
        self.player2 = player2

    def start(self):
        self.city = generateCity()
        self.player1.socket.write_message(gameStart())
        self.player2.socket.write_message(gameStart())

    def end(self):
        if self.completed:
            winner = self.chooseWinner()
            self.player1.socket.write_message(gameEnd())
            self.player2.socket.write_message(gameEnd())
            pass
        else:
            self.completed = True

    def chooseWinner(self):
        pass


class Player(object):

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket

    def setPartner(self, player):
        self.partner = player

class City(object):
    pass