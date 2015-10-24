from msg import gameStart, gameEnd, gameWait
from utils import generateCity, distance
import time


class Game(object):
    completed = False
    ready_for_next_round = False

    def __init__(self, player1, player2):
        self.round_number = 1
        player1.setGame(self)
        self.player1 = player1
        player2.setGame(self)
        self.player2 = player2

    def start(self):
        if self.round_number == 10:
            return
        self.city = generateCity()
        wait = gameWait()
        start = gameStart(self.city)
        self.sendToPlayers(wait)
        time.sleep(5)
        self.sendToPlayers(start)

    def nextRound(self):
        if self.ready_for_next_round:
            self.ready_for_next_round = False
            self.start()
        else:
            self.ready_for_next_round = True

    def end(self):
        if self.completed:
            game_end_message = gameEnd(self.chooseWinner())
            self.round_number += 1
            self.sendToPlayers(game_end_message)
        else:
            self.completed = True

    def chooseWinner(self):
        dist1 = distance(self.player1.click.x, self.player1.click.y, self.city.x, self.city.y)
        dist2 = distance(self.player2.click.x, self.player2.click.y, self.city.x, self.city.y)

        time1 = self.player1.click.time
        time2 = self.player2.click.time

        result1 = dist1 + time1
        result2 = dist2 + time2

        return [
            {"id": self.player1.id, "win": result1 < result2, "dist": dist1, "point": 10000 / dist1},
            {"id": self.player2.id, "win": result1 > result2, "dist": dist2, "point": 10000 / dist2}
        ]

    def sendToPlayers(self, txt):
        self.player1.socket.write_message(txt)
        self.player2.socket.write_message(txt)


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


class PlayerClick(object):
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time


class City(object):
    def __init__(self, name, country, x, y):
        self.name = name
        self.country = country
        self.x = x
        self.y = y

    def __str__(self):
        return str({"name": self.name, "country": self.country, "x": self.x, "y": self.y})
