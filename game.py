from msg import gameStart, gameEnd
from utils import generateCity


class Game(object):

    completed = False

    def __init__(self, id, player1, player2):
        self.id = id
        player1.setGame(id)
        self.player1 = player1
        player2.setGame(id)
        self.player2 = player2

    def start(self):
        self.city = generateCity()
        start = gameStart(self.city)
        self.player1.socket.write_message(start)
        self.player2.socket.write_message(start)

    def end(self):
        if self.completed:
            winner = self.chooseWinner()
            game_end_message = gameEnd(winner)
            self.player1.socket.write_message(game_end_message)
            self.player2.socket.write_message(game_end_message)
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

    def setGame(self, game):
        self.game = game

class City(object):

    def __init__(self, name, country, x, y):
        self.name = name
        self.country = country
        self.x = x
        self.y = y

    def __str__(self):
        return str({"name": self.name, "country": self.country, "x": self.x, "y": self.y})
