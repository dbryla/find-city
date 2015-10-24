import os
from tornado import web, ioloop, websocket
from game import Player, Game
from utils import get_random

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}

players = {}
free_players = []
games = {}

class SocketHandler(websocket.WebSocketHandler):

    def open(self):
        id = get_random()
        player =  Player(id, self)
        players[id] = player

        print 'connection opened with id =', id
        self.write_message({"id": id})

        if len(free_players) != 0:
            # match waiting player
            another_player = free_players.pop()
            game = Game(id, player, another_player)
            games[get_random()] = game
            game.start()
        else:
            # wait for another player
            free_players.append(player)



    def on_message(self, message):
        for id in players:
            players[id].socket.write_message({"msg": message})

        print 'received:', message

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
