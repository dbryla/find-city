import os
import json
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
games = {}


class SocketHandler(websocket.WebSocketHandler):

    def open(self):
        id = getRandom()
        player = Player(id, self)
        players[id] = player

        print 'connection opened with id =', id
        self.write_message({"id": id})

        if len(free_players) != 0:
            # match waiting player
            another_player = free_players.pop()
            game_id = getRandom()
            game = Game(game_id, player, another_player)
            games[game_id] = game
            game.start()
        else:
            # wait for another player
            free_players.append(player)



    def on_message(self, message):

        msg = json.loads(message)
        try:
            msg["id"]
        except:
            raise web.HTTPError(400, "ERROR: No id.")

        for id in players:
            players[id].socket.write_message({"msg": msg["msg"]})

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
