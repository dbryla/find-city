import os
import json
import sqlite3

from tornado import web, ioloop, websocket

import msg
from game import Player, Game, PlayerClick
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
MSG = 'msg'

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


    def on_close(self):
        print 'connection closed...'

class FriendHandler(websocket.WebSocketHandler):

    def open(self):
        id = getRandom()
        self.player = Player(id, self)
        players[id] = self.player
        print 'connection opened with id =', id

        self.write_message(msg.init(id))


    def on_message(self, message):
        message = json.loads(message)
        try:
            message[ID]
        except:
            raise web.HTTPError(400, "ERROR: No id.")

        if message[ACTION_FIELD] == 'friend':
            Game(self.player.id, players[message[MSG]]).start()

        if message[ACTION_FIELD] == PLAY_ACTION:
            players[message[ID]].endGame(PlayerClick(message[X], message[Y], message[TIME]))


    def on_close(self):
        print 'connection closed...'

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/socket', SocketHandler),
    (r'/friend', FriendHandler)
], **settings)

port = int(os.environ.get('PORT', 8080))

def createDB():
    dbPath = os.path.join(os.path.join(os.path.dirname(__file__), "db"), 'cities.db')
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    '''
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
            raise

    '''
    connection.close()
    #return result

if __name__ == '__main__':
    application.listen(port)
    createDB()
    ioloop.IOLoop.instance().start()
