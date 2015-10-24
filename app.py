import os
import json
import msg
from tornado import web, ioloop, websocket
from game import Player, Game
from utils import getRandom

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}

players = {}
free_players = []

ACTION_FIELD = 'action'
PLAY_ACTION = 'play'
ID = 'id'
X = 'x'
Y = 'y'
TIME = 'time'


class PlayerClick(object):

    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time


class SocketHandler(websocket.WebSocketHandler):

    def open(self):
        id = getRandom()
        player = Player(id, self)
        players[id] = player
        print 'connection opened with id =', id

        self.write_message(msg.init(id))

        if len(free_players) != 0:
            # match waiting player
            another_player = free_players.pop()
            Game(player, another_player).start()
        else:
            # wait for another player
            free_players.append(player)



    def on_message(self, message):
        message = json.loads(message)
        try:
            message[ID]
        except:
            raise web.HTTPError(400, "ERROR: No id.")

        if message[ACTION_FIELD] == PLAY_ACTION:
            players[message[ID]].endGame(PlayerClick(message[X], message[Y], message[TIME]))

        for id in players:
            players[id].socket.write_message(msg.send(message["msg"]))

    def on_close(self):
        print 'connection closed...'


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/socket', SocketHandler)
], **settings)

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    application.listen(port)
    ioloop.IOLoop.instance().start()
