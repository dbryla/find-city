import json
from tornado import websocket, web, gen
import db
from game import Game
import msg
from player import PlayerClick, Player
from utils import getRandom

players = {}
free_players = []
sockets = {}

ACTION_FIELD = 'action'
PLAY_ACTION = 'play'
ID = 'id'
X = 'x'
Y = 'y'
MSG = 'msg'
RECORD_ACTION = 'record'
LIST_ACTION ='list'

def close(self):
    id = sockets[self]

    if players[id] in free_players:
        free_players.remove(players[id])

    if players[id].game:
        players[sockets[self]].game.rageQuit(sockets[self])

        player1 = players[id].game.player1
        player2 = players[id].game.player2

        if player1.record == 0:
            del sockets[player1.socket]
            del players[player1.id]
        if player2.record == 0:
            del sockets[player2.socket]
            del players[player2.id]

    print 'connection closed...'

class SocketHandler(websocket.WebSocketHandler):

    @gen.coroutine
    def open(self):
        id = getRandom()
        player = Player(id, self)
        players[id] = player
        sockets[self] = id

        print 'connection opened with id =', id

        self.write_message(msg.init(id))

        if len(free_players) != 0:
            print 'match waiting player'
            another_player = free_players.pop()
            Game(player, another_player).start()
        else:
            print 'wait for another player'
            free_players.append(player)



    def on_message(self, message):
        message = json.loads(message)
        try:
            message[ID]
        except:
            raise web.HTTPError(400, "ERROR: No id.")

        if message[ACTION_FIELD] == PLAY_ACTION:
            players[message[ID]].endGame(PlayerClick(message[X], message[Y]))
        elif message[ACTION_FIELD] == RECORD_ACTION:
            db.saveRecord(message[MSG], players[message[ID]].record)
            rows = db.readRecords()
            players[message[ID]].socket.write_message(msg.showRank(rows))
        elif message[ACTION_FIELD] == LIST_ACTION:
            rows = db.readRecords()
            self.write_message(msg.showRank(rows))

    def on_close(self):
        close(self)

class FriendHandler(websocket.WebSocketHandler):

    @gen.coroutine
    def open(self):
        id = getRandom()
        self.player = Player(id, self)
        players[id] = self.player
        sockets[self] = id

        print 'connection opened with id =', id

        self.write_message(msg.init(id))

    def on_message(self, message):
        message = json.loads(message)
        try:
            message[ID]
        except:
            raise web.HTTPError(400, "ERROR: No id.")
        if message[ACTION_FIELD] == PLAY_ACTION:
            players[message[ID]].endGame(PlayerClick(message[X], message[Y]))
        elif message[ACTION_FIELD] == RECORD_ACTION:
            db.saveRecord(message[MSG], players[message[ID]].record)
            rows = db.readRecords()
            players[message[ID]].socket.write_message(msg.showRank(rows))
        elif message[ACTION_FIELD] == LIST_ACTION:
            rows = db.readRecords()
            self.write_message(msg.showRank(rows))
        elif message[ACTION_FIELD] == 'friend':
            if message[MSG] in players:
                if not self.player.game or not players[message[MSG]].game:
                    Game(self.player, players[message[MSG]]).start()
                else:
                    self.write_message(msg.noFriend())
            else:
                self.write_message(msg.noFriend())

    def on_close(self):
        close(self)

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.htm")