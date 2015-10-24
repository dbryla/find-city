from threading import Timer
from msg import gameStart, gameEnd, gameWait
from utils import generateCity, distance
import time


class Game(object):
    completed = False
    timeout = True

    def __init__(self, player1, player2):
        self.round_number = 1
        player1.setGame(self)
        self.player1 = player1
        player2.setGame(self)
        self.player2 = player2
        self.result1 = 0
        self.result2 = 0

    def start(self):
        self.city = generateCity()
        wait = gameWait()
        start = gameStart(self.city)
        self.sendToPlayers(wait)
        time.sleep(5)
        self.sendToPlayers(start)
        self.timer = Timer(15.0, self.timeoutFunction)
        self.timer.start()

    def timeoutFunction(self):
        if self.timeout:
            self.end(True)

    def end(self, timed = False):
        if self.completed:
            self.completed = False
            self.timeout = False
            self.timer.cancel()
            self.timeout = True
            game_end_message = gameEnd(self.chooseWinner(timed))
            self.round_number += 1
            self.player1.click = None
            self.player2.click = None
            self.sendToPlayers(game_end_message)
            if self.round_number <= 10:
                self.start()
        else:
            self.completed = True

    def returnPlayerData(self, player):
        player_x = player.click.x
        player_y = player.click.y
        return ({"x": player_x, "y": player_y, "time": player.click.time},
                distance(player_x, player_y, self.city.x, self.city.y))

    def chooseWinner(self, timed = False):
        if timed:
            print 'timeout occurs'
            if not self.player1.click and not self.player2.click:
                return {}
            elif self.player2.click:
                player2, dist2 = self.returnPlayerData(self.player2)
                point2 = 10000 / dist2
                self.result2 = self.result2 +  point2
                return {"players":
                    [
                        {"id": self.player1.id, "win": False, "point": 0, "result": self.result1},
                        {"id": self.player2.id, "win": True, "dist": dist2, "point": point2,
                         "click": player2, "result": self.result2}
                    ],
                    "location": {"x": self.city.x, "y": self.city.y}
                }
            else:
                player1, dist1 = self.returnPlayerData(self.player1)
                point1 = 10000 / dist1
                self.result1 = self.result1 +  point1
                return {"players":
                    [
                        {"id": self.player1.id, "win": True, "dist": dist1, "point": point1,
                         "click": player1, "result": self.result2},
                        {"id": self.player2.id, "win": False, "point": 0, "result": self.result2},
                    ],
                    "location": {"x": self.city.x, "y": self.city.y}
                }
        else:
            player1, dist1 = self.returnPlayerData(self.player1)
            player2, dist2 = self.returnPlayerData(self.player2)
            result1 = dist1 + player1["time"]
            result2 = dist2 + player2["time"]

            point1 = 10000 / dist1
            self.result1 = self.result1 +  point1
            point2 = 10000 / dist2
            self.result2 = self.result2 +  point2

        return {"players":
            [
                {"id": self.player1.id, "win": result1 < result2, "dist": dist1, "point": point1,
                 "click": player1, "result": self.result1},
                {"id": self.player2.id, "win": result1 > result2, "dist": dist2, "point": point2,
                 "click": player2, "result": self.result2}
            ],
            "location": {"x": self.city.x, "y": self.city.y}
        }

    def rageQuit(self, id):
        if id != self.player1.id:
            self.player1.socket.write_message({"action": "quit"})
        if id != self.player2.id:
            self.player2.socket.write_message({"action": "quit"})

    def sendToPlayers(self, txt):
        self.player1.socket.write_message(txt)
        self.player2.socket.write_message(txt)


class Player(object):
    def __init__(self, id, socket):
        self.id = id
        self.socket = socket
        self.click = None
        self.game = None

    def setPartner(self, player):
        self.partner = player

    def setGame(self, game):
        self.game = game

    def endGame(self, click):
        if not self.click:
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
