import os
import random
from tornado import web, ioloop, websocket
from game import Player

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}

players = {}
free_sockets = {}
games = {}

class SocketHandler(websocket.WebSocketHandler):

    def open(self):
        id = self.get_random()
        players[id] = Player(id, self)

        print 'connection opened with id =', id
        self.write_message({"id": id})

        '''
        if len(free_sockets) != 0:
            # match waiting player
            another_player = free_sockets.popitem()
            games[another_player.id + ':' + id] =
        # wait for another player
        '''



    def on_message(self, message):
        for id in players:
            players[id].socket.write_message({"msg": message})

        print 'received:', message

    def on_close(self):
        print 'connection closed...'

    def get_random(self):
        return random.randint(1000000, 9999999)


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
