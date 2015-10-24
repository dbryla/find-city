import os

from tornado import web, ioloop
from db import createDB
from handlers import IndexHandler, SocketHandler, FriendHandler


settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "autoreload": True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/socket', SocketHandler),
    (r'/friend', FriendHandler)
], **settings)

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    application.listen(port)
    createDB()
    ioloop.IOLoop.instance().start()
