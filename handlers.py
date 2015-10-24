import json
from tornado import websocket, web, gen
from game import Player, Game, PlayerClick
import msg
from utils import getRandom

players = {}
free_players = []
sockets = {}

ACTION_FIELD = 'action'
PLAY_ACTION = 'play'
ID = 'id'
X = 'x'
Y = 'y'
TIME = 'time'
MSG = 'msg'
NEXT_ROUND = 'next'

class SocketHandler(websocket.WebSocketHandler):

    @gen.coroutine
    def open(self):
        id = getRandom()
        player = Player(id, self)
        players[id] = player
        sockets[self] = id;

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
        if message[ACTION_FIELD] == NEXT_ROUND:
            players[message[ID]].game.nextRound()


    def on_close(self):
        players[sockets[self]].game.rageQuit(sockets[self])

        id = sockets[self]

        player1 = players[id].game.player1
        player2 = players[id].game.player2

        del sockets[player1.socket]
        del sockets[player2.socket]
        del players[player1.id]
        del players[player2.id]

        print 'connection closed...'

class FriendHandler(websocket.WebSocketHandler):

    def open(self):
        id = getRandom()
        self.player = Player(id, self)
        players[id] = self.player
        self.write_message(msg.init(id))

    def on_message(self, message):
        message = json.loads(message)
        try:
            message[ID]
        except:
            raise web.HTTPError(400, "ERROR: No id.")

        print players
        if message[ACTION_FIELD] == 'friend':
            Game(self.player, players[message[MSG]]).start()

        if message[ACTION_FIELD] == PLAY_ACTION:
            players[message[ID]].endGame(PlayerClick(message[X], message[Y], message[TIME]))

    def on_close(self):
        print 'connection closed...'

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.htm")