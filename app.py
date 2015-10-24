import os
from tornado import web, ioloop, websocket

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}


class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        print 'connection opened...'
        self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        self.write_message("The server says: " + message + " back at you")
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
