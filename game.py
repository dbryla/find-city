from msg import gameStart, gameEnd
from utils import generateCity


class Game(object):

    completed = False

    def __init__(self, player1, player2):
        player1.setGame(self)
        self.player1 = player1
        player2.setGame(self)
        self.player2 = player2

    def start(self):
        self.city = generateCity()
        start = gameStart(self.city)
        self.player1.socket.write_message(start)
        self.player2.socket.write_message(start)

    def end(self):
        if self.completed:
            game_end_message = gameEnd(self.chooseWinner())
            self.player1.socket.write_message(game_end_message)
            self.player2.socket.write_message(game_end_message)
        else:
            self.completed = True

    def chooseWinner(self):
        "TODO: chooseWinner"


class Player(object):

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket

    def setPartner(self, player):
        self.partner = player

    def setGame(self, game):
        self.game = game

    def endGame(self, click):
        self.click = click
        self.game.end()

class City(object):

    def __init__(self, name, country, x, y):
        self.name = name
        self.country = country
        self.x = x
        self.y = y

    def __str__(self):
        return str({"name": self.name, "country": self.country, "x": self.x, "y": self.y})
